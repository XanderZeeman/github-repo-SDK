# Import required modules
import sys
import json

# Define configurable log levels
LOG_LEVELS = ["INFO", "WARN", "ERROR"]

# Ensure correct usage
if len(sys.argv) < 2:
    print("Usage: python3 src/main.py <path_to_log_file>")
    sys.exit(1)

# Parse command-line arguments and verify JSON output option
log_path = sys.argv[1]
output_json = "--json" in sys.argv

# Function to analyze log file
def analyze_log(file_path):
    summary = {level: 0 for level in LOG_LEVELS}
    summary["TOTAL"] = 0

    # Read and process the log file
    try:
        with open(file_path, "r") as file:
            for line in file:
                summary["TOTAL"] += 1
                for level in LOG_LEVELS:
                    if line.startswith(level):
                        summary[level] += 1

        return summary
    
    # Handle file-related errors
    except FileNotFoundError:
        print(f"Error: File not found → {file_path}")
        sys.exit(1)

    except PermissionError:
        print(f"Error: Permission denied → {file_path}")
        sys.exit(1)

    return summary

# Function to print summary in JSON format
def print_summary_json(summary):
    print(json.dumps(summary, indent=2))

# Function to print summary in plain text format
def print_summary(summary):
    print("Log Summary")
    print("-----------")
    # Print counts for each log level
    for level in LOG_LEVELS:
        print(f"{level}: {summary[level]}")
    print("-----------")    
    print(f"TOTAL: {summary['TOTAL']}")

# Main execution function
def main():
    result = analyze_log(log_path)

    # Output the summary in the requested formatS
    if output_json:
        print_summary_json(result)
    else:
       print_summary(result)

if __name__ == "__main__":
    main()