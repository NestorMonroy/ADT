#!/usr/bin/env bash
# scripts/plantuml_test.sh
# Version: 1.0.0
#
# Proposito:
#   Probar y validar que PlantUML (tools/plantuml.jar) es un JAR valido y ejecuta correctamente
#   usando Java portable del proyecto (si existe) o java del sistema como fallback.
#
# Uso:
#   ./scripts/plantuml_test.sh
#   ./scripts/plantuml_test.sh --jar tools/plantuml.jar
#   ./scripts/plantuml_test.sh --java tools/java/jdk-17/bin/java.exe
#   ./scripts/plantuml_test.sh --no-render
#   ./scripts/plantuml_test.sh --tmp-dir tools/_tmp
#
# Comportamiento:
#   - Sin errores silenciosos: cualquier fallo termina con exit code != 0 y mensaje claro.
#   - Validaciones:
#       1) El jar existe y size > 0
#       2) Firma ZIP: empieza con "PK"
#       3) java -jar plantuml.jar -version funciona
#       4) (opcional) Render de un diagrama simple en un directorio temporal

set -euo pipefail

JAR_REL="tools/plantuml.jar"
JAVA_REL_WIN="tools/java/jdk-17/bin/java.exe"
JAVA_REL_NIX="tools/java/jdk-17/bin/java"
TMP_DIR_REL="tools/_tmp/plantuml_test"
DO_RENDER=1

usage() {
  cat <<'EOF'
Uso:
  ./scripts/plantuml_test.sh [opciones]

Opciones:
  --jar PATH        Ruta al plantuml.jar (default: tools/plantuml.jar)
  --java PATH       Ruta al ejecutable java (default: usa Java portable si existe, si no java en PATH)
  --tmp-dir PATH    Directorio temporal para pruebas de render (default: tools/_tmp/plantuml_test)
  --no-render       Solo valida jar/version; no intenta renderizar diagrama
  --help, -h        Ayuda
EOF
}

log() {
  printf '[ %s ] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >&2
}

fail() {
  echo "" >&2
  echo "ERROR: $1" >&2
  echo "" >&2
  exit 1
}

# Repo root: repo_root/scripts/plantuml_test.sh
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

JAR_PATH="$REPO_ROOT/$JAR_REL"
TMP_DIR="$REPO_ROOT/$TMP_DIR_REL"
JAVA_PATH=""

