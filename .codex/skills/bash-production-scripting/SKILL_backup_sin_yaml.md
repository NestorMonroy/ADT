# Bash Production Scripting

**Version:** 1.0.0  
**Created:** 2026-01-31  
**Purpose:** Best practices for production-grade bash scripts with cross-platform compatibility

---

## Overview

This skill documents battle-tested patterns for writing robust, portable bash scripts that work across Linux, macOS, and Git Bash/MINGW environments. Derived from real-world experience building build automation and logging systems.

---

## Core Principles

1. **Pure ASCII output** - Maximum terminal compatibility
2. **Functional programming** - Pure functions with local variables
3. **Explicit error handling** - Never fail silently
4. **Cross-platform compatibility** - Works on Git Bash/MINGW/Linux/macOS
5. **Clean logs** - No ANSI codes in saved files
6. **No buffering issues** - Real-time output visibility

---

## Script Structure Template

```bash
#!/bin/bash
# ============================================================
# Script: script_name.sh
# Version: 1.0.0
# Purpose: Brief description
# Date: YYYY-MM-DD
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
LOG_DIR="${BASE_DIR}/.logs"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="${LOG_DIR}/script-log-${TIMESTAMP}.log"

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
    exit "${2:-1}"
}

# ============================================================
# SEPARATOR FUNCTIONS (Pure ASCII)
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
# USAGE
# ============================================================

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]

Brief description of what the script does.

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
    Log file: $LOG_DIR/script-log-TIMESTAMP.log
    
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
# MAIN FUNCTIONS
# ============================================================

# Add your main functions here using local variables
# Example:
example_function() {
    local input_file="$1"
    local output_file="$2"
    
    dbg "Processing: $input_file -> $output_file"
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would process $input_file"
        return 0
    fi
    
    # Actual processing here
    
    return 0
}

# ============================================================
# MAIN
# ============================================================

main() {
    local exit_code
    
    dbg "Script started: $SCRIPT_NAME"
    dbg "Script directory: $SCRIPT_DIR"
    dbg "Repository root: $REPO_ROOT"
    dbg "QUIET=$QUIET, VERBOSE=$VERBOSE, DRY_RUN=$DRY_RUN"
    
    # Create log directory
    mkdir -p "$LOG_DIR" || die "Could not create: $LOG_DIR"
    
    # Your main logic here
    banner "SCRIPT EXECUTION"
    
    # Example function call
    example_function "input.txt" "output.txt"
    exit_code=$?
    
    # Final summary
    sep
    if [ $exit_code -eq 0 ]; then
        log "[OK] Script completed successfully"
    else
        log "[FAIL] Script completed with errors"
    fi
    sep
    
    dbg "Script finished with exit code: $exit_code"
    
    exit $exit_code
}

# ============================================================
# EXECUTE
# ============================================================

parse_args "$@"
main
```

---

## Critical Patterns

### 1. ANSI Code Removal (Cross-Platform)

**Problem:** Log files with ANSI escape codes are unreadable.

**Solution:** Use `perl` for maximum portability (works on Git Bash/MINGW/Linux/macOS):

```bash
# Clean ANSI codes from a file
perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$LOG_FILE"
```

**Why perl instead of sed:**
- `sed -i` behavior differs between BSD (macOS) and GNU (Linux)
- `sed` in Git Bash/MINGW doesn't handle `\x1B` reliably
- `perl -i` works identically across all platforms

**CRITICAL:** Clean AFTER writing, not during pipe to avoid buffering issues.

### 2. Avoiding Pipeline Buffering

**Problem:** Processing in pipeline causes output to freeze/buffer.

```bash
# BAD - Causes buffering and freezing:
make html 2>&1 | perl -pe 's/...' | tee "$LOG_FILE"

# GOOD - Write raw, clean after:
make html 2>&1 | tee "$LOG_FILE"
perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$LOG_FILE"
```

**Why:**
- Any processing in pipeline introduces buffering
- `tee` alone does not buffer
- Cleaning after completion avoids all buffering issues

### 3. Line Ending Conversion (CRLF → LF)

**Problem:** Git Bash/MINGW creates files with Windows line endings (CRLF).

**Solution:** Convert in same perl command:

```bash
perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$LOG_FILE"
#                                       ^^^^^^^^ removes \r (CR)
```

