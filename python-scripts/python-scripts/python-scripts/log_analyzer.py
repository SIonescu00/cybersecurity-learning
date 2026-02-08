# Simple Log Analyzer

log_file = "sample.log"

keywords = ["FAILED", "ERROR", "WARNING"]

try:
    with open(log_file, "r") as f:
        for line in f:
            if any(word in line for word in keywords):
                print(line.strip())
except FileNotFoundError:
    print(f"{log_file} not found. Please add a log file to analyze.")
