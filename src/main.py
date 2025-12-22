import sys

if len(sys.argv) < 2:
    print("Usage: python3 src/main.py <path_to_log_file>")
    sys.exit(1)

log_path = sys.argv[1]


def analyze_log(file_path):
    summary = {
        "INFO": 0,
        "WARN": 0,
        "ERROR": 0,
        "TOTAL": 0
    }

    try:
        with open(file_path, "r") as file:
            for line in file:
                summary["TOTAL"] += 1
                for level in ("INFO", "WARN", "ERROR"):
                    if line.startswith(level):
                        summary[level] += 1

        return summary
    except FileNotFoundError:
        print(f"Error: log file not found -> {file_path}")
        sys.exit(1)

    return summary

def print_summary(summary):
    print("Log Summary")
    print("-----------")
    print(f"Total entries: {summary['TOTAL']}")
    print(f"INFO: {summary['INFO']}")
    print(f"WARN: {summary['WARN']}")
    print(f"ERROR: {summary['ERROR']}")


if __name__ == "__main__":
    result = analyze_log(log_path)
    print_summary(result)