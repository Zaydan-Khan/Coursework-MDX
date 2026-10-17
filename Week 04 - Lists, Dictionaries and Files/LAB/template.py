
"""
RECORD CHECK - AI / Data Science version
========================================
Name  :
Lane  : AI / Data Science
Date  :
"""

# =========================================================
# 1. FUNCTIONS


def check_record(value, limit):
    """Calculate the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100 if limit != 0 else 0

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one dataset."""
    print(f"Dataset: {label}")
    print(f"Rows loaded: {value}")
    print(f"Rows expected: {limit}")
    print(f"Difference: {difference} rows")
    print(f"Completion: {percent:.2f}%")
    print(f"Status: {status}")
    print("-" * 30)


def load_records(path):
    """Load dataset records from a file into a list of dictionaries."""
    records = []

    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


# =========================================================
# 2. STORE

try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("File not found: records.txt")
    records = []


# =========================================================
# 3. PROCESS + OUTPUT

over_limit_count = 0

with open("results.txt", "w") as output_file:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        output_file.write(f'{record["label"]},{status}\n')

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"Total datasets over limit: {over_limit_count}")
print("Results saved to results.txt")