while [ $# -gt 0 ]; do
  case "$1" in
    --jar)
      shift
      [ $# -gt 0 ] || fail "Falta valor para --jar"
      JAR_PATH="$REPO_ROOT/$1"
      shift
      ;;
    --java)
      shift
      [ $# -gt 0 ] || fail "Falta valor para --java"
      # si viene relativa, la resolvemos contra repo; si viene absoluta, respetamos
      if [[ "$1" = /* ]] || [[ "$1" =~ ^[A-Za-z]:[\\/].* ]]; then
        JAVA_PATH="$1"
      else
        JAVA_PATH="$REPO_ROOT/$1"
      fi
      shift
      ;;
    --tmp-dir)
      shift
      [ $# -gt 0 ] || fail "Falta valor para --tmp-dir"
      TMP_DIR="$REPO_ROOT/$1"
      shift
      ;;
    --no-render)
      DO_RENDER=0
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      fail "Opcion desconocida: $1"
      ;;
  esac
done

file_size() {
  if command -v stat >/dev/null 2>&1; then
    stat -c%s "$1" 2>/dev/null || wc -c <"$1"
  else
    wc -c <"$1"
  fi
}

zip_signature_ok() {
  [ -f "$1" ] || return 1
  local sig
  sig="$(head -c 2 "$1" 2>/dev/null || true)"
  [ "$sig" = "PK" ]
}

detect_java() {
  local win="$REPO_ROOT/$JAVA_REL_WIN"
  local nix="$REPO_ROOT/$JAVA_REL_NIX"

  if [ -n "$JAVA_PATH" ]; then
    if [ -f "$JAVA_PATH" ] || command -v "$JAVA_PATH" >/dev/null 2>&1; then
      echo "$JAVA_PATH"
      return 0
    fi
    fail "No se encontro el java especificado: $JAVA_PATH"
  fi

  if [ -f "$win" ]; then
    echo "$win"
    return 0
  fi

  if [ -x "$nix" ]; then
    echo "$nix"
    return 0
  fi

  if command -v java >/dev/null 2>&1; then
    echo "java"
    return 0
  fi

  echo ""
}

echo "" >&2
echo "======================================================================" >&2
echo "PLANTUML TEST (sh) v1.0.0" >&2
echo "======================================================================" >&2
echo "" >&2

log "Repo root: $REPO_ROOT"
log "JAR:       $JAR_PATH"
log "TMP_DIR:   $TMP_DIR"
log "RENDER:    $([ "$DO_RENDER" -eq 1 ] && echo "SI" || echo "NO")"
echo "" >&2

# 1) Validar jar existe y size
[ -f "$JAR_PATH" ] || fail "No existe el archivo: $JAR_PATH"

LEN="$(file_size "$JAR_PATH")"
[ "$LEN" -gt 0 ] || fail "El archivo JAR mide 0 bytes: $JAR_PATH"

# 2) Validar firma ZIP
if ! zip_signature_ok "$JAR_PATH"; then
  head_txt="$(head -n 5 "$JAR_PATH" 2>/dev/null || true)"
  fail "El archivo no parece un JAR (no inicia con 'PK'). Primeras lineas:\n$head_txt"
fi
log "JAR valido (size=$LEN, sig=PK)"

# 3) Detectar java y probar version
JAVA_BIN="$(detect_java)"
[ -n "$JAVA_BIN" ] || fail "No se encontro Java (portable no encontrado y java no esta en PATH)."

log "JAVA_BIN:  $JAVA_BIN"
log "Ejecutando: java -jar plantuml.jar -version"
set +e
OUT="$("$JAVA_BIN" -jar "$JAR_PATH" -version 2>&1)"
CODE=$?
set -e
if [ $CODE -ne 0 ]; then
  echo "$OUT" >&2
  fail "Fallo PlantUML -version (exit code $CODE)."
fi
echo "$OUT" >&2
log "PlantUML -version OK"

# 4) Render opcional
if [ "$DO_RENDER" -eq 1 ]; then
  log "Preparando prueba de render..."
  mkdir -p "$TMP_DIR"

  DIAGRAM_SRC="$TMP_DIR/test.puml"
  cat >"$DIAGRAM_SRC" <<'PUML'
@startuml
skinparam monochrome true
Alice -> Bob: hello
Bob --> Alice: ok
@enduml
PUML

  log "Diagrama de prueba: $DIAGRAM_SRC"
  log "Ejecutando render PNG..."
  set +e
  OUT2="$("$JAVA_BIN" -jar "$JAR_PATH" -tpng "$DIAGRAM_SRC" 2>&1)"
  CODE2=$?
  set -e
  if [ $CODE2 -ne 0 ]; then
    echo "$OUT2" >&2
    fail "Fallo render PNG (exit code $CODE2)."
  fi
  if [ -n "$OUT2" ]; then
    echo "$OUT2" >&2
  fi

  PNG_OUT="$TMP_DIR/test.png"
  [ -f "$PNG_OUT" ] || fail "No se genero el PNG esperado: $PNG_OUT"
  PNG_LEN="$(file_size "$PNG_OUT")"
  [ "$PNG_LEN" -gt 0 ] || fail "El PNG generado tiene size 0: $PNG_OUT"

  log "Render OK: $PNG_OUT (size=$PNG_LEN)"
fi

echo "" >&2
log "PLANTUML TEST completado correctamente."
echo "" >&2
