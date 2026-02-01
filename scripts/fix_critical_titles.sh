#!/bin/bash
# ============================================================
# Script: fix_critical_titles.sh
# Version: 2.1.0
# Purpose: Fix CRITICAL RST section title issues across all files
# Date: 2026-02-01
# ============================================================
# 
# This script scans all .rst files in source/ and fixes:
# - Leading spaces in section titles
# - Incorrect underline lengths (adjusts to match title length)
#
# Changes in v2.1.0:
# - Now correctly adjusts underline lengths to match title
# - Generates underline with exact number of '=' as title characters
# - Fixes both Pattern A and Pattern B completely
#
# Patterns detected:
# - Pattern A: Title and underline both have leading space
# - Pattern B: Leading space + underline has extra character
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

SOURCE_DIR="${REPO_ROOT}/source"
BACKUP_DIR="${REPO_ROOT}/archivados/rst_backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
REPORT_FILE="${REPO_ROOT}/.mywork/fix_critical_titles_${TIMESTAMP}.log"

# Flags
QUIET=0
VERBOSE=0
DRY_RUN=0
SKIP_BACKUP=0

# Statistics
TOTAL_FILES=0
TOTAL_FIXES=0
FILES_MODIFIED=0

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

report() {
    echo "$*" >> "$REPORT_FILE"
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
    
    # Verify source directory exists
    if [ ! -d "$SOURCE_DIR" ]; then
        die "Source directory not found: $SOURCE_DIR"
    fi
    log "[OK] Source directory: $SOURCE_DIR"
    dbg "SOURCE_DIR: $SOURCE_DIR"
    
    # Count RST files
    local rst_count=$(find "$SOURCE_DIR" -name "*.rst" -type f | wc -l)
    log "[OK] Found $rst_count RST files to process"
    
    # Verify we're in a git repo
    if ! git -C "$REPO_ROOT" rev-parse --git-dir >/dev/null 2>&1; then
        die "Not in a git repository: $REPO_ROOT"
    fi
    log "[OK] Git repository detected"
    
    # Create backup directory if needed
    if [ "$SKIP_BACKUP" -eq 0 ]; then
        if [ ! -d "$BACKUP_DIR" ]; then
            dbg "Creating backup directory: $BACKUP_DIR"
            mkdir -p "$BACKUP_DIR" || die "Could not create: $BACKUP_DIR"
        fi
        log "[OK] Backup directory: $BACKUP_DIR"
    else
        log "[SKIP] Backup disabled"
    fi
    
    # Create report file directory
    mkdir -p "$(dirname "$REPORT_FILE")" 2>/dev/null
    
    echo
}

# ============================================================
# BACKUP FUNCTION
# ============================================================

create_backup() {
    local source_file="$1"
    
    if [ "$SKIP_BACKUP" -eq 1 ]; then
        dbg "Backup skipped for: $(basename "$source_file")"
        return 0
    fi
    
    # Create backup with relative path structure
    local rel_path="${source_file#$SOURCE_DIR/}"
    local backup_file="${BACKUP_DIR}/${TIMESTAMP}/$(dirname "$rel_path")"
    
    mkdir -p "$backup_file" || die "Failed to create backup directory"
    
    cp "$source_file" "$backup_file/$(basename "$source_file")" || die "Failed to backup: $source_file"
    
    dbg "Backed up: $source_file -> $backup_file/$(basename "$source_file")"
}

# ============================================================
# ANALYSIS FUNCTIONS
# ============================================================

# Detect problematic lines in a file
# Returns: space-separated list of line numbers
detect_issues() {
    local file="$1"
    
    # Find lines where:
    # - Current line starts with space + letter/number
    # - Next line starts with space + equals signs
    awk '
        /^ [A-Za-z0-9]/ {
            title_line = NR
            title = $0
            getline
            if (/^ =+$/) {
                print title_line
            }
        }
    ' "$file"
}

# Analyze specific line to determine pattern
# Returns: "A:title_len:underline_len" or "B:title_len:underline_len"
analyze_line() {
    local file="$1"
    local line_num="$2"
    
    local title_line=$line_num
    local underline_line=$((line_num + 1))
    
    local title=$(sed -n "${title_line}p" "$file")
    local underline=$(sed -n "${underline_line}p" "$file")
    
    # Get lengths with leading space
    local title_len=$(echo -n "$title" | wc -c)
    local underline_len=$(echo -n "$underline" | wc -c)
    
    # Remove leading space to get actual content lengths
    local clean_title="${title# }"
    local clean_underline="${underline# }"
    
    local clean_title_len=$(echo -n "$clean_title" | wc -c)
    local clean_underline_len=$(echo -n "$clean_underline" | wc -c)
    
    # Determine pattern
    if [ "$title_len" -eq "$underline_len" ]; then
        # Pattern A: lengths match (both have leading space, correct number of =)
        echo "A:$clean_title_len:$clean_title_len"
    else
        # Pattern B: lengths don't match (underline has extra =)
        # After removing leading space, underline still has 1 extra =
        local target_len=$clean_title_len
        echo "B:$target_len:$target_len"
    fi
}

