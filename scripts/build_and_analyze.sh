#!/bin/bash
# ============================================================
# Script: build_and_analyze.sh
# Version: 1.1.0
# Purpose: Build Sphinx + Real-time analysis of WARNING/ERROR/CRITICAL
# Date: 2026-02-01
#
# Enterprise additions:
# - Must run from repo root (/ADT): fail-fast validation
# - CLI flags -> exported env vars (SPHINX_PROFILE, SPHINX_STRICT, etc.)
# - Auditable "BUILD PROFILE (EFFECTIVE)" block in log output
# - Optional builder selection: html | spelling
# ============================================================

set -o pipefail

# ============================================================
# SCRIPT METADATA
# ============================================================

SCRIPT_NAME="$(basename "$0")"
BASE_DIR="$(pwd)"

# ============================================================
# CONFIGURATION
# ============================================================

LOG_DIR="${BASE_DIR}/.mywork/build-logs"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
LOG_FILE="${LOG_DIR}/build-log-${TIMESTAMP}.log"

# Output builder
BUILDER="html"

# Flags (existing)
QUIET=0
VERBOSE=0
DRY_RUN=0

# Enterprise flags (defaults)
PROFILE="enterprise"

STRICT=0
OFFLINE=0
SKIP_INTERSPHINX=0

ENABLE_INTERSPHINX=0
ENABLE_PLANTUML=0
ENABLE_SPELLING=0

CUSTOM_SIDEBAR=0

# Record CLI invocation for audit
CLI_ARGS="$*"

# ============================================================
# LOGGING FUNCTIONS
# ============================================================

log() {
    [ "$QUIET" -eq 1 ] && return 0
    printf '%s\n' "$*"
}

dbg() {
    [ "$VERBOSE" -eq 1 ] && printf '[debug] %s\n' "$*" >&2
}

die() {
    printf '[error] %s\n' "$*" >&2
    exit 1
}

# ============================================================
# SEPARATOR FUNCTIONS
# ============================================================

sep() {
    printf '=%.0s' {1..60}
    echo
}

hsep() {
    printf -- '-%.0s' {1..60}
    echo
}

banner() {
    sep
    log "$1"
    sep
}

# ============================================================
# VALIDATIONS
# ============================================================

validate_environment() {
    dbg "Starting environment validation"

    banner "PRE-EXECUTION VALIDATIONS"

    # Must run from repo root (contract)
    # Validate repository markers in current directory
    if [ ! -f "${BASE_DIR}/Makefile" ]; then
        die "Makefile not found in current directory. Run from repo root (/ADT). Current: ${BASE_DIR}"
    fi
    log "[OK] Makefile found: ${BASE_DIR}/Makefile"

    if [ ! -f "${BASE_DIR}/source/conf.py" ]; then
        die "source/conf.py not found. Run from repo root (/ADT). Current: ${BASE_DIR}"
    fi
    log "[OK] conf.py found: ${BASE_DIR}/source/conf.py"

    if [ ! -d "${BASE_DIR}/source/conf.d" ]; then
        die "source/conf.d not found. Run from repo root (/ADT). Current: ${BASE_DIR}"
    fi
    log "[OK] conf.d directory: ${BASE_DIR}/source/conf.d"

    # Create log directory if needed
    if [ ! -d "$LOG_DIR" ]; then
        dbg "Creating log directory: $LOG_DIR"
        mkdir -p "$LOG_DIR" || die "Could not create: $LOG_DIR"
    fi
    log "[OK] Log directory: $LOG_DIR"

    # Verify tools (base)
    command -v make >/dev/null 2>&1 || die "make is not installed"
    command -v grep >/dev/null 2>&1 || die "grep is not installed"
    command -v sed >/dev/null 2>&1 || die "sed is not installed"
    command -v tee >/dev/null 2>&1 || die "tee is not installed"
    command -v perl >/dev/null 2>&1 || die "perl is not installed (required to clean ANSI codes)"
    log "[OK] Tools available: make, grep, sed, tee, perl"

    # Verify sphinx-build only if builder=spelling (html uses Makefile)
    if [ "$BUILDER" = "spelling" ]; then
        command -v sphinx-build >/dev/null 2>&1 || die "sphinx-build is not installed (required for --builder spelling)"
        log "[OK] Tool available: sphinx-build"
    fi

    # Validate builder value early
    if [ "$BUILDER" != "html" ] && [ "$BUILDER" != "spelling" ]; then
        die "Unknown builder: $BUILDER (expected: html|spelling)"
    fi

    log ""
}

