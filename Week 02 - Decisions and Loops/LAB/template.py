over_limit_count = 0

while True:

    label = input("Enter dataset name (or quit): ")

    if label == "quit":
        break

    value = float(input("Enter rows loaded: "))

    limit = float(input("Enter rows expected: "))

    # ==================================================================

    # 2. difference and the percentage.

    difference = value - limit
    percent = (value / limit) * 100

    # 3. Decide a status

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ===================================================================

    # 4. the report.

    print()

    print("=" * 34)

    print(f"  RECORD CHECK - {label}")

    print("=" * 34)

    print(f"Rows loaded   : {value:>10.2f}")
    print(f"Rows expected : {limit:>10.2f}")
    print(f"Difference    : {difference:>10.2f}")
    print(f"Percent       : {percent:>10.2f}%")
    print(f"Status        : {status}")

    print("=" * 34)


print(f"OVER LIMIT records: {over_limit_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
