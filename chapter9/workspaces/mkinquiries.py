from pathlib import Path
import random


random.seed(0)

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dates = []
for m, day in enumerate(days, 1):
    dates += [f"2020/{m:02d}/{d:02d}" for d in range(1, day + 1)]

dates.sort()

inquiries = [f"{d},{random.randint(0, 1000)}\n" for d in dates]

with open(Path("inquiries.csv"), "w") as f:
    f.writelines(inquiries)
