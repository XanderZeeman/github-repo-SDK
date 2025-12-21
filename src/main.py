def analyze_log(file_path):
    summary = {
        "INFO": 0,
        "WARN": 0,
        "ERROR": 0,
        "TOTAL": 0
    }

    with open(file_path, "r") as file:
        for line in file:
            summary["TOTAL"] += 1
            for level in ("INFO", "WARN", "ERROR"):
                if line.startswith(level):
                    summary[level] += 1
                    
    return summary

def print_summary(summary):
    print("Log Summary")
    print("-----------")
    print(f"Total entries: {summary['TOTAL']}")
    print(f"INFO: {summary['INFO']}")
    print(f"WARN: {summary['WARN']}")
    print(f"ERROR: {summary['ERROR']}")


if __name__ == "__main__":
    log_file = "data/sample.log"
    result = analyze_log(log_file)
    print_summary(result)