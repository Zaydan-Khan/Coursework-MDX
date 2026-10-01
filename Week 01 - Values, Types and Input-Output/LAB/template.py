dataset_name = input("Enter the dataset name: ")
rows_loaded = float(input("Enter the number of rows loaded: "))
rows_expected = float(input("Enter the number of rows expected: "))

difference = rows_loaded - rows_expected
percent = (rows_loaded/rows_expected) * 100

print("=" * 30)
print(f"Dataset   : {dataset_name}")
print("=" * 30)
print(f"Used      : {rows_loaded:>15.2f}")
print(f"Expected  : {rows_expected:>15.2f}")
print(f"Difference: {difference:>+15.2f}")
print(f"Percent   : {percent:>15.2f}%")
print("=" * 30)