# ============================================================
# CLEAN FUNCTION
# ============================================================

clean_build() {
    dbg "Starting clean"

    banner "CLEANING BUILD DIRECTORY"

    cd "$BASE_DIR" || die "Could not change to: $BASE_DIR"

    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would execute: make clean"
        return 0
    fi

    log "Executing make clean..."
    make clean 2>&1
    CLEAN_EXIT=$?

    if [ $CLEAN_EXIT -eq 0 ]; then
        log "[OK] Clean completed"
    else
        log "[WARN] Clean failed with exit code: $CLEAN_EXIT"
    fi

    log ""

    return $CLEAN_EXIT
}

# ============================================================
# COUNT ISSUES FUNCTION (Pure)
# ============================================================

count_pattern() {
    local log_file="$1"
    local pattern="$2"
    local count

    count=$(grep -c "$pattern" "$log_file" 2>/dev/null || echo "0")
    count=$(echo "$count" | tr -d '[:space:]')
    count=${count:-0}

    echo "$count"
}

# ============================================================
# ANALYSIS FUNCTION
# ============================================================

analyze_log() {
    local warning_count
    local error_count
    local critical_count
    local total_issues

    dbg "Starting log analysis"

    banner "ANALYSIS OF RESULTS"

    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would analyze: $LOG_FILE"
        log "WARNING:  0"
        log "ERROR:    0"
        log "CRITICAL: 0"
        hsep
        log "TOTAL:    0"
    else
        warning_count=$(count_pattern "$LOG_FILE" "WARNING:")
        error_count=$(count_pattern "$LOG_FILE" "ERROR:")
        critical_count=$(count_pattern "$LOG_FILE" "CRITICAL:")
        total_issues=$((warning_count + error_count + critical_count))

        dbg "WARNING count: $warning_count"
        dbg "ERROR count: $error_count"
        dbg "CRITICAL count: $critical_count"
        dbg "TOTAL issues: $total_issues"

        log "WARNING:  $warning_count"
        log "ERROR:    $error_count"
        log "CRITICAL: $critical_count"
        hsep
        log "TOTAL:    $total_issues"
    fi

    log ""
    hsep
    log ""

    log "Log file:"
    log "  $LOG_FILE"
    log ""

    if [ "$DRY_RUN" -eq 0 ] && [ -f "$LOG_FILE" ]; then
        log "Log size:"
        ls -lh "$LOG_FILE" | awk '{print "  " $5}'
        log ""
    fi
}

# ============================================================
# DISPLAY LAST LINES
# ============================================================

display_tail() {
    if [ "$DRY_RUN" -eq 1 ]; then
        return 0
    fi

    if [ ! -f "$LOG_FILE" ]; then
        dbg "Log file does not exist, skipping tail"
        return 0
    fi

    banner "LAST 20 LINES OF LOG"
    log ""
    tail -20 "$LOG_FILE"
    log ""
}

# ============================================================
# USAGE
# ============================================================

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]

Build Sphinx documentation and analyze WARNING/ERROR/CRITICAL messages.

CONTRACT:
    Run this script from the repository root (/ADT). It fails fast otherwise.

