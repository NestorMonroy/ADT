#!/bin/bash
################################################################################
# scripts/java-info.sh
# Version: 1.0.0
#
# Proposito:
#   Diagnostico local del toolchain Java portable + PlantUML dentro del proyecto.
#   No requiere configuracion global (no usa JAVA_HOME ni PATH global).
#
# Uso:
#   ./scripts/java-info.sh
#   ./scripts/java-info.sh --no-plantuml
#
# Salida:
#   - Rutas detectadas
#   - java -version (portable si existe, si no, java del sistema)
#   - plantuml.jar -version (si existe y no se deshabilita)
#
# Comportamiento:
#   - Sin errores silenciosos: cualquier fallo detiene la ejecucion con mensaje claro.
################################################################################

set -e

# ------------------------------------------------------------------------------
# Colores (mismos tonos que el resto de scripts del proyecto)
# ------------------------------------------------------------------------------
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

CHECK_PLANTUML=1

# ------------------------------------------------------------------------------
# Argumentos
# ------------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
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
      echo -e "${RED}Opcion desconocida: $1${NC}"
      exit 1
      ;;
  esac
done

log() {
  echo -e "[ $(date '+%Y-%m-%d %H:%M:%S') ] $1"
}

fail() {
  echo ""
  echo "ERROR: $1"
  echo ""
  exit 1
}

# Ejecuta un comando y falla si el exit code no es 0.
exec_cmd() {
  local title="$1"
  shift
  echo ""
  log "$title"
  set +e
  local out
  out="$("$@" 2>&1)"
  local code=$?
  set -e
  if [ $code -ne 0 ]; then
    echo "$out"
    fail "Comando fallo con exit code $code en: $title"
  fi
  if [ -n "$out" ]; then
    echo "$out"
  fi
}

# ------------------------------------------------------------------------------
# Resolver raiz del repo asumiendo:
#   repo_root/scripts/java-info.sh
# ------------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Contrato del proyecto
JAVA_PORTABLE_WIN="$REPO_ROOT/tools/java/jdk-17/bin/java.exe"
JAVA_PORTABLE_NIX="$REPO_ROOT/tools/java/jdk-17/bin/java"
PLANTUML_JAR="$REPO_ROOT/tools/plantuml.jar"

# Seleccion de java:
# 1) Java portable Windows (si se ejecuta desde Git Bash/MSYS en Windows)
# 2) Java portable Unix (si algun dia se usa)
# 3) java del sistema (PATH)
JAVA_BIN=""
if [ -f "$JAVA_PORTABLE_WIN" ]; then
  JAVA_BIN="$JAVA_PORTABLE_WIN"
elif [ -x "$JAVA_PORTABLE_NIX" ]; then
  JAVA_BIN="$JAVA_PORTABLE_NIX"
else
  if command -v java >/dev/null 2>&1; then
    JAVA_BIN="java"
  else
    JAVA_BIN=""
  fi
fi

echo ""
echo "======================================================================"
echo "JAVA-INFO (Unix) - Diagnostico de Java portable + PlantUML"
echo "======================================================================"
echo ""

log "Repo root:    $REPO_ROOT"
log "JAVA_BIN:     ${JAVA_BIN:-NO_ENCONTRADO}"
log "PLANTUML_JAR: $PLANTUML_JAR"
echo ""

# 1) Validar Java
log "Validando Java..."
if [ -z "$JAVA_BIN" ]; then
  fail "No se encontro Java. Instala Java portable con scripts/setup_java.sh (si aplica) o instala java en el sistema."
fi

exec_cmd "java -version" "$JAVA_BIN" -version

# 2) Validar PlantUML JAR (opcional)
if [ $CHECK_PLANTUML -eq 1 ]; then
  echo ""
  log "Validando PlantUML JAR..."
  if [ ! -f "$PLANTUML_JAR" ]; then
    fail "No se encontro 'plantuml.jar' en '$PLANTUML_JAR'."
  fi

  exec_cmd "PlantUML -version (java -jar plantuml.jar -version)" "$JAVA_BIN" -jar "$PLANTUML_JAR" -version
else
  echo ""
  log "CHECK_PLANTUML deshabilitado. Omitiendo validacion de PlantUML."
fi

echo ""
log "Diagnostico completado correctamente."
echo ""
