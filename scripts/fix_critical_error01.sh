#!/bin/bash
# ============================================================
# Script: fix_critical_error01.sh
# Version: 1.0.0
# Purpose: Fix 22 CRITICAL issues in error_01_omisiones.rst
# Date: 2026-02-01
# ============================================================
# 
# This script fixes RST section title issues:
# - Pattern A (6 cases): Remove leading spaces from title and underline
# - Pattern B (16 cases): Remove leading spaces + fix underline length
#
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

TARGET_FILE="${REPO_ROOT}/source/06_casos_practicos/errores_comunes/error_01_omisiones.rst"
BACKUP_DIR="${REPO_ROOT}/.mywork/backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/error_01_omisiones.rst.backup-${TIMESTAMP}"

# Flags
QUIET=0
VERBOSE=0
DRY_RUN=0

# ============================================================
# PATTERN DATA
# ============================================================

# Pattern A: Lines with equal lengths (only remove leading spaces)
# Format: "line_number:title_chars:underline_chars"
declare -a PATTERN_A=(
    "154:12:12"  # Introducción
    "431:12:12"  # Introducción
    "463:16:16"  # 7.1.1 Subsección
    "467:16:16"  # 7.1.2 Subsección
    "487:16:16"  # 7.2.1 Subsección
    "491:16:16"  # 7.2.2 Subsección
)

# Pattern B: Lines where underline has 1 extra character
# Format: "line_number:title_chars:underline_chars"
declare -a PATTERN_B=(
    "158:7:7"    # Content
    "162:10:10"  # Motivation
    "166:4:4"    # Form
    "178:11:11"  # Referencias
    "435:7:7"    # Content
    "439:10:10"  # Motivation
    "443:4:4"    # Form
    "447:26:26"  # 7.1 Infrastructure Level 1
    "451:7:7"    # Content
    "455:10:10"  # Motivation
    "459:4:4"    # Form
    "471:26:26"  # 7.2 Infrastructure Level 2
    "475:7:7"    # Content
    "479:10:10"  # Motivation
    "483:4:4"    # Form
    "503:11:11"  # Referencias
)

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
    printf '=%.0s' {1..70}
    echo
}

hsep() { 
    printf -- '-%.0s' {1..70}
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
    
    # Verify target file exists
    if [ ! -f "$TARGET_FILE" ]; then
        die "Target file not found: $TARGET_FILE"
    fi
    log "[OK] Target file: $(basename "$TARGET_FILE")"
    dbg "TARGET_FILE: $TARGET_FILE"
    
    # Verify we're in a git repo
    if ! git -C "$REPO_ROOT" rev-parse --git-dir >/dev/null 2>&1; then
        die "Not in a git repository: $REPO_ROOT"
    fi
    log "[OK] Git repository detected"
    
    # Check git status
    if [ -n "$(git -C "$REPO_ROOT" status --porcelain "$TARGET_FILE")" ]; then
        log "[WARNING] Target file has uncommitted changes"
        if [ "$DRY_RUN" -eq 0 ]; then
            read -p "Continue anyway? (y/n) " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                die "Aborted by user"
            fi
        fi
    fi
    
    # Create backup directory if needed
    if [ ! -d "$BACKUP_DIR" ]; then
        dbg "Creating backup directory: $BACKUP_DIR"
        mkdir -p "$BACKUP_DIR" || die "Could not create: $BACKUP_DIR"
    fi
    log "[OK] Backup directory: $BACKUP_DIR"
    
    echo
}

# ============================================================
# BACKUP FUNCTION
# ============================================================

create_backup() {
    banner "CREATING BACKUP"
    
    cp "$TARGET_FILE" "$BACKUP_FILE" || die "Failed to create backup"
    log "[OK] Backup created: $(basename "$BACKUP_FILE")"
    dbg "Backup path: $BACKUP_FILE"
    
    echo
}

# ============================================================
# ANALYSIS FUNCTIONS
# ============================================================

