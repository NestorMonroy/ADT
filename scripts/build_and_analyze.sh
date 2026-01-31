#!/bin/bash
# ============================================================
# Script: build_and_analyze.sh
# Version: 1.0.0
# Purpose: Build Sphinx + Real-time analysis of WARNING/ERROR/CRITICAL
# Date: 2026-01-31
# ============================================================

set -o pipefail

# ============================================================
# SCRIPT METADATA
# ============================================================

SCRIPT_NAME="$(basename "$0")"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR="${REPO_ROOT}"
LOG_DIR="${BASE_DIR}/.mywork/build-logs"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="${LOG_DIR}/build-fase1-${TIMESTAMP}.txt"

# Flags
QUIET=0
VERBOSE=0
DRY_RUN=0

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

    # Verify BASE_DIR exists
    if [ ! -d "$BASE_DIR" ]; then
        die "Base directory does not exist: $BASE_DIR"
    fi
    log "[OK] Base directory: $BASE_DIR"
    dbg "BASE_DIR validated: $BASE_DIR"

    # Verify Makefile exists
    if [ ! -f "$BASE_DIR/Makefile" ]; then
        die "Makefile not found in: $BASE_DIR"
    fi
    log "[OK] Makefile found"
    dbg "Makefile path: $BASE_DIR/Makefile"

    # Create log directory if needed
    if [ ! -d "$LOG_DIR" ]; then
        dbg "Creating log directory: $LOG_DIR"
        mkdir -p "$LOG_DIR" || die "Could not create: $LOG_DIR"
    fi
    log "[OK] Log directory: $LOG_DIR"
    dbg "LOG_DIR validated: $LOG_DIR"

    # Verify tools
    command -v make >/dev/null 2>&1 || die "make is not installed"
    command -v grep >/dev/null 2>&1 || die "grep is not installed"
    command -v sed >/dev/null 2>&1 || die "sed is not installed"
    log "[OK] Tools available: make, grep, sed"
    dbg "All required tools validated"

    log ""
}

# ============================================================
# BUILD FUNCTION
# ============================================================

run_build() {
    dbg "Starting Sphinx build"

    banner "STARTING SPHINX BUILD"

    log "Project: $BASE_DIR"
    log "Log file: $LOG_FILE"
    log "Timestamp: $TIMESTAMP"
    log ""
    hsep
    log ""

    # Change to project directory
    dbg "Changing to directory: $BASE_DIR"
    cd "$BASE_DIR" || die "Could not change to: $BASE_DIR"

    # Build with real-time filtering
    log "Executing make html..."
    log ""

    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would execute: make html"
        BUILD_EXIT=0
    else
        make html 2>&1 | tee "$LOG_FILE" | \
            grep --color=always -E "WARNING:|ERROR:|CRITICAL:|$"
        BUILD_EXIT=${PIPESTATUS[0]}
    fi

    dbg "Build exit code: $BUILD_EXIT"

    log ""
    hsep
    log ""

    # Clean ANSI codes from log
    if [ "$DRY_RUN" -eq 0 ]; then
        dbg "Cleaning ANSI codes from log file"
        sed -i 's/\x1B\[[0-9;]*[JKmsu]//g' "$LOG_FILE"
    fi

    # Report result
    if [ $BUILD_EXIT -eq 0 ]; then
        log "[OK] Build completed successfully"
    else
        log "[FAIL] Build failed with exit code: $BUILD_EXIT"
        log "       (Partial log will be analyzed for diagnostics)"
    fi

    log ""

    return $BUILD_EXIT
}

# ============================================================
# ANALYSIS FUNCTION
# ============================================================

analyze_log() {
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
        # Count issues
        WARNING_COUNT=$(grep -c 'WARNING:' "$LOG_FILE" 2>/dev/null || echo 0)
        ERROR_COUNT=$(grep -c 'ERROR:' "$LOG_FILE" 2>/dev/null || echo 0)
        CRITICAL_COUNT=$(grep -c 'CRITICAL:' "$LOG_FILE" 2>/dev/null || echo 0)
        TOTAL_ISSUES=$((WARNING_COUNT + ERROR_COUNT + CRITICAL_COUNT))

        dbg "WARNING count: $WARNING_COUNT"
        dbg "ERROR count: $ERROR_COUNT"
        dbg "CRITICAL count: $CRITICAL_COUNT"
        dbg "TOTAL issues: $TOTAL_ISSUES"

        # Display summary
        log "WARNING:  $WARNING_COUNT"
        log "ERROR:    $ERROR_COUNT"
        log "CRITICAL: $CRITICAL_COUNT"
        hsep
        log "TOTAL:    $TOTAL_ISSUES"
    fi

    log ""
    hsep
    log ""

    # Log file info
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

OPTIONS:
    -h, --help          Show this help message
    -q, --quiet         Suppress normal output
    -v, --verbose       Enable verbose/debug output
    -n, --dry-run       Show what would be done without executing

EXAMPLES:
    $SCRIPT_NAME                # Normal execution
    $SCRIPT_NAME -v             # Verbose mode
    $SCRIPT_NAME -q             # Quiet mode
    $SCRIPT_NAME -n             # Dry-run mode

OUTPUT:
    Log file: $LOG_DIR/build-fase1-TIMESTAMP.txt

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
            *)
                die "Unknown option: $1 (use -h for help)"
                ;;
        esac
    done
}

# ============================================================
# MAIN
# ============================================================

main() {
    dbg "Script started: $SCRIPT_NAME"
    dbg "Script directory: $SCRIPT_DIR"
    dbg "Repository root: $REPO_ROOT"
    dbg "QUIET=$QUIET, VERBOSE=$VERBOSE, DRY_RUN=$DRY_RUN"

    # Validate environment
    validate_environment

    # Run build
    run_build
    BUILD_RESULT=$?

    # Analyze log
    analyze_log

    # Display tail
    display_tail

    # Final summary
    sep
    if [ $BUILD_RESULT -eq 0 ]; then
        log "[OK] Script completed successfully"
    else
        log "[WARN] Script completed with build errors"
    fi
    sep

    dbg "Script finished with exit code: $BUILD_RESULT"

    exit $BUILD_RESULT
}

# ============================================================
# EXECUTE
# ============================================================

parse_args "$@"
main