### 4. Pure Functions with Local Variables

**Bad:**
```bash
process_file() {
    OUTPUT_DIR="/tmp/output"  # Global variable
    mkdir -p "$OUTPUT_DIR"
}
```

**Good:**
```bash
process_file() {
    local input="$1"
    local output_dir="$2"
    
    mkdir -p "$output_dir" || return 1
    
    # Process...
    
    return 0
}
```

**Benefits:**
- No side effects
- Testable
- Reusable
- Clear inputs/outputs

### 5. Timestamp Generation

```bash
# Always use this format for sortable timestamps
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# Example: 20260131-155030
# Benefits: 
# - Sortable alphabetically
# - No spaces (shell-safe)
# - ISO 8601 compatible
```

### 6. Exit Code Handling

```bash
# Capture exit code from pipeline
make html 2>&1 | tee "$LOG_FILE"
BUILD_EXIT=${PIPESTATUS[0]}  # Get exit code of 'make', not 'tee'

# Return from functions
return $exit_code  # Not 'exit' in functions

# Exit from main
exit $exit_code
```

### 7. Script Metadata (Dynamic Paths)

```bash
# Always calculate dynamically, never hardcode
SCRIPT_NAME="$(basename "$0")"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Benefits:
# - Works when called from any directory
# - Works with symlinks
# - Portable across systems
```

### 8. Argument Parsing Pattern

```bash
parse_args() {
    while [ $# -gt 0 ]; do
        case "$1" in
            -h|--help)
                usage
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
```

---

## Common Pitfalls and Solutions

### Pitfall 1: Using sed -i on macOS

**Problem:**
```bash
sed -i 's/foo/bar/g' file.txt  # Fails on macOS (requires -i '')
```

**Solution:**
```bash
# Use perl instead - works everywhere
perl -i -pe 's/foo/bar/g' file.txt
```

### Pitfall 2: Hardcoded Paths

**Problem:**
```bash
LOG_DIR="/tmp/ADT/.mywork/build-logs"  # Breaks if script moves
```

**Solution:**
```bash
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${BASE_DIR}/.mywork/build-logs"
```

### Pitfall 3: No Error Checking

**Problem:**
```bash
mkdir "$LOG_DIR"
cd "$LOG_DIR"  # Might fail if mkdir failed
```

**Solution:**
```bash
mkdir -p "$LOG_DIR" || die "Could not create: $LOG_DIR"
cd "$LOG_DIR" || die "Could not change to: $LOG_DIR"
```

### Pitfall 4: Global Variables in Functions

**Problem:**
```bash
count_warnings() {
    WARNING_COUNT=$(grep -c 'WARNING' "$1")  # Global
}
```

**Solution:**
```bash
count_warnings() {
    local log_file="$1"
    local count
    
    count=$(grep -c 'WARNING' "$log_file" 2>/dev/null || echo "0")
    count=$(echo "$count" | tr -d '[:space:]')
    count=${count:-0}
    
    echo "$count"  # Return via stdout
}

# Usage:
warnings=$(count_warnings "$LOG_FILE")
```

### Pitfall 5: Not Using set -o pipefail

**Problem:**
```bash
#!/bin/bash
make html | tee log.txt
# If 'make' fails but 'tee' succeeds, script returns 0
```

**Solution:**
```bash
#!/bin/bash
set -o pipefail

make html | tee log.txt
# Now script returns failure if 'make' fails
```

---

## Cross-Platform Considerations

### Git Bash / MINGW Specific

1. **Line endings:** Always convert CRLF → LF
2. **sed behavior:** Use `perl` instead of `sed` for reliability
3. **Paths:** Use forward slashes `/` (work on Windows too)
4. **Buffering:** More aggressive than Linux - avoid processing in pipes

### macOS (BSD) Specific

1. **sed -i:** Requires `-i ''` on macOS vs `-i` on Linux
2. **date format:** Some formats differ from GNU date
3. **readlink:** Use `readlink -f` alternative or calculate manually

### Universal Approach

Use tools that work identically everywhere:
- ✅ `perl` - Same everywhere
- ✅ `awk` - POSIX standard
- ✅ `grep` - POSIX standard
- ❌ `sed -i` - Platform-specific
- ❌ `readlink -f` - Not on macOS

---

## Testing Checklist

Before deploying a script, test on:

