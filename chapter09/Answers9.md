# 練習問題 9 解答例


## Q 1

```python
from datetime import datetime, timedelta


from_d = datetime(2020, 8, 10, 10, 0, 0)
to_d = from_d - timedelta(hours=12, minutes=34, seconds=56)
print(to_d)     # 2020-08-09 21:25:04
```


## Q 2

```python
from datetime import datetime


d1 = datetime(2020, 8, 10, 10, 0, 0)
d2 = datetime(2020, 8, 13, 13, 0, 0)

td = d2 - d1
print(f"{td.days}日前")   # 3日前

```


## Q 3

```python
from datetime import datetime


datetimes = [
    datetime.fromisoformat("2022-08-18 10:00:43"),
    datetime.fromisoformat("2020-05-10 23:34:10"),
    datetime.fromisoformat("2021-12-31 12:11:09"),
    datetime.fromisoformat("2020-10-10 10:10:10"),
    datetime.fromisoformat("2022-08-18 10:00:45"),
]

print(f"{min(datetimes)}, {max(datetimes)}")

```


## Q 4

```python
from datetime import date, timedelta


datetimes = [
    date.fromisoformat("2020-08-23"),
    date.fromisoformat("2020-09-02"),
    date.fromisoformat("2020-08-10"),
    date.fromisoformat("2020-08-22"),
    date.fromisoformat("2020-08-18"),
]

today = date.fromisoformat("2020-08-20")

min_td = timedelta(days=30)
ans = None
for dt in datetimes:
    td = dt - today
    if td >= timedelta(days=0) and td < min_td:
        ans = dt
        min_td = td

print(ans)  # 2020-08-22

```


## Q 5

```python
from datetime import datetime


dt_str = "1996/2/27 13'14'39"
dt = datetime.strptime(dt_str, "%Y/%m/%d %H'%M'%S")
print(dt)   # 1996-02-27 13:14:39

```


## Q 6

```python
from datetime import datetime


dt = datetime(1996, 2, 27, 13, 14, 39, 600)
dt_str = dt.strftime("%Y年%m月%d日 %H時%M分%S秒")
print(dt_str)   # 1996年02月27日 13時14分39秒

```


## Q 7

```python
from datetime import date


def mk_filename_with_date(filename):
    name, ext = filename.split(".")
    d_str = date.today().strftime("%Y%m%d")
    return f"{name}_{d_str}.{ext}"


filename = "monthly_report.txt"
filename_with_date = mk_filename_with_date(filename)
print(filename_with_date)   # monthly_report_20200819.txt

filename = "data.json"
filename_with_date = mk_filename_with_date(filename)
print(filename_with_date)   # data_20200819.json

```


## Q 8

```python
from datetime import datetime, timedelta
from pprint import pprint


class Event:
    def __init__(self, title, datetime):
        self.title = title
        self.datetime = datetime

    def __repr__(self):
        return f"Event(title={self.title}, datetime={self.datetime})"


events = []

title = "Daily MTG"
first_dt = datetime(2022, 8, 10, 10, 00, 00)
for i in range(5):
    dt = first_dt + timedelta(weeks=i)
    events.append(Event(title, dt))

pprint(events)
"""
[Event(title=Daily MTG, datetime=2022-08-10 10:00:00),
 Event(title=Daily MTG, datetime=2022-08-17 10:00:00),
 Event(title=Daily MTG, datetime=2022-08-24 10:00:00),
 Event(title=Daily MTG, datetime=2022-08-31 10:00:00),
 Event(title=Daily MTG, datetime=2022-09-07 10:00:00)]
"""

```


## Q 9

`task.deadline - today` で両日の差を計算し，7 日以上であれば stacked，0 日以上 7 日未満であれば approching，それ以外であれば over の list に追加します．  

```python
from datetime import date
from pprint import pprint


class Task:
    def __init__(self, no, content, created, deadline):
        self.no = no
        self.content = content
        self.created = created
        self.deadline = deadline
        self.finished = False

    def __repr__(self):
        return f"Task(no={self.no})"

    def done(self):
        self.finished = True


tasks = [
    Task(1, "Send a pull Requiest", date(2020, 8, 30), date(2020, 9, 2)),
    Task(2, "Open a new issue", date(2020, 8, 1), date(2020, 8, 7)),
    Task(3, "Fix bug", date(2020, 8, 13), date(2020, 8, 25)),
    Task(4, "Review a Pull Request", date(2020, 8, 15), date(2020, 8, 20)),
    Task(5, "Close a resolved issue", date(2020, 8, 12), date(2020, 8, 17)),
    Task(6, "Send a pull Requiest", date(2020, 8, 10), date(2020, 8, 22)),
]

tasks[4].done()


today = date(2020, 8, 16)

grouped_tasks = {
    "stacked": [],
    "approching": [],
    "over": [],
    "finished": [],
}

for task in tasks:
    if task.finished:
        grouped_tasks["finished"].append(task)
        continue

    td = task.deadline - today
    if 7 <= td.days:
        grouped_tasks["stacked"].append(task)
    elif 0 <= td.days < 7:
        grouped_tasks["approching"].append(task)
    else:
        grouped_tasks["over"].append(task)

pprint(grouped_tasks)

```


## Q 10

コマンドライン引数の西暦，開始月，終了月は `sys.argv[1:]` に格納されているので，取り出して int 型に直します．  
開始月 start_month，終了月 end_month が 1 以上 12 以下でないときはエラーメッセージを出力して `sys.exit()` でプログラムをすぐに終了します．  

inquiries.csv はカンマ区切りなので，`line.strip()` で改行コードを除去したあと `split(",")` で日付と問い合わせ件数に分割します．  
そのあと，`datetime.strptime(d, "%Y/%m/%d").date()` で文字列から date オブジェクトにし，month 属性と start_month，end_month を比較して集計期間であれば問い合わせ件数の合計 num に加算します．  

```python
import sys
from pathlib import Path
from datetime import date, datetime


year = int(sys.argv[1])
start_month = int(sys.argv[2])
end_month = int(sys.argv[3])

if not (1 <= start_month <= 12 and 1 <= end_month <= 12):
    print("Error: start month and end month must be in 1..12.")
    sys.exit()

num = 0
src = Path("inquiries.csv")
with open(src, "r") as f:
    for line in f:
        d, n = line.strip().split(",")
        if start_month <= datetime.strptime(d, "%Y/%m/%d").date().month <= end_month:
            num += int(n)

print(num)

```



<hr>

[Chapter 9 システム/例外処理/モジュール](Chapter9.md)  
[Index](../README.md)
