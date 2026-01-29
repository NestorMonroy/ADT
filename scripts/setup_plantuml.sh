#!/usr/bin/env bash
# scripts/setup_plantuml.sh
# Version: 1.0.1
#
# Proposito:
#   Descargar e instalar tools/plantuml.jar de forma reproducible e idempotente.
#
# Uso:
#   ./scripts/setup_plantuml.sh
#   ./scripts/setup_plantuml.sh --dry-run
#   ./scripts/setup_plantuml.sh --force
#   ./scripts/setup_plantuml.sh --version 1.2026.1
#
# Comportamiento:
#   - Idempotente: si tools/plantuml.jar ya es valido, no hace nada (a menos que --force).
#   - Sin errores silenciosos: si algo falla, termina con error y mensaje claro.
#   - Valida: size > 0, firma ZIP "PK", y si hay java disponible ejecuta "-version".

set -euo pipefail

DRY_RUN=0
FORCE=0
VERSION=""

# Logs a STDERR para no contaminar salidas capturadas por $(...)
log() {
  printf '[ %s ] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >&2
}

fail() {
  echo "" >&2
  echo "ERROR: $1" >&2
  echo "" >&2
  exit 1
}

run_or_dry() {
  if [ "$DRY_RUN" -eq 1 ]; then
    log "[DRY-RUN] $*"
    return 0
  fi
  "$@"
}

usage() {
  cat <<'EOF'
Uso:
  ./scripts/setup_plantuml.sh [--dry-run] [--force] [--version X.YYYY.Z]

Opciones:
  --dry-run        Simula acciones sin cambiar archivos
  --force          Reinstala aunque ya exista un plantuml.jar valido
  --version        Fuerza una version especifica (ej: 1.2026.1)
  --help, -h       Muestra esta ayuda
EOF
}

# -----------------------------
# Args
# -----------------------------
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --force)   FORCE=1; shift ;;
    --version)
      shift
      [ $# -gt 0 ] || fail "Falta valor para --version"
      VERSION="$1"
      shift
      ;;
    --help|-h) usage; exit 0 ;;
    *) fail "Opcion desconocida: $1" ;;
  esac
done

# -----------------------------
# Repo root: repo_root/scripts/setup_plantuml.sh
# -----------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

TOOLS_DIR="$REPO_ROOT/tools"
DOWNLOADS_DIR="$TOOLS_DIR/_downloads"
DEST_JAR="$TOOLS_DIR/plantuml.jar"

# Java portable (contrato del proyecto)
JAVA_PORTABLE_WIN="$TOOLS_DIR/java/jdk-17/bin/java.exe"
JAVA_PORTABLE_NIX="$TOOLS_DIR/java/jdk-17/bin/java"

# -----------------------------
# Helpers
# -----------------------------
require_cmd() {
  command -v "$1" >/dev/null 2>&1 || fail "Comando requerido no encontrado: $1"
}

zip_signature_ok() {
  [ -f "$1" ] || return 1
  local sig
  sig="$(head -c 2 "$1" 2>/dev/null || true)"
  [ "$sig" = "PK" ]
}

file_size() {
  if command -v stat >/dev/null 2>&1; then
    stat -c%s "$1" 2>/dev/null || wc -c <"$1"
  else
    wc -c <"$1"
  fi
}

detect_java() {
  if [ -f "$JAVA_PORTABLE_WIN" ]; then
    echo "$JAVA_PORTABLE_WIN"
    return 0
  fi
  if [ -x "$JAVA_PORTABLE_NIX" ]; then
    echo "$JAVA_PORTABLE_NIX"
    return 0
  fi
  if command -v java >/dev/null 2>&1; then
    echo "java"
    return 0
  fi
  echo ""
}

validate_existing_jar() {
  [ -f "$DEST_JAR" ] || return 1
  local len
  len="$(file_size "$DEST_JAR")"
  if [ "$len" -gt 0 ] && zip_signature_ok "$DEST_JAR"; then
    return 0
  fi
  return 1
}

detect_latest_version() {
  # IMPORTANTE: esta funcion debe imprimir SOLO la version por STDOUT.
  local page="$DOWNLOADS_DIR/plantuml_download_page.html"
  local url="https://plantuml.com/download"

  log "Obteniendo pagina de descargas para detectar version estable: $url"
  run_or_dry mkdir -p "$DOWNLOADS_DIR"
  run_or_dry curl -L --fail --retry 3 --retry-delay 2 "$url" -o "$page"

  if [ "$DRY_RUN" -eq 1 ]; then
    echo "<auto>"
    return 0
  fi

  # Extrae la primera ocurrencia de vX.YYYY.Z
  local v
  v="$(grep -Eo 'v[0-9]+\.[0-9]+\.[0-9]+' "$page" | head -n 1 | sed 's/^v//')"
  [ -n "$v" ] || fail "No se pudo detectar la version desde $url. Usa --version X.YYYY.Z"
  echo "$v"
}

