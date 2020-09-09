# Chapter 5 練習問題解答例

## Q 1

```python
def ignorecase(s1, s2):
    return s1.lower() == s2.lower()
    # return s1.upper() == s2.upper() でも OK
```


## Q 2

split メソッドに `@` を指定することで，`@` の前部分と後ろ部分に分けることができます．  

```python
def make_userid(email):
    return email.split("@")[0]
```


## Q 3

```python
def sum_and_avg(x):
    t = 0
    for n in x:
        t += n
    return t, t / len(x)    # tuple で返す
```


## Q 4

```python
def calc_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
```


## Q 5

```python
REPORT_NAME = "monthly_report_{}.txt"
MONTH_PREFIXES = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def make_report_name(month):
    if not (1 <= month <= 12):
        raise ValueError("Invalid Argument: month must be 1 <= month <= 12.")
    return REPORT_NAME.format(MONTH_PREFIXES[month - 1])
```


## Q 6

```python
PRICES = {
    "x_attack": 500,
    "defender": 550,
    "x_speed": 350,
    "x_special": 350,
    "x_sp_def": 350,
    "x_accuracy": 950,
}


def calc_total(cart):
    t = 0
    for k, v in cart.items():
        t += PRICES[k] * v
    return t
```


## Q 7

```python
def sort_by_indices(x, indices=None):   # デフォルト引数を使う
    if indices is None:
        x.sort()
        return

    if len(x) != len(indices):
        raise ValueError(
            "Invalid Argument: the length of indices must be the same with the length of x.")

    x_copy = x.copy()   # ソートの途中で x の要素の順番が変わっていくのでソート前の list をもっておく
    for i, idx in enumerate(indices):
        x[i] = x_copy[idx]  # indices の要素 idx (= x のインデックス) にある x の要素を i = 0 (= x の先頭) から順に代入
```


## Q 8

```python
def perm(n):
    if n < 0:
        raise ValueError("Invalid Argument: n must be n >= 0.")

    if n == 0:
        return 1

    for i in range(n - 1, 1, -1):
        n *= i
    return n
```

## Q 9

```python
def perm(n):
    if n < 0:
        raise ValueError("Invalid Argument: n must be n >= 0.")

    if n == 0:
        return 1

    for i in range(n - 1, 1, -1):
        n *= i
    return n


def perm_with_dup(*args):
    n = 0
    t = 1
    for p in args:
        if p <= 0:
            raise ValueError("Invalid Argument: all args must be arg > 0.")
        n += p            # n を計算 (p1 + p2 + ... + pm)
        t *= perm(p)      # 分子の階乗を計算してすべて乗算する (p1! * p2! * ... * pm!)

    return perm(n) // t     # n! // (p1! * p2! * ... * pm!)
```

# Q 10

```python
schedules = [
    {
        "start": 8,
        "end": 9,
        "room": "meeting_room_A",
        "num": 10
    },
    {
        "start": 12,
        "end": 14,
        "room": "meeting_room_A",
        "num": 12
    },
    {
        "start": 13,
        "end": 14,
        "room": "meeting_room_B",
        "num": 5
    },
    {
        "start": 18,
        "end": 19,
        "room": "meeting_room_A",
        "num": 5
    },
    {
        "start": 19,
        "end": 20,
        "room": "meeting_room_B",
        "num": 7
    },
]


def book(start, end, room, num):
    global schedulesS   # グローバル変数を更新するので `global` で明示

    booked = [False] * 24   # 1 時間ごとの予約状況を保持する list
    for schedule in schedules:
        if schedule["room"] == room:
            s = schedule["start"]
            e = schedule["end"]
            booked[s:e] = [True] * (e - s)  # 予約してある時間を True で埋める
    if booked[start:end] == [False] * (end - start):    # 予約した時間がすべて予約されていないか？
        schedules.append(
            {
                "start": start,
                "end": end,
                "room": room,
                "num": num
            }
        )
        return True
    else:
        return False
```