analyze_line() {
    local line_num="$1"
    local title_line=$((line_num))
    local underline_line=$((line_num + 1))
    
    local title=$(sed -n "${title_line}p" "$TARGET_FILE")
    local underline=$(sed -n "${underline_line}p" "$TARGET_FILE")
    
    local title_len=$(echo -n "$title" | wc -c)
    local underline_len=$(echo -n "$underline" | wc -c)
    
    dbg "Line $title_line: '$title' (len=$title_len)"
    dbg "Line $underline_line: '$underline' (len=$underline_len)"
    
    echo "$title_len:$underline_len"
}

# ============================================================
# PATTERN A: Remove leading spaces only
# ============================================================

fix_pattern_a() {
    local line_num="$1"
    local expected_title_len="$2"
    local expected_underline_len="$3"
    
    local title_line=$line_num
    local underline_line=$((line_num + 1))
    
    dbg "Fixing Pattern A - Line $title_line"
    
    # Get current content
    local title=$(sed -n "${title_line}p" "$TARGET_FILE")
    local underline=$(sed -n "${underline_line}p" "$TARGET_FILE")
    
    # Remove leading space
    local new_title="${title# }"
    local new_underline="${underline# }"
    
    # Verify lengths
    local new_title_len=$(echo -n "$new_title" | wc -c)
    local new_underline_len=$(echo -n "$new_underline" | wc -c)
    
    if [ "$new_title_len" -ne "$expected_title_len" ]; then
        log "[WARNING] Line $title_line: Expected length $expected_title_len, got $new_title_len"
    fi
    
    if [ "$new_underline_len" -ne "$expected_underline_len" ]; then
        log "[WARNING] Line $underline_line: Expected length $expected_underline_len, got $new_underline_len"
    fi
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would fix line $title_line (Pattern A)"
        dbg "  Before: '$title'"
        dbg "  After:  '$new_title'"
        return 0
    fi
    
    # Apply fix
    sed -i "${title_line}s/^ //" "$TARGET_FILE"
    sed -i "${underline_line}s/^ //" "$TARGET_FILE"
    
    log "[OK] Fixed line $title_line (Pattern A)"
}

# ============================================================
# PATTERN B: Remove leading spaces + fix underline length
# ============================================================

fix_pattern_b() {
    local line_num="$1"
    local expected_title_len="$2"
    local expected_underline_len="$3"
    
    local title_line=$line_num
    local underline_line=$((line_num + 1))
    
    dbg "Fixing Pattern B - Line $title_line"
    
    # Get current content
    local title=$(sed -n "${title_line}p" "$TARGET_FILE")
    local underline=$(sed -n "${underline_line}p" "$TARGET_FILE")
    
    # Remove leading space from title
    local new_title="${title# }"
    
    # Remove leading space from underline AND remove one '='
    local temp_underline="${underline# }"
    local new_underline="${temp_underline#=}"
    
    # Verify lengths
    local new_title_len=$(echo -n "$new_title" | wc -c)
    local new_underline_len=$(echo -n "$new_underline" | wc -c)
    
    if [ "$new_title_len" -ne "$expected_title_len" ]; then
        log "[WARNING] Line $title_line: Expected length $expected_title_len, got $new_title_len"
    fi
    
    if [ "$new_underline_len" -ne "$expected_underline_len" ]; then
        log "[WARNING] Line $underline_line: Expected length $expected_underline_len, got $new_underline_len"
    fi
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would fix line $title_line (Pattern B)"
        dbg "  Title before:     '$title' (len=$(echo -n "$title" | wc -c))"
        dbg "  Title after:      '$new_title' (len=$new_title_len)"
        dbg "  Underline before: '$underline' (len=$(echo -n "$underline" | wc -c))"
        dbg "  Underline after:  '$new_underline' (len=$new_underline_len)"
        return 0
    fi
    
    # Apply fix
    # Remove leading space from title
    sed -i "${title_line}s/^ //" "$TARGET_FILE"
    
    # Remove leading space and one '=' from underline
    sed -i "${underline_line}s/^ =/=/" "$TARGET_FILE"
    
    log "[OK] Fixed line $title_line (Pattern B)"
}

# ============================================================
# MAIN EXECUTION
# ============================================================