OPTIONS:
    -h, --help               Show this help message
    -q, --quiet              Suppress normal output
    -v, --verbose            Enable verbose/debug output
    -n, --dry-run            Show what would be done without executing

    --profile NAME           Set SPHINX_PROFILE (default: enterprise)
    --builder NAME           Build target: html (default) | spelling

    --strict                 Set SPHINX_STRICT=1
    --offline                Set SPHINX_OFFLINE=1
    --skip-intersphinx       Set SPHINX_SKIP_INTERSPHINX=1

    --enable-intersphinx     Set SPHINX_ENABLE_INTERSPHINX=1
    --enable-plantuml        Set SPHINX_ENABLE_PLANTUML=1
    --enable-spelling        Set SPHINX_ENABLE_SPELLING=1
    --custom-sidebar         Set SPHINX_SIDEBAR_CUSTOM=1

EXAMPLES:
    $SCRIPT_NAME
    $SCRIPT_NAME --strict
    $SCRIPT_NAME --offline
    $SCRIPT_NAME --enable-plantuml --custom-sidebar
    $SCRIPT_NAME --builder spelling --enable-spelling
    $SCRIPT_NAME --profile qa --strict --enable-spelling

OUTPUT:
    Log file: $LOG_DIR/build-log-TIMESTAMP.log

EOF
    exit 0
}

# ============================================================
# ARGUMENT PARSING
# ============================================================

parse_args() {
    while [ $# -gt 0 ]; do
        case "$1" in
            -h|--help)
                usage
                ;;
            -q|--quiet)
                QUIET=1
                shift
                ;;
            -v|--verbose)
                VERBOSE=1
                shift
                ;;
            -n|--dry-run)
                DRY_RUN=1
                shift
                ;;
            --profile)
                [ -n "${2:-}" ] || die "Missing value for --profile"
                PROFILE="$2"
                shift 2
                ;;
            --builder)
                [ -n "${2:-}" ] || die "Missing value for --builder"
                BUILDER="$2"
                shift 2
                ;;
            --strict)
                STRICT=1
                shift
                ;;
            --offline)
                OFFLINE=1
                shift
                ;;
            --skip-intersphinx)
                SKIP_INTERSPHINX=1
                shift
                ;;
            --enable-intersphinx)
                ENABLE_INTERSPHINX=1
                shift
                ;;
            --enable-plantuml)
                ENABLE_PLANTUML=1
                shift
                ;;
            --enable-spelling)
                ENABLE_SPELLING=1
                shift
                ;;
            --custom-sidebar)
                CUSTOM_SIDEBAR=1
                shift
                ;;
            *)
                die "Unknown option: $1 (use -h for help)"
                ;;
        esac
    done
}

# ============================================================
# EXPORT ENTERPRISE FLAGS
# ============================================================

export_sphinx_env() {
    export SPHINX_PROFILE="$PROFILE"
    export SPHINX_STRICT="$STRICT"
    export SPHINX_OFFLINE="$OFFLINE"
    export SPHINX_SKIP_INTERSPHINX="$SKIP_INTERSPHINX"
    export SPHINX_ENABLE_INTERSPHINX="$ENABLE_INTERSPHINX"
    export SPHINX_ENABLE_PLANTUML="$ENABLE_PLANTUML"
    export SPHINX_ENABLE_SPELLING="$ENABLE_SPELLING"
    export SPHINX_SIDEBAR_CUSTOM="$CUSTOM_SIDEBAR"
}

# ============================================================
# BUILD FUNCTION
# ============================================================

