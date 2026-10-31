"""
RECORD CHECK  -  my version
===========================

Name  : Zaydan Khan
Lane  : AI
Date  : 31/10/2026

Run it:   python template.py
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Excellent : add over_limit_count as a class-level running total.


class Record:
    """Stores information about a dataset."""

    def __init__(self, label, value, limit):
        """Stores the dataset details as attributes."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns OVER LIMIT, WARNING or OK based on the percentage."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Excellent : write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects.

def load_records(path):
    """Reads records from a file and returns a list of Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = Record(label, float(value), float(limit))
            records.append(record)

    return records


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Excellent : keep a running count of how many came back OVER LIMIT
#                and print it once, after the loop.

over_limit_count = 0

for record in load_records("records_sample.txt"):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print(f"Label : {record.label}")
    print(f"Value : {record.value}")
    print(f"Limit : {record.limit}")

    result = record.status()
    print(f"Status : {result}")

    if result == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)

print()
print("=" * 34)
print("FINAL SUMMARY")
print(f"Total OVER LIMIT : {over_limit_count}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers by hand
#    [x] Check every method only reads/changes its OWN object (self)
#    [x] Check every method and __init__ has a one-line docstring
