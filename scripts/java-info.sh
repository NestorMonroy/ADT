#!/usr/bin/env bash
################################################################################
# scripts/java-info.sh
# Version: 1.0.1
#
# Proposito:
#   Diagnostico local del toolchain Java portable + PlantUML dentro del proyecto.
#   No requiere configuracion global (no usa JAVA_HOME ni PATH global).
#
# Uso:
#   ./scripts/java-info.sh
#   ./scripts/java-info.sh --no-plantuml
################################################################################

set -euo pipefail

CHECK_PLANTUML=1

while [ $# -gt 0 ]; do
  case "$1" in
    --no-plantuml)
      CHECK_PLANTUML=0
      shift
      ;;
    --help|-h)
      echo "Uso: $0 [--no-plantuml]"
      exit 0
      ;;
    *)
      echo "ERROR: Opcion desconocida: $1"
      exit 1
      ;;
  esac
done

log() {
  printf '[ %s ] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1"
}

fail() {
  echo ""
  echo "ERROR: $1"
  echo ""
  exit 1
}

exec_cmd() {
  # Ejecuta un comando y falla si exit code != 0.
  # Imprime tanto stdout como stderr.
  local title="$1"
  shift

  echo ""
  log "$title"

  set +e
  local out
  out="$("$@" 2>&1)"
  local code=$?
  set -e

  if [ -n "$out" ]; then
    printf '%s\n' "$out"
  fi

  if [ $code -ne 0 ]; then
    fail "Comando fallo con exit code $code en: $title"
  fi
}

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

JAVA_PORTABLE_WIN="$REPO_ROOT/tools/java/jdk-17/bin/java.exe"
JAVA_PORTABLE_NIX="$REPO_ROOT/tools/java/jdk-17/bin/java"
PLANTUML_JAR="$REPO_ROOT/tools/plantuml.jar"

JAVA_BIN=""
if [ -f "$JAVA_PORTABLE_WIN" ]; then
  JAVA_BIN="$JAVA_PORTABLE_WIN"
elif [ -x "$JAVA_PORTABLE_NIX" ]; then
  JAVA_BIN="$JAVA_PORTABLE_NIX"
elif command -v java >/dev/null 2>&1; then
  JAVA_BIN="java"
else
  JAVA_BIN=""
fi

echo ""
echo "======================================================================"
echo "JAVA-INFO (sh) - Diagnostico de Java portable + PlantUML"
echo "======================================================================"
echo ""

log "Repo root:    $REPO_ROOT"
log "JAVA_BIN:     ${JAVA_BIN:-NO_ENCONTRADO}"
log "PLANTUML_JAR: $PLANTUML_JAR"
echo ""

log "Validando Java..."
[ -n "$JAVA_BIN" ] || fail "No se encontro Java. Instala Java portable con scripts/setup_java.sh o instala java en el sistema."

exec_cmd "java -version" "$JAVA_BIN" -version

if [ "$CHECK_PLANTUML" -eq 1 ]; then
  echo ""
  log "Validando PlantUML JAR..."
  [ -f "$PLANTUML_JAR" ] || fail "No se encontro 'plantuml.jar' en '$PLANTUML_JAR'."

  exec_cmd "PlantUML -version (java -jar plantuml.jar -version)" "$JAVA_BIN" -jar "$PLANTUML_JAR" -version
else
  echo ""
  log "CHECK_PLANTUML deshabilitado. Omitiendo validacion de PlantUML."
fi

echo ""
log "Diagnostico completado correctamente."
echo ""