- [ ] Linux (Ubuntu/Debian)
- [ ] macOS (if applicable)
- [ ] Git Bash on Windows (if applicable)

Test scenarios:
- [ ] Run from different directories
- [ ] Run with `-v` (verbose)
- [ ] Run with `-n` (dry-run)
- [ ] Interrupt with Ctrl+C (cleanup?)
- [ ] Run with invalid arguments
- [ ] Run when log directory doesn't exist
- [ ] Check log file is clean (no ANSI codes)
- [ ] Check line endings (should be LF)

---

## Performance Considerations

### Buffering Trade-offs

**Real-time processing (slow but interactive):**
```bash
# User sees output immediately but script is slower
make html 2>&1 | tee "$LOG_FILE"
```

**Batch processing (fast but delayed):**
```bash
# Faster but user sees nothing until complete
make html > "$LOG_FILE" 2>&1
```

**Recommended:** Use tee for interactive scripts, redirect for batch jobs.

### Function Call Overhead

Minimize function calls in tight loops:

```bash
# BAD - Calls function 10000 times
for i in {1..10000}; do
    log "Processing $i"
done

# GOOD - Batch process
{
    for i in {1..10000}; do
        echo "Processing $i"
    done
} | tee -a "$LOG_FILE"
```

---

## Real-World Examples

### Example 1: Build Script with Timer

```bash
run_build() {
    local build_start
    local build_end
    local build_duration
    
    banner "STARTING BUILD"
    
    build_start=$(date +%s)
    
    make html 2>&1 | tee "$LOG_FILE"
    local build_exit=${PIPESTATUS[0]}
    
    build_end=$(date +%s)
    build_duration=$((build_end - build_start))
    
    perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$LOG_FILE"
    
    log "Build time: ${build_duration}s"
    
    return $build_exit
}
```

### Example 2: Clean Log Analysis

```bash
count_pattern() {
    local log_file="$1"
    local pattern="$2"
    local count
    
    count=$(grep -c "$pattern" "$log_file" 2>/dev/null || echo "0")
    count=$(echo "$count" | tr -d '[:space:]')
    count=${count:-0}
    
    echo "$count"
}

analyze_log() {
    local warning_count
    local error_count
    
    warning_count=$(count_pattern "$LOG_FILE" "WARNING:")
    error_count=$(count_pattern "$LOG_FILE" "ERROR:")
    
    log "WARNING:  $warning_count"
    log "ERROR:    $error_count"
}
```

### Example 3: Make Clean Before Build

```bash
clean_build() {
    banner "CLEANING BUILD DIRECTORY"
    
    cd "$BASE_DIR" || die "Could not change to: $BASE_DIR"
    
    if [ "$DRY_RUN" -eq 1 ]; then
        log "[DRY-RUN] Would execute: make clean"
        return 0
    fi
    
    make clean 2>&1
    local clean_exit=$?
    
    if [ $clean_exit -eq 0 ]; then
        log "[OK] Clean completed"
    else
        log "[WARN] Clean failed with exit code: $clean_exit"
    fi
    
    return $clean_exit
}
```

---

## Version History

**v1.0.0** (2026-01-31)
- Initial skill creation
- Core patterns from build_and_analyze.sh development
- Cross-platform ANSI code handling
- Buffering solutions
- Functional programming patterns

---

## References

- [Bash Manual](https://www.gnu.org/software/bash/manual/)
- [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html)
- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/)
- Perl one-liners: https://perl.plover.com/FAQs/Buffering.html
- stdbuf usage: https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/

---

## Related Skills

- `incremental-correction-methodology` - Iterative development approach used to create this skill
- `sphinx-expert` - Context for Sphinx build automation

---

## Quick Reference Card

```bash
# ANSI code removal
perl -i -pe 's/\e\[[0-9;]*[a-zA-Z]//g; s/\r$//' "$file"

# Capture pipeline exit code
command | tee file
exit_code=${PIPESTATUS[0]}

# Dynamic script paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Sortable timestamp
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# Pure function template
func_name() {
    local arg1="$1"
    local result
    
    # processing
    
    echo "$result"
    return 0
}

# Error handling
command || die "Failed to run command"

# Separator functions
sep()  { printf '=%.0s' {1..60}; echo; }
hsep() { printf -- '-%.0s' {1..60}; echo; }
```