process_corrections() {
    banner "PROCESSING CORRECTIONS"
    
    local total_fixes=0
    local pattern_a_count=${#PATTERN_A[@]}
    local pattern_b_count=${#PATTERN_B[@]}
    
    log "Pattern A fixes: $pattern_a_count"
    log "Pattern B fixes: $pattern_b_count"
    log "Total fixes: $((pattern_a_count + pattern_b_count))"
    echo
    
    # Process Pattern A
    hsep
    log "Processing Pattern A (remove leading spaces only)"
    hsep
    
    for entry in "${PATTERN_A[@]}"; do
        IFS=':' read -r line_num title_len underline_len <<< "$entry"
        fix_pattern_a "$line_num" "$title_len" "$underline_len"
        ((total_fixes++))
    done
    
    echo
    
    # Process Pattern B
    hsep
    log "Processing Pattern B (remove spaces + fix underline)"
    hsep
    
    for entry in "${PATTERN_B[@]}"; do
        IFS=':' read -r line_num title_len underline_len <<< "$entry"
        fix_pattern_b "$line_num" "$title_len" "$underline_len"
        ((total_fixes++))
    done
    
    echo
    banner "CORRECTIONS COMPLETED"
    log "Total fixes applied: $total_fixes"
    echo
}

# ============================================================
# VERIFICATION
# ============================================================

verify_fixes() {
    banner "VERIFICATION"
    
    log "Checking for remaining issues..."
    
    # Simple check: count lines with leading space followed by underline
    local remaining=$(awk '/^ [A-Z0-9]/ {line=NR; getline; if (/^ =+$/) print line}' "$TARGET_FILE" | wc -l)
    
    if [ "$remaining" -eq 0 ]; then
        log "[OK] No remaining issues detected"
    else
        log "[WARNING] $remaining potential issues remain"
        log "Run 'make html' to verify"
    fi
    
    echo
}

# ============================================================
# USAGE
# ============================================================

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]

Fix 22 CRITICAL RST section title issues in error_01_omisiones.rst

OPTIONS:
    -d, --dry-run       Show what would be done without making changes
    -v, --verbose       Enable verbose output
    -q, --quiet         Suppress non-error output
    -h, --help          Show this help message

EXAMPLES:
    # Dry-run to see what would be fixed
    $SCRIPT_NAME --dry-run

    # Apply fixes
    $SCRIPT_NAME

    # Apply fixes with verbose output
    $SCRIPT_NAME --verbose

PATTERNS:
    Pattern A (6 fixes):  Remove leading spaces from title and underline
    Pattern B (16 fixes): Remove leading spaces + remove 1 '=' from underline

EOF
    exit 0
}

# ============================================================
# ARGUMENT PARSING
# ============================================================

parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -d|--dry-run)
                DRY_RUN=1
                log "DRY-RUN mode enabled"
                shift
                ;;
            -v|--verbose)
                VERBOSE=1
                shift
                ;;
            -q|--quiet)
                QUIET=1
                shift
                ;;
            -h|--help)
                usage
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
    parse_arguments "$@"
    
    banner "FIX CRITICAL - error_01_omisiones.rst"
    log "Script: $SCRIPT_NAME"
    log "Version: 1.0.0"
    log "Target: $(basename "$TARGET_FILE")"
    [ "$DRY_RUN" -eq 1 ] && log "Mode: DRY-RUN"
    echo
    
    validate_environment
    
    if [ "$DRY_RUN" -eq 0 ]; then
        create_backup
    else
        log "[DRY-RUN] Backup skipped"
        echo
    fi
    
    process_corrections
    
    if [ "$DRY_RUN" -eq 0 ]; then
        verify_fixes
    fi
    
    banner "EXECUTION SUMMARY"
    if [ "$DRY_RUN" -eq 1 ]; then
        log "DRY-RUN completed - no changes made"
        log "Run without --dry-run to apply fixes"
    else
        log "Fixes applied successfully"
        log "Backup: $BACKUP_FILE"
        log ""
        log "Next steps:"
        log "  1. Review changes: git diff $TARGET_FILE"
        log "  2. Test build:     make clean && make html"
        log "  3. Commit:         git add && git commit"
    fi
    echo
}

# Run main
main "$@"
