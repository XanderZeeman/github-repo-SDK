import sys
import json

LOG_LEVELS = ["INFO", "WARN", "ERROR"]

if len(sys.argv) < 2:
    print("Usage: python3 src/main.py <path_to_log_file>")
    sys.exit(1)

log_path = sys.argv[1]
output_json = "--json" in sys.argv



def analyze_log(file_path):
    summary = {level: 0 for level in LOG_LEVELS}
    summary["TOTAL"] = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                summary["TOTAL"] += 1
                for level in LOG_LEVELS:
                    if line.startswith(level):
                        summary[level] += 1

        return summary
    except FileNotFoundError:
        print(f"Error: log file not found -> {file_path}")
        sys.exit(1)

    return summary

def print_summary_json(summary):
    print(json.dumps(summary, indent=2))

def print_summary(summary):
    print("Log Summary")
    print("-----------")
    for level in LOG_LEVELS:
        print(f"{level}: {summary[level]}")
    print("-----------")    
    print(f"TOTAL: {summary['TOTAL']}")


if __name__ == "__main__":
    result = analyze_log(log_path)

if output_json:
    print_summary_json(result)
else:
    print_summary(result)
