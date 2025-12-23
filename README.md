# Log File Analyzer

A simple command-line tool that analyzes structured log files and produces a summary of log activity.

This project was built to practice writing clean, user-facing Python utilities with proper error handling, input validation, and repository hygiene.

---

## Features

- Parses log files line-by-line
- Counts INFO, WARN, and ERROR entries, with support for configurable log levels
- Provides a clear summary of log activity
- Handles missing or inaccessible files gracefully
- Designed for clarity and extensibility
- Optional JSON output

---

## Example Log Format

INFO Application started
WARN Configuration file missing
ERROR Failed to connect to database
INFO Retrying connection

---

## Usage

From the project root:

```bash
python3 src/main.py data/sample.log
```

---

## Output

Log Summary
-----------
TOTAL: 4
INFO: 2
WARN: 1
ERROR: 1

## Project Structure

.
├── src/

│   └── main.py

├── data/

│   └── sample.log

├── .gitignore

└── README.md
