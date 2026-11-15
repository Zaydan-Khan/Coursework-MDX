
"""
  RECORD CHECK - my version
  =========================

  Name  :
  Lane  : AI / Data Science
  Date  :

  Run it:   python template.py
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.


def parse_line(raw_line):
    """Clean and parse one survey record into a dictionary."""
    cleaned = raw_line.strip().lower()

    parts = cleaned.split(",")

    survey = parts[0].strip()

    record = {"survey": survey}

    for item in parts[1:]:
        key, value = item.split("=")
        record[key.strip()] = float(value.strip())

    return record


def status_of(rating):
    """Return FLAGGED or OK based on the survey rating."""
    if rating < 3:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []

with open("messy_records.txt") as f:
    for line in f:
        raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many were flagged.

total_records = 0
flagged_records = 0

for raw_record in raw_records:
    record = parse_line(raw_record)

    status = status_of(record["rating"])

    print(record, status)

    total_records += 1

    if status == "FLAGGED":
        flagged_records += 1

print(f"\nTotal records: {total_records}")
print(f"Flagged records: {flagged_records}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring

# Testing an invalid value:
# parse_line("Survey_2026,rating=unknown,age=23")
#
# Expected error:
# ValueError: could not convert string to float: 'unknown'
