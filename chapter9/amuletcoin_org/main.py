import sys

from utils import validate_args, max_len
from record import Record, RecordList


def main():
    try:
        src, start, end = validate_args(sys.argv[1:])
    except ValueError:
        print(
            "Error: Invalid Arguments: please run this program like "
            + f"'python {__file__} accounts/account.csv -s 2020-08-24 -e 2020-09-01'"
        )
        return

    if not src.is_file():
        print(f"Error: '{src}' does not exist or is a directory.")
        return

    if src.suffix != ".csv":
        print("Error: Invalid Extension: Only CSV file is available.")
        return

    records = RecordList([])
    with open(src, "r") as f:
        for line in f:
            records.append(Record(*line.strip().split(",")))

    category_total = records.category_total(start, end)
    c_length = max_len(category_total.keys())
    e_length = max_len(category_total.values())
    print(f"{'total':{c_length}s} | {category_total['total']:>{e_length}d}")
    for category, expense in category_total.items():
        if category != "total":
            print(f"{category:{c_length}s} | {expense:>{e_length}d}")


if __name__ == "__main__":
    main()