# ============================================================
# FIX FUNCTIONS
# ============================================================

# Pattern A: Remove leading spaces AND adjust underline length
fix_pattern_a() {
    local file="$1"
    local line_num="$2"
    
    local title_line=$line_num
    local underline_line=$((line_num + 1))
    
    dbg "Pattern A - Line $title_line in $(basename "$file")"
    
    # Read current lines
    local title=$(sed -n "${title_line}p" "$file")
    local underline=$(sed -n "${underline_line}p" "$file")
    
    # Remove leading space from title
    local clean_title="${title# }"
    
    # Count characters in clean title
    local title_length=${#clean_title}
    
    # Generate correct underline
    local correct_underline=$(printf '=%.0s' $(seq 1 $title_length))
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would fix line $title_line in $(basename "$file")"
        dbg "  Before: '$title'"
        dbg "  After:  '$clean_title' (underline: $title_length chars)"
        return 0
    fi
    
    # Remove leading space from title
    sed -i "${title_line}s/^ //" "$file"
    
    # Replace underline with correct length
    sed -i "${underline_line}s|.*|${correct_underline}|" "$file"
    
    log "[FIXED] Line $title_line in $(basename "$file") (Pattern A)"
    report "[FIXED] $(basename "$file"):$title_line (Pattern A)"
    
    ((TOTAL_FIXES++))
}

# Pattern B: Remove leading spaces AND adjust underline length
fix_pattern_b() {
    local file="$1"
    local line_num="$2"
    
    local title_line=$line_num
    local underline_line=$((line_num + 1))
    
    dbg "Pattern B - Line $title_line in $(basename "$file")"
    
    # Read current lines
    local title=$(sed -n "${title_line}p" "$file")
    local underline=$(sed -n "${underline_line}p" "$file")
    
    # Remove leading space from title
    local clean_title="${title# }"
    
    # Count characters in clean title
    local title_length=${#clean_title}
    
    # Generate correct underline
    local correct_underline=$(printf '=%.0s' $(seq 1 $title_length))
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would fix line $title_line in $(basename "$file")"
        dbg "  Title before:     '$title'"
        dbg "  Title after:      '$clean_title'"
        dbg "  Underline before: '$underline'"
        dbg "  Underline after:  '$correct_underline' ($title_length chars)"
        return 0
    fi
    
    # Remove leading space from title
    sed -i "${title_line}s/^ //" "$file"
    
    # Replace underline with correct length
    sed -i "${underline_line}s|.*|${correct_underline}|" "$file"
    
    log "[FIXED] Line $title_line in $(basename "$file") (Pattern B)"
    report "[FIXED] $(basename "$file"):$title_line (Pattern B)"
    
    ((TOTAL_FIXES++))
}

# ============================================================
# PROCESS FILE
# ============================================================

process_file() {
    local file="$1"
    
    dbg "Processing: $file"
    
    # Detect issues
    local issues=$(detect_issues "$file")
    
    if [ -z "$issues" ]; then
        dbg "No issues found in: $(basename "$file")"
        return 0
    fi
    
    # Count issues
    local issue_count=$(echo "$issues" | wc -w)
    log ""
    log "File: $(basename "$file")"
    log "  Issues found: $issue_count"
    
    # Create backup before any fixes
    if [ "$DRY_RUN" -eq 0 ]; then
        create_backup "$file"
    fi
    
    # Process each issue
    local file_fixes=0
    for line_num in $issues; do
        # Analyze to determine pattern
        local analysis=$(analyze_line "$file" "$line_num")
        local pattern=$(echo "$analysis" | cut -d: -f1)
        
        dbg "Line $line_num: Pattern $pattern"
        
        if [ "$pattern" = "A" ]; then
            fix_pattern_a "$file" "$line_num"
            ((file_fixes++))
        elif [ "$pattern" = "B" ]; then
            fix_pattern_b "$file" "$line_num"
            ((file_fixes++))
        fi
    done
    
    if [ $file_fixes -gt 0 ]; then
        ((FILES_MODIFIED++))
    fi
}

# ============================================================
# MAIN PROCESSING
# ============================================================

process_all_files() {
    banner "PROCESSING RST FILES"
    
    # Find all RST files
    local files=$(find "$SOURCE_DIR" -name "*.rst" -type f | sort)
    
    TOTAL_FILES=$(echo "$files" | wc -l)
    log "Total files to scan: $TOTAL_FILES"
    echo
    
    # Process each file
    while IFS= read -r file; do
        process_file "$file"
    done <<< "$files"
    
    echo
}

# ============================================================
# REPORT GENERATION
# ============================================================

generate_report() {
    banner "EXECUTION SUMMARY"
    
    log "Files scanned:    $TOTAL_FILES"
    log "Files modified:   $FILES_MODIFIED"
    log "Total fixes:      $TOTAL_FIXES"
    
    if [ "$DRY_RUN" -eq 0 ] && [ "$TOTAL_FIXES" -gt 0 ]; then
        log ""
        log "Report saved:     $REPORT_FILE"
        log "Backups saved to: $BACKUP_DIR/$TIMESTAMP/"
    fi
    
    echo
    
    # Write summary to report
    {
        echo ""
        echo "========================================"
        echo "EXECUTION SUMMARY"
        echo "========================================"
        echo "Date:             $(date)"
        echo "Files scanned:    $TOTAL_FILES"
        echo "Files modified:   $FILES_MODIFIED"
        echo "Total fixes:      $TOTAL_FIXES"
        echo "Mode:             $([ "$DRY_RUN" -eq 1 ] && echo "DRY-RUN" || echo "APPLIED")"
    } >> "$REPORT_FILE"
}

# ============================================================
# VERIFICATION
# ============================================================

verify_fixes() {
    if [ "$DRY_RUN" -eq 1 ]; then
        return 0
    fi
    
    banner "POST-FIX VERIFICATION"
    
    log "Scanning for remaining issues..."
    
    local remaining=0
    while IFS= read -r file; do
        local issues=$(detect_issues "$file")
        if [ -n "$issues" ]; then
            local count=$(echo "$issues" | wc -w)
            ((remaining += count))
        fi
    done < <(find "$SOURCE_DIR" -name "*.rst" -type f)
    
    if [ "$remaining" -eq 0 ]; then
        log "[OK] No remaining issues detected"
    else
        log "[WARNING] $remaining potential issues remain"
        log "         Run script again or check manually"
    fi
    
    echo
}

# ============================================================
# USAGE
# ============================================================

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]

Fix CRITICAL RST section title issues in all .rst files under source/

This script detects and fixes:
  - Section titles with leading spaces
  - Underlines with incorrect lengths

PATTERNS:
  Pattern A: Remove leading spaces from title and underline
  Pattern B: Remove leading spaces + fix underline length (-1 char)

OPTIONS:
    -d, --dry-run       Show what would be done without making changes
    -v, --verbose       Enable verbose output
    -q, --quiet         Suppress non-error output
    --no-backup         Skip creating backups (use with caution!)
    -h, --help          Show this help message

EXAMPLES:
    # Dry-run to see what would be fixed
    $SCRIPT_NAME --dry-run

    # Apply fixes to all files
    $SCRIPT_NAME

    # Apply fixes with verbose output
    $SCRIPT_NAME --verbose

    # Quick scan without backups (dry-run implied for safety)
    $SCRIPT_NAME --dry-run --no-backup

BACKUPS:
    All modified files are backed up to:
    $BACKUP_DIR/<timestamp>/

REPORT:
    A detailed report is saved to:
    .mywork/fix_critical_titles_<timestamp>.log

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
            --no-backup)
                SKIP_BACKUP=1
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
    
    banner "FIX CRITICAL TITLES - ALL RST FILES"
    log "Script: $SCRIPT_NAME"
    log "Version: 2.1.0"
    log "Target: $SOURCE_DIR"
    [ "$DRY_RUN" -eq 1 ] && log "Mode: DRY-RUN"
    echo
    
    # Initialize report
    {
        echo "========================================"
        echo "FIX CRITICAL TITLES REPORT"
        echo "========================================"
        echo "Date:    $(date)"
        echo "Script:  $SCRIPT_NAME v2.0.0"
        echo "Mode:    $([ "$DRY_RUN" -eq 1 ] && echo "DRY-RUN" || echo "APPLIED")"
        echo ""
    } > "$REPORT_FILE"
    
    validate_environment
    process_all_files
    
    if [ "$DRY_RUN" -eq 0 ]; then
        verify_fixes
    fi
    
    generate_report
    
    if [ "$DRY_RUN" -eq 1 ]; then
        banner "DRY-RUN COMPLETED"
        log "No changes were made"
        log "Run without --dry-run to apply fixes"
    else
        banner "FIXES APPLIED"
        log "Next steps:"
        log "  1. Review changes:  git status"
        log "  2. Check diff:      git diff"
        log "  3. Test build:      make clean && make html"
        log "  4. Commit:          git add && git commit"
    fi
    
    echo
}

# Run main
main "$@"
