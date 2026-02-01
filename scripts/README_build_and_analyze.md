# Build and Analyze Script Documentation

Version: 1.0.0
Date: 2026-01-31
Location: /tmp/ADT/scripts/build_and_analyze.sh

---

## Overview

This script builds Sphinx documentation and analyzes warnings, errors, and critical issues.

## Features

- Real-time colored output in terminal
- Clean log file without ANSI escape codes
- Automatic counting of issues
- Timestamped log files for history
- Intelligent pipeline processing

---

## How It Works

### Pipeline Breakdown

```bash
make html 2>&1 | \
    tee >(sed 's/\x1B\[[0-9;]*[JKmsu]//g' > "$LOG_FILE") | \
    grep --line-buffered --color=always -E "WARNING:|ERROR:|CRITICAL:|$"
```

**Step 1:** `make html 2>&1`
- Executes Sphinx build
- Redirects stderr to stdout

**Step 2:** `tee >(...)`
- Duplicates output stream
- Sends one copy to file (cleaned)
- Sends one copy to next command (for terminal display)

**Step 3:** `sed 's/\x1B\[[0-9;]*[JKmsu]//g'`
- Removes ANSI escape codes
- Creates clean, readable log file

**Step 4:** `grep --line-buffered --color=always`
- Highlights issues in terminal
- Shows all output (not just matches)
- Line-buffered for real-time display

---

## Usage

### Basic Usage

```bash
cd /tmp/ADT
./scripts/build_and_analyze.sh
```

### What You'll See

**During Build:**
- Full Sphinx output with colored highlights
- WARNING/ERROR/CRITICAL lines stand out

**After Build:**
```
============================================================
BUILD SUMMARY
============================================================
WARNING:  3
ERROR:    0
CRITICAL: 0
------------------------------------------------------------
TOTAL:    3
============================================================

Log file: /tmp/ADT/.mywork/build-logs/build-fase1-20260131-213045.txt

Last 20 lines of log:
------------------------------------------------------------
[last 20 lines of clean log here]
------------------------------------------------------------

Build completed successfully
```

---

## Output Files

### Log File Location

```
/tmp/ADT/.mywork/build-logs/build-fase1-YYYYMMDD-HHMMSS.txt
```

**Characteristics:**
- Timestamped filename
- Clean text (no ANSI codes)
- Complete build output
- Easily readable in any text editor

### Log File Content

The log file contains:
- All Sphinx build messages
- Progress information
- Warnings and errors
- Build statistics

**Crucially:** No ANSI escape codes, making it readable in:
- Text editors (vim, nano, VSCode, etc.)
- Less/more pagers
- Grep/sed/awk tools
- Log analyzers

---

## Exit Codes

- `0` = Build successful
- `1` = Build failed or error in script
- Other = Specific Sphinx error codes

---

## Examples

### Example 1: Successful Build with Warnings

**Terminal Output:**
```
============================================================
Starting Sphinx build...
============================================================
Base directory: /tmp/ADT
Log file: /tmp/ADT/.mywork/build-logs/build-fase1-20260131-213045.txt
Timestamp: 20260131-213045
============================================================

Running Sphinx...
WARNING: document isn't included in any toctree    (in yellow)
WARNING: duplicate label found                     (in yellow)
Building... done

============================================================
BUILD SUMMARY
============================================================
WARNING:  2
ERROR:    0
CRITICAL: 0
------------------------------------------------------------
TOTAL:    2
============================================================

Build completed successfully
```

### Example 2: Build with Errors

**Terminal Output:**
```
Running Sphinx...
ERROR: Unknown directive type "code-block"         (in red)
WARNING: duplicate label found                     (in yellow)
Build failed

============================================================
BUILD SUMMARY
============================================================
WARNING:  1
ERROR:    1
CRITICAL: 0
------------------------------------------------------------
TOTAL:    2
============================================================

Build failed with exit code: 1
```

---

## Configuration

### Modifiable Variables

Located at the top of the script:

```bash
BASE_DIR="/tmp/ADT"                  # Project directory
LOG_DIR="${BASE_DIR}/.mywork/build-logs"  # Log storage
TIMESTAMP=$(date +%Y%m%d-%H%M%S)     # Timestamp format
LOG_FILE="${LOG_DIR}/build-fase1-${TIMESTAMP}.txt"  # Log filename
```