download_plantuml_jar() {
  # IMPORTANTE: esta funcion debe imprimir SOLO la ruta tmp por STDOUT.
  local v="$1"
  local tmp="$DOWNLOADS_DIR/plantuml-$v.jar"
  local url="https://sourceforge.net/projects/plantuml.mirror/files/v${v}/plantuml.jar/download"

  log "Descargando PlantUML JAR (v${v}) desde SourceForge mirror"
  run_or_dry mkdir -p "$DOWNLOADS_DIR"
  run_or_dry curl -L --fail --retry 3 --retry-delay 2 "$url" -o "$tmp"
  echo "$tmp"
}

validate_downloaded_jar() {
  local jar="$1"
  [ -f "$jar" ] || fail "No se encontro el archivo descargado: $jar"

  local len
  len="$(file_size "$jar")"
  [ "$len" -gt 0 ] || fail "La descarga resulto en archivo de 0 bytes: $jar (posible bloqueo/proxy/redirect roto)."

  if ! zip_signature_ok "$jar"; then
    local head_txt
    head_txt="$(head -n 5 "$jar" 2>/dev/null || true)"
    fail "El archivo descargado no parece un JAR (no inicia con 'PK'). Primeras lineas:\n$head_txt"
  fi

  log "Validacion basica OK (size=$len, sig=PK)"
}

install_jar() {
  local src="$1"
  log "Instalando JAR en destino del proyecto: $DEST_JAR"
  run_or_dry mkdir -p "$TOOLS_DIR"
  run_or_dry cp -f "$src" "$DEST_JAR"
}

validate_execution_with_java() {
  local java_bin="$1"
  if [ -z "$java_bin" ]; then
    log "No se encontro java para validacion de ejecucion (portable no encontrado y java no esta en PATH)."
    log "Puedes validar manualmente con: tools/java/jdk-17/bin/java.exe -jar tools/plantuml.jar -version"
    return 0
  fi

  log "Validando ejecucion: $java_bin -jar tools/plantuml.jar -version"
  if [ "$DRY_RUN" -eq 1 ]; then
    log "[DRY-RUN] $java_bin -jar $DEST_JAR -version"
    return 0
  fi

  set +e
  local out
  out="$("$java_bin" -jar "$DEST_JAR" -version 2>&1)"
  local code=$?
  set -e

  if [ $code -ne 0 ]; then
    echo "$out" >&2
    fail "PlantUML fallo al ejecutar. Revisa si el jar fue bloqueado, truncado o reemplazado por HTML."
  fi

  # PlantUML imprime por STDOUT; lo reenviamos a STDERR para mantener estilo de logs
  echo "$out" >&2
  log "PlantUML instalado y validado correctamente."
}

# -----------------------------
# Main
# -----------------------------
echo "" >&2
echo "======================================================================" >&2
echo "SETUP PLANTUML JAR (tools/plantuml.jar) v1.0.1" >&2
if [ "$DRY_RUN" -eq 1 ]; then
  echo "MODO: DRY-RUN (Simulacion)" >&2
else
  echo "MODO: REAL" >&2
fi
if [ "$FORCE" -eq 1 ]; then
  echo "FORCE: Habilitado" >&2
fi
echo "======================================================================" >&2
echo "" >&2

log "Repo root:     $REPO_ROOT"
log "Destino JAR:   $DEST_JAR"
log "Downloads dir: $DOWNLOADS_DIR"
echo "" >&2

require_cmd curl
require_cmd grep
require_cmd sed
require_cmd head

if [ "$FORCE" -eq 0 ] && validate_existing_jar; then
  log "PlantUML JAR ya existe y es valido. No se realizan cambios."
  exit 0
fi

if [ -z "$VERSION" ]; then
  VERSION="$(detect_latest_version)"
fi

log "Version seleccionada: $VERSION"

TMP_JAR="$(download_plantuml_jar "$VERSION")"
if [ "$DRY_RUN" -eq 0 ]; then
  validate_downloaded_jar "$TMP_JAR"
fi

install_jar "$TMP_JAR"

JAVA_BIN="$(detect_java)"
validate_execution_with_java "$JAVA_BIN"

echo "" >&2
log "Finalizado."
echo "" >&2
