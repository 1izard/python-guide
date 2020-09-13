from pathlib import Path
import shutil
import json
import random


random.seed(0)


weathers = [
    {
        "date": "2020-08-02",
        "weather": "sunny",
        "max_temp": 31.5,
        "min_temp": 22.6
    },
    {
        "date": "2020-08-03",
        "weather": "sunny",
        "max_temp": 32.3,
        "min_temp": 22.3
    },
    {
        "date": "2020-08-04",
        "weather": "sunny",
        "max_temp": 33.1,
        "min_temp": 24.5
    },
    {
        "date": "2020-08-05",
        "weather": "sunny",
        "max_temp": 34.2,
        "min_temp": 25.7
    },
    {
        "date": "2020-08-06",
        "weather": "sunny",
        "max_temp": 33.1,
        "min_temp": 25.5
    },
    {
        "date": "2020-08-07",
        "weather": "cloudy",
        "max_temp": 35.4,
        "min_temp": 26
    },
    {
        "date": "2020-08-08",
        "weather": "cloudy",
        "max_temp": 32.3,
        "min_temp": 26
    }
]

prices = {
    "モンスターボール": 200,
    "スーパーボール": 600,
    "ハイパーボール": 1200,
    "リピートボール": 1000,
    "タイマーボール": 1000,
}
price_dcts = [{"item_name": k, "unit_price": v} for k, v in prices.items()]
balls = list(prices.keys())
items = [balls[random.randint(0, len(balls) - 1)] + "\n" for _ in range(20)]

packages = [
    "autopep8==1.5.4\n",
    "flake8==3.8.3\n",
    "mccabe==0.6.1\n",
    "pycodestyle==2.6.0\n",
    "pyflakes==2.2.0\n",
    "toml==0.10.1\n",
]

numbers = list(range(1, 31))
random.shuffle(numbers)
images = [f"image{i:02d}.png\n" for i in numbers]

wanted = [
    "dir2_5_1/data2_5_1_01.png\n",
    "dir2_5_1/data2_5_1_04.png\n",
    "dir2_5_1/data2_5_1_07.png\n",
    "dir2_5_2/data2_5_2_05.png\n",
    "dir2_5_3/data2_5_3_09.png\n",
    "dir2_5_3/data2_5_3_10.png\n",
    "dir2_5_4/data2_5_4_02.png\n",
    "dir2_5_4/data2_5_4_03.png\n",
    "dir2_5_5/data2_5_5_06.png\n",
    "dir2_5_5/data2_5_5_10.png\n",
]

dist = {f"data{i:02d}.png": f"dir2_6_{random.randint(1, 3)}" for i in range(1, 11)}


dir2 = Path(__file__).parent / "dir2"
if dir2.is_dir():
    shutil.rmtree(str(dir2))
dir2.mkdir()
(dir2 / "file2_1.txt").touch()
(dir2 / "file2_2.csv").touch()
with open(dir2 / "file2_3.json", "w") as f:
    json.dump(weathers, f)

dir2_1 = dir2 / "dir2_1"
dir2_1.mkdir()
(dir2_1 / "example.py").touch()
(dir2_1 / "file2_1_1.txt").touch()
(dir2_1 / "file2_1_2.json").touch()
dir2_1_1 = dir2_1 / "dir2_1_1"
dir2_1_1.mkdir()
for i in range(1, 4):
    (dir2_1_1 / f"file2_1_1_{i:02d}.txt").touch()
(dir2_1_1 / "file2_1_1_04.md").touch()
dir2_1_2 = dir2_1 / "dir2_1_2"
dir2_1_2.mkdir()
(dir2_1_2 / "file2_1_2_01txt").touch()
(dir2_1_2 / "file2_1_2_02.txt").touch()


dir2_2 = dir2 / "dir2_2"
dir2_2.mkdir()
with open(dir2_2 / "file2_2_1.json", "w") as f:
    json.dump(price_dcts, f, ensure_ascii=False)
with open(dir2_2 / "file2_2_2.txt", "w") as f:
    f.writelines(items)
with open(dir2_2 / "requirements.txt", "w") as f:
    f.writelines(packages)
dir2_2_1 = dir2_2 / "dir2_2_1"
dir2_2_1.mkdir()
for i in range(1, 4):
    with open(dir2_2_1 / f"file2_2_1_{i:02d}.txt", "w") as f:
        f.writelines(images[(i - 1) * 10:(i - 1) * 10 + 10])

dir2_3 = dir2 / "dir2_3"
dir2_3.mkdir()
dir2_3_1 = dir2_3 / "dir2_3_1"
dir2_3_1.mkdir()
for i in range(1, 4):
    d = dir2_3_1 / f"dir2_3_1_{i}"
    d.mkdir()
    for j in range(1, 6):
        (d / f"file2_3_1_{i}_{j:02d}.txt").touch()

dir2_4 = dir2 / "dir2_4"
dir2_4.mkdir()
for i in range(1, 11):
    (dir2_4 / f"data2_4_{numbers[i]:02d}.png").touch()

dir2_5 = dir2 / "dir2_5"
dir2_5.mkdir()
work = dir2_5 / "work"
work.mkdir()
with open(work / "wanted.txt", "w") as f:
    f.writelines(wanted)
for i in range(1, 6):
    d = dir2_5 / f"dir2_5_{i}"
    d.mkdir()
    for j in range(1, 11):
        (d / f"data2_5_{i}_{j:02d}.png").touch()

dir2_6 = dir2 / "dir2_6"
dir2_6.mkdir()
for i in range(1, 4):
    (dir2_6 / f"dir2_6_{i}").mkdir()
work = dir2_6 / "work"
work.mkdir()
with open(work / "dist.json", "w") as f:
    json.dump(dist, f)
for i in range(1, 11):
    (work / f"data{i:02d}.png").touch()
