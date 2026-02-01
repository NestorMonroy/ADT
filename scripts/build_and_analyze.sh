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
LOG_FILE="${LOG_DIR}/build-log-${TIMESTAMP}.log"

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
# BUILD FUNCTION
# ============================================================

run_build() {
    local build_exit
    local build_start
    local build_end
    local build_duration
    
    dbg "Starting Sphinx build"
    
    banner "STARTING SPHINX BUILD"
    
    log "Project: $BASE_DIR"
    log "Log file: $LOG_FILE"
    log "Timestamp: $TIMESTAMP"
    log ""
    hsep
    log ""
    
    cd "$BASE_DIR" || die "Could not change to: $BASE_DIR"
    
    log "Executing make html..."
    log ""
    
    build_start=$(date +%s)
    dbg "Build start time: $build_start"
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would execute: make html"
        build_exit=0
    else
        # Write raw output to log file (no filtering to avoid buffering issues)
        make html 2>&1 | tee "$LOG_FILE"
        build_exit=${PIPESTATUS[0]}
        
        # Clean ANSI codes AFTER build completes (avoids buffering)
        dbg "Cleaning ANSI codes from completed log"
        perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$LOG_FILE"
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
        # Count issues using pure function
        warning_count=$(count_pattern "$LOG_FILE" "WARNING:")
        error_count=$(count_pattern "$LOG_FILE" "ERROR:")
        critical_count=$(count_pattern "$LOG_FILE" "CRITICAL:")
        total_issues=$((warning_count + error_count + critical_count))
        
        dbg "WARNING count: $warning_count"
        dbg "ERROR count: $error_count"
        dbg "CRITICAL count: $critical_count"
        dbg "TOTAL issues: $total_issues"
        
        # Display summary
        log "WARNING:  $warning_count"
        log "ERROR:    $error_count"
        log "CRITICAL: $critical_count"
        hsep
        log "TOTAL:    $total_issues"
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
    local build_result
    
    dbg "Script started: $SCRIPT_NAME"
    dbg "Script directory: $SCRIPT_DIR"
    dbg "Repository root: $REPO_ROOT"
    dbg "QUIET=$QUIET, VERBOSE=$VERBOSE, DRY_RUN=$DRY_RUN"
    
    # Validate environment
    validate_environment
    
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
