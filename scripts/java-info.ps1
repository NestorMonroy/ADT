# scripts/java-info.ps1
# Version: 1.0.0
#
# Proposito:
#   Diagnostico local del toolchain Java portable + PlantUML dentro del proyecto.
#   No requiere configuracion global (no usa JAVA_HOME ni PATH global).
#
# Uso:
#   powershell -ExecutionPolicy Bypass -File .\scripts\java-info.ps1
#
# Salida:
#   - Rutas detectadas
#   - java.exe -version
#   - plantuml.jar -version (si existe)
#
# Comportamiento:
#   - Sin errores silenciosos: cualquier fallo detiene la ejecucion con mensaje claro.

[CmdletBinding()]
param(
    # Si se especifica, el script valida y ejecuta tambien el comando PlantUML.
    [switch]$CheckPlantUml = $true
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Log {
    param([Parameter(Mandatory=$true)][string]$Message)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$ts] $Message"
}

function Fail {
    param([Parameter(Mandatory=$true)][string]$Message)
    Write-Host ""
    Write-Host "ERROR: $Message"
    Write-Host ""
    exit 1
}

function Exec-Cmd {
    param(
        [Parameter(Mandatory=$true)][string]$Title,
        [Parameter(Mandatory=$true)][scriptblock]$Command
    )

    Write-Host ""
    Write-Log $Title
    try {
        $out = & $Command 2>&1
        $code = $LASTEXITCODE
        if ($code -ne 0) {
            Write-Host $out
            Fail "Comando fallo con exit code $code en: $Title"
        }
        if ($out) { $out | ForEach-Object { Write-Host $_ } }
    }
    catch {
        Fail "Excepcion al ejecutar '$Title': $($_.Exception.Message)"
    }
}

# Resolver raiz del repo asumiendo:
#   repo_root/scripts/java-info.ps1
try {
    $repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..") | Select-Object -ExpandProperty Path
}
catch {
    Fail "No se pudo resolver la raiz del repositorio desde: $PSScriptRoot"
}

# Contrato del proyecto
$javaExe = Join-Path $repoRoot "tools\java\jdk-17\bin\java.exe"
$plantumlJar = Join-Path $repoRoot "tools\plantuml.jar"

Write-Host ""
Write-Host "======================================================================"
Write-Host "JAVA-INFO (Windows) - Diagnostico de Java portable + PlantUML"
Write-Host "======================================================================"
Write-Host ""

Write-Log "Repo root:    $repoRoot"
Write-Log "JAVA_EXE:     $javaExe"
Write-Log "PLANTUML_JAR: $plantumlJar"
Write-Host ""

# 1) Validar Java portable
Write-Log "Validando Java portable..."
if (-not (Test-Path -LiteralPath $javaExe)) {
    Fail "No se encontro Java portable en '$javaExe'. Ejecuta el flujo de instalacion (setup_java) y reintenta."
}

Exec-Cmd -Title "java.exe -version" -Command { & $javaExe -version }

# 2) Validar PlantUML JAR (opcional)
if ($CheckPlantUml) {
    Write-Host ""
    Write-Log "Validando PlantUML JAR..."
    if (-not (Test-Path -LiteralPath $plantumlJar)) {
        Fail "No se encontro 'plantuml.jar' en '$plantumlJar'."
    }

    Exec-Cmd -Title "PlantUML -version (java -jar plantuml.jar -version)" -Command { & $javaExe -jar $plantumlJar -version }
}
else {
    Write-Host ""
    Write-Log "CheckPlantUml deshabilitado. Omitiendo validacion de PlantUML."
}

Write-Host ""
Write-Log "Diagnostico completado correctamente."
Write-Host ""
