from pathlib import Path
import random


random.seed(0)


N = 400 * 3


category_ratio = {
    "food": 0.3,
    "utility": 0.1,
    "transport":  0.1,
    "hobby": 0.2,
    "socializing": 0.2,
    "daily_miscellaneous": 0.1,
}

expense_ratio = {
    100: 0.6,
    1000: 0.3,
    10000: 0.1,
}

categories = []
for k, v in category_ratio.items():
    categories += [k] * int(N * v)
random.shuffle(categories)

expenses = []
for k, v in expense_ratio.items():
    expenses += [random.randint(1, 9) * k for _ in range(int(N * v))]
random.shuffle(expenses)

dates = [
    f"202{random.randint(0, 2)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}" for _ in range(N)]

lines = sorted([f"{dates[i]},{categories[i]},{expenses[i]}\n" for i in range(N)])
with open(Path("account.csv"), "w") as f:
    f.writelines(lines)