### Customization Options

**Change timestamp format:**
```bash
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)  # Use dashes and underscores
```

**Change log filename pattern:**
```bash
LOG_FILE="${LOG_DIR}/sphinx-build-${TIMESTAMP}.log"
```

**Change log directory:**
```bash
LOG_DIR="${BASE_DIR}/logs"
```

---

## Troubleshooting

### Problem: "ERROR: Base directory does not exist"

**Cause:** BASE_DIR is not set correctly

**Solution:**
```bash
# Edit script and verify BASE_DIR
vim /tmp/ADT/scripts/build_and_analyze.sh
# Change BASE_DIR to correct path
```

### Problem: "Permission denied"

**Cause:** Script is not executable

**Solution:**
```bash
chmod +x /tmp/ADT/scripts/build_and_analyze.sh
```

### Problem: "make: *** No rule to make target 'html'"

**Cause:** Not in a Sphinx project directory

**Solution:**
```bash
# Verify you're in the right directory
cd /tmp/ADT
# Verify Makefile exists
ls -la Makefile
```

### Problem: Log file has ANSI codes anyway

**Cause:** sed pattern might not match all ANSI sequences

**Solution:**
```bash
# Try more comprehensive pattern
sed 's/\x1B\[[0-9;]*m//g'  # Simpler pattern
# Or
perl -pe 's/\e\[[0-9;]*m//g'  # Use perl instead
```

---

## Advanced Usage

### Run with Custom Log Name

```bash
# Modify TIMESTAMP before running
CUSTOM_NAME="migration-test" ./scripts/build_and_analyze.sh
```

### Pipe Output to Another Command

```bash
./scripts/build_and_analyze.sh | tee additional-log.txt
```

### Run and Email Results

```bash
./scripts/build_and_analyze.sh 2>&1 | mail -s "Build Report" user@example.com
```

---

## Technical Details

### ANSI Code Removal Pattern

The pattern `\x1B\[[0-9;]*[JKmsu]` matches:
- `\x1B` or `\e` = ESC character
- `[` = Literal bracket
- `[0-9;]*` = Zero or more digits or semicolons
- `[JKmsu]` = Final character (cursor movement, erase, color)

**Examples matched:**
- `[2K` = Clear line
- `[01m` = Bold
- `[32m` = Green color
- `[39;49;00m` = Reset color

### Pipeline Error Handling

The script uses `set -o pipefail` to catch errors in any part of the pipeline.

```bash
set -o pipefail
make html 2>&1 | tee ... | grep ...
BUILD_EXIT=${PIPESTATUS[0]}  # Get exit code of 'make html'
```

This ensures that if `make html` fails, the script exits with that error code.

---

## Files Created

For each run, the script creates:

1. **Log file**: `build-fase1-YYYYMMDD-HHMMSS.txt`
   - Clean, readable text
   - Complete build output
   - No ANSI codes

2. **(Temporary)** Process substitution file
   - Created automatically by bash
   - Cleaned up automatically
   - Not visible to user

---

## Performance

**Typical execution time:** 2-5 minutes (depends on project size)

**Memory usage:** Minimal (streaming processing)

**Disk usage:** Approximately 100KB-500KB per log file

---

## Maintenance

### Cleaning Old Logs

```bash
# Remove logs older than 30 days
find /tmp/ADT/.mywork/build-logs -name "build-fase1-*.txt" -mtime +30 -delete

# Keep only last 10 logs
cd /tmp/ADT/.mywork/build-logs
ls -t build-fase1-*.txt | tail -n +11 | xargs rm -f
```

### Archiving Logs

```bash
# Compress old logs
gzip /tmp/ADT/.mywork/build-logs/build-fase1-2026*.txt

# Create monthly archive
tar czf logs-2026-01.tar.gz build-fase1-202601*.txt
```

---

## Version History

**v1.0.0** (2026-01-31)
- Initial release
- Intelligent pipeline with clean log output
- Real-time colored terminal display
- Automatic issue counting
- No emojis or icons (professional output)

---

End of documentation
