from collections import Counter
import re
import sys

FAILED_LOGIN = re.compile(r"failed login", re.IGNORECASE)
IP = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

def analyze(path):
    failed = 0
    ips = Counter()

    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            if FAILED_LOGIN.search(line):
                failed += 1
            match = IP.search(line)
            if match:
                ips[match.group()] += 1

    print(f"Failed login events: {failed}")
    print("Top IP addresses:")
    for ip, count in ips.most_common(5):
        print(f"  {ip}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <log-file>")
        sys.exit(1)
    analyze(sys.argv[1])