run_build() {
    local build_exit
    local build_start
    local build_end
    local build_duration

    dbg "Starting Sphinx build"

    banner "STARTING SPHINX BUILD"

    log "PWD:       $BASE_DIR"
    log "Builder:   $BUILDER"
    log "Log file:  $LOG_FILE"
    log "Timestamp: $TIMESTAMP"
    log "Command:   $SCRIPT_NAME $CLI_ARGS"
    log ""

    banner "BUILD PROFILE (EFFECTIVE)"
    log "SPHINX_PROFILE=$SPHINX_PROFILE"
    log "SPHINX_STRICT=$SPHINX_STRICT"
    log "SPHINX_OFFLINE=$SPHINX_OFFLINE"
    log "SPHINX_SKIP_INTERSPHINX=$SPHINX_SKIP_INTERSPHINX"
    log "SPHINX_ENABLE_INTERSPHINX=$SPHINX_ENABLE_INTERSPHINX"
    log "SPHINX_ENABLE_PLANTUML=$SPHINX_ENABLE_PLANTUML"
    log "SPHINX_ENABLE_SPELLING=$SPHINX_ENABLE_SPELLING"
    log "SPHINX_SIDEBAR_CUSTOM=$SPHINX_SIDEBAR_CUSTOM"
    log "BUILDER=$BUILDER"
    log ""

    hsep
    log ""

    cd "$BASE_DIR" || die "Could not change to: $BASE_DIR"

    build_start=$(date +%s)
    dbg "Build start time: $build_start"

    if [ "$BUILDER" = "html" ]; then
        log "Executing make html..."
        log ""

        if [ "$DRY_RUN" -eq 1 ]; then
            log "[DRY-RUN] Would execute: make html"
            build_exit=0
        else
            make html 2>&1 | tee "$LOG_FILE"
            build_exit=${PIPESTATUS[0]}
            dbg "Cleaning ANSI codes from completed log"
            perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$LOG_FILE"
        fi

    elif [ "$BUILDER" = "spelling" ]; then
        log "Executing sphinx-build -b spelling..."
        log ""

        if [ "$DRY_RUN" -eq 1 ]; then
            log "[DRY-RUN] Would execute: sphinx-build -b spelling source _build/spelling"
            build_exit=0
        else
            sphinx-build -b spelling source _build/spelling 2>&1 | tee "$LOG_FILE"
            build_exit=${PIPESTATUS[0]}
            dbg "Cleaning ANSI codes from completed log"
            perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$LOG_FILE"
        fi
    else
        die "Unknown builder: $BUILDER (expected: html|spelling)"
    fi

    build_end=$(date +%s)
    build_duration=$((build_end - build_start))
    dbg "Build end time: $build_end"
    dbg "Build duration: $build_duration seconds"

    log ""
    hsep
    log ""

    if [ $build_exit -eq 0 ]; then
        log "[OK] Build completed successfully"
    else
        log "[FAIL] Build failed with exit code: $build_exit"
        log "       (Partial log will be analyzed for diagnostics)"
    fi

    log ""
    log "Build time: ${build_duration}s"
    log ""

    return $build_exit
}

# ============================================================
# MAIN
# ============================================================

main() {
    local build_result

    dbg "Script started: $SCRIPT_NAME"
    dbg "PWD/Base dir: $BASE_DIR"
    dbg "QUIET=$QUIET, VERBOSE=$VERBOSE, DRY_RUN=$DRY_RUN"
    dbg "PROFILE=$PROFILE, BUILDER=$BUILDER"
    dbg "STRICT=$STRICT, OFFLINE=$OFFLINE, SKIP_INTERSPHINX=$SKIP_INTERSPHINX"
    dbg "ENABLE_INTERSPHINX=$ENABLE_INTERSPHINX, ENABLE_PLANTUML=$ENABLE_PLANTUML, ENABLE_SPELLING=$ENABLE_SPELLING"
    dbg "CUSTOM_SIDEBAR=$CUSTOM_SIDEBAR"

    # Validate environment (also validates contract: must run from repo root)
    validate_environment

    # Export enterprise environment variables for Sphinx (effective policy)
    export_sphinx_env

    # Clean build directory
    clean_build

    # Run build
    run_build
    build_result=$?

    # Analyze log
    analyze_log

    # Display tail
    display_tail

    # Final summary
    sep
    if [ $build_result -eq 0 ]; then
        log "[OK] Script completed successfully"
    else
        log "[WARN] Script completed with build errors"
    fi
    sep

    dbg "Script finished with exit code: $build_result"

    exit $build_result
}

# ============================================================
# EXECUTE
# ============================================================

parse_args "$@"
main