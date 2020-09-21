# Chapter 6 組込み関数

Python では，一般的に使用される関数を **組込み関数** (built-in function) として実装し，簡単にその機能を使えるようにしています．  

公式 doc の組込み関数のページ( https://docs.python.org/ja/3/library/functions.html#built-in-funcs ) より，組込み関数の一覧です．  

|             |           | 組込み関数 |            |              |
| :---------: | :-------: | :--------: | :--------: | :----------: |
|     abs     |  delattr  |    hash    | memoryview |     set      |
|     all     |   dict    |    help    |    min     |   setattr    |
|     any     |    dir    |    hex     |    next    |    slice     |
|    ascii    |  divmod   |     id     |   object   |    sorted    |
|     bin     | enumerate |   input    |    oct     | staticmethod |
|    bool     |   eval    |    int     |    open    |     str      |
| breakpoint  |   exec    | isinstance |    ord     |     sum      |
|  bytearray  |  filter   | issubclass |    pow     |    super     |
|    bytes    |   float   |    iter    |   print    |    tuple     |
|  callable   |  format   |    len     |  property  |     type     |
|     chr     | frozenset |    list    |   range    |     vars     |
| classmethod |  getattr  |   locals   |    repr    |     zip      |
|   compile   |  globals  |    map     |  reversed  | `__import__` |
|   complex   |  hasattr  |    max     |   round    |              |

`print()` や `range()` など，これまでいくつかの組込み関数を使ってきました．  
この章では，まだ紹介していない有用な組込み関数をみていきます．  


# abs()

abs 関数は数値の絶対値を返します．  
(Extra) あるいは，`__abs__` メソッドが実装されているクラスのオブジェクトであれば `__abs__` メソッドの結果を返します．(ここまで Extra)

```python
a = -5
b = 5

abs_a = abs(a)          # 5
abs_b = abs(b)          # 5
same = abs_a == abs_b   # True

c = -3.2
within = abs(c) < 5.0   # True
```


# all()

iterable オブジェクトの要素がすべて `True` と判定されるオブジェクトであれば `True`，1 つでも `False` と判定されるオブジェクトがあれば `False` を返す関数です．  
all 関数は， `False` となる要素を見つけたら直ちに `False` を返します．  


```python
b1 = all([True, True, True, True])        # True
b2 = all([True, False, True, True])       # False

i1 = all([1, -1])     # True
i2 = all([1, 0, -1])  # False

f1 = all([3.4, -2.3])         # True
f2 = all([3.4, 0.0, -2.3])    # False

s1 = all(["Oddish", " ", "\n", "\t"])     # True
s2 = all(["Oddish", "", "Vileplume"])     # False
```


# any()

any 関数は，iterable オブジェクトの要素のうち 1 つでも `True` と判定されるオブジェクトがあれば `True`，すべて `False` と判定されるオブジェクトであれば `False` を返す関数です．  
1 つでも `True` の要素が見つかれば，その時点で `True` を返します．  

```python
b1 = any([False, False, False, True])        # True
b2 = any([False, False, False, False])       # False

i1 = any([1, -1, 0])     # True
i2 = any([0, 0, 0])      # False

f1 = any([3.4, -2.3, 0.0])   # True
f2 = any([0.0, 0.0, 0.0])    # False

s1 = any(["", " ", "\n", "\t"])     # True
s2 = any(["", "", "", ""])          # False
```


# min()

min 関数は，複数の値，あるいは iterable オブジェクトを与えるとその中で最小の値を返す関数です．  

```python
a = min(-10, 0, 10)     # -10
b = min([2, -4, 4, 6, 2, 1, 8, 10, 6, 4])   # -4

c = min(-2.5, 0, 2.5)   # -2.5
d = min([1.26, -4.44, 2.24, 2.91, 3.67, -1.81, 1.53, -2.56, 2.81, 4.0])  # -4.44
```


# max()

max 関数は，複数の値，あるいは iterable オブジェクトを与えるとその中で最大の値を返します．  

```python
a = min(-10, 0, 10)     # 10
b = min([2, -4, 4, 6, 2, 1, 8, 10, 6, 4])   # 10

c = min(-2.5, 0, 2.5)   # 2.5
d = min([1.26, -4.44, 2.24, 2.91, 3.67, -1.81, 1.53, -2.56, 2.81, 4.0])  # 4.0
```


# sum()

sum 関数は，iterable オブジェクトを引数として渡すと要素の和を返します．  

```python
s1 = sum([4, -9, -7, -1, 5])    # -8
s2 = sum([1.64, 0.84, 1.18, -3.21, -4.36])  # -3.91
```

(Extra)  

# filter()

filter 関数は，bool オブジェクトを返す関数オブジェクトと iterable オブジェクトを引数として渡すと，関数オブジェクトが `True` を返す要素のみを含んだ iterable オブジェクトである filter オブジェクトを返します．  
`filter(<関数オブジェクト> <iterable オブジェクト>)` のように使います．  
filter オブジェクトは，大抵は `list()` や `tuple()` で list や tuple にします．  

例 1.  
list `[3, -7, 7, 3, -3, -3, 0, -1, 10, -7]` の中から 0 より大きい要素のみを含んだ list を得るコードです．  
関数オブジェクトとしてラムダ関数を渡しています．  
関数は，要素に 1 つずつ適用されるイメージです．  

```python
f = filter(lambda x: x > 0, [3, -7, 7, 3, -3, -3, 0, -1, 10, -7])
print(f)    # <filter object at 0x7f4f726f8460>

lst = list(f)
print(lst)  # [3, 7, 3, 10]


# list 内包表記
lst = [x for x in [3, -7, 7, 3, -3, -3, 0, -1, 10, -7] if x > 0]
print(lst)  # [3, 7, 3, 10]
```


例 2.  
list `lst` の中で拡張子が `.txt` のファイル名のものを抽出した list `txts` を作っています．  

```python
files = ["report.txt", "memo.txt", "stats.csv", "README.md", "spec.txt"]
txts = list(filter(lambda x: x.split(".")[1] == "txt", files))
print(txts)     # ['report.txt', 'memo.txt', 'spec.txt']


# list 内包表記
txts = [x for x in files if x.split(".")[1] == "txt"]
print(txts)     # ['report.txt', 'memo.txt', 'spec.txt']
```

例 3.  
商品名と価格のペアからなる dict `prices` から価格が `1000` より小さい商品名を list `reasonables` にまとめています．  

```python
prices = {
    "poke_ball": 200,
    "great_ball": 600,
    "ultra_ball": 1200,
    "timer_ball": 1000,
    "repeat_ball": 1000
}

reasonables = list(filter(lambda x: prices[x] < 1000, prices))
print(reasonables)  # ['poke_ball', 'great_ball']


# list 内包表記
reasonables = [x for x in prices if prices[x] < 1000]
print(reasonables)  # ['poke_ball', 'great_ball']
```


# map()

map 関数は，関数オブジェクトと iterable オブジェクトを引数にとり，iterable オブジェクトの要素 1 つ 1 つに関数を適用して，その結果を iterable オブジェクトである map オブジェクトで返します．  
filter 関数と同様， `map(<関数オブジェクト>, <iterable オブジェクト>)` のように使います．  

例 1.  
map 関数で list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` の要素をすべて 2 乗した新しい list `squares` を作っています．  

```python
squares = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# list 内包表記
squares = [x * x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

例 2.  
文字列として渡された数値の list `str_lst` を，map 関数で組込み関数 int を `str_lst` のすべての要素に適用することで int オブジェクトに直した list `int_lst` を作っています．  

```python
str_lst = ["-6", "-5", "3", "1", "2", "6", "3", "8", "4", "-1"]
int_lst = list(map(int, str_lst))
print(int_lst)  # [-6, -5, 3, 1, 2, 6, 3, 8, 4, -1]


# list 内包表記
int_lst = [int(x) for x in str_lst]
print(int_lst)  # [-6, -5, 3, 1, 2, 6, 3, 8, 4, -1]
```

例 3.  
2 次元 list `data` の各 list ごとの平均値を list `avgs` にまとめています．  

```python
data = [[-11.81, 31.01, -36.15, -43.27, -30.26],
        [9.61, -8.99, 18.66, -27.4, 30.54],
        [-3.54, 31.17, 3.94, 20.54, 17.67]]

avgs = list(map(lambda x: sum(x) / len(x), data))
print(avgs)  # [-18.096, 4.484, 13.956]


# list 内包表記
avgs = [sum(x) / len(x) for x in data]
print(avgs)  # [-18.096, 4.484, 13.956]
```

## 参考

Effective Python では，filter 関数や map 関数より list 内包表記や dict 内包表記のほうが読みやすいとして内包表記を使うことを勧めています．  
速度は若干ですが filter 関数や map 関数のほうが内包表記より速いです．  

(ここまで Extra)  


# sorted()

引数として与えられた iterable オブジェクトをソートします．  
`<list オブジェクト>.sort()` が in-place でソートする (もとの list オブジェクトをソートする) のに対して，組込み関数 sorted はソートされた list を新しく作って返します．  
そのため，ソートしたいがもとの list はもとのままにしておきたいときに使います．  
引数に何も与えない場合は昇順にソートします．  

```python
src = [-6, -5, 3, 1, 2, 6, 3, 8, 4, -1]
dest = sorted(src)  # 組込み関数
print(src)  # [-6, -5, 3, 1, 2, 6, 3, 8, 4, -1]     <- もとのまま
print(dest)  # [-6, -5, -1, 1, 2, 3, 3, 4, 6, 8]     <- 昇順でソートされている

src.sort()  # in-place でソート
print(src)  # [-6, -5, -1, 1, 2, 3, 3, 4, 6, 8]     <= 昇順でソートされている
```

引数 reverse を `True` にすると降順でソートします．  

```python
src = [-6, -5, 3, 1, 2, 6, 3, 8, 4, -1]
dest = sorted(src, reverse=True)
print(src)  # [-6, -5, 3, 1, 2, 6, 3, 8, 4, -1]     <- もとのまま
print(dest)  # [8, 6, 4, 3, 3, 2, 1, -1, -5, -6]    <= 降順でソートされている

src.sort(reverse=True)
print(src)  # [8, 6, 4, 3, 3, 2, 1, -1, -5, -6]     <= 降順でソートされている
```

sorted 関数は仮引数として `key` をもっています．  
key として関数オブジェクトを与えると，その関数の適用結果に基づいてソートを行います．  

次のコードでは，人名 list `names` を苗字の昇順でソートしています．  

```python
names = ["Sosuke Natsume", "Ryunosuke Akutagawa", "Osamu Dazai"]
sorted_by_last_name = sorted(names, key=lambda x: x.split()[1])
print(sorted_by_last_name)  # ['Ryunosuke Akutagawa', 'Osamu Dazai', 'Sosuke Natsume']

names.sort(key=lambda x: x.split()[1])
print(names)    # ['Ryunosuke Akutagawa', 'Osamu Dazai', 'Sosuke Natsume']
```

こちらの例では，会議室の予約状況を管理している list `schedules` を予約の開始時刻 `start` が早い順にソートしています．  

```python
from pprint import pprint


schedules = [
    {
        "start": 12,
        "end": 14,
        "room": "meeting_room_A",
        "num": 12
    },
    {
        "start": 8,
        "end": 9,
        "room": "meeting_room_A",
        "num": 10
    },
    {
        "start": 18,
        "end": 19,
        "room": "meeting_room_A",
        "num": 5
    },
]

sorted_by_start = sorted(schedules, key=lambda x: x["start"])
pprint(sorted_by_start)
"""
[{'end': 9, 'num': 10, 'room': 'meeting_room_A', 'start': 8},
 {'end': 14, 'num': 12, 'room': 'meeting_room_A', 'start': 12},
 {'end': 19, 'num': 5, 'room': 'meeting_room_A', 'start': 18}]
"""

schedules.sort(key=lambda x: x["start"])
pprint(schedules)
"""
[{'end': 9, 'num': 10, 'room': 'meeting_room_A', 'start': 8},
 {'end': 14, 'num': 12, 'room': 'meeting_room_A', 'start': 12},
 {'end': 19, 'num': 5, 'room': 'meeting_room_A', 'start': 18}]
"""
```

複数の値に基づいてソートするには，関数の結果を tuple にします．  
次のコードの `schedules` には `start` が 12 である要素が 2 つあります．  
重複時に `end` が早いほうを先にするには関数の返り値を `(start, end)` の順に tuple にします．  

```python
from pprint import pprint


schedules = [
    {
        "start": 12,
        "end": 14,
        "room": "meeting_room_A",
        "num": 12
    },
    {
        "start": 8,
        "end": 9,
        "room": "meeting_room_A",
        "num": 10
    },
    {
        "start": 12,
        "end": 13,
        "room": "meeting_room_B",
        "num": 10
    },
    {
        "start": 18,
        "end": 19,
        "room": "meeting_room_A",
        "num": 5
    },
]

sorted_by_start = sorted(schedules, key=lambda x: (x["start"], x["end"]))
pprint(sorted_by_start)
"""
[{'end': 9, 'num': 10, 'room': 'meeting_room_A', 'start': 8},
 {'end': 13, 'num': 10, 'room': 'meeting_room_B', 'start': 12},
 {'end': 14, 'num': 12, 'room': 'meeting_room_A', 'start': 12},
 {'end': 19, 'num': 5, 'room': 'meeting_room_A', 'start': 18}]
"""

schedules.sort(key=lambda x: (x["start"], x["end"]))
pprint(schedules)
"""
[{'end': 9, 'num': 10, 'room': 'meeting_room_A', 'start': 8},
 {'end': 13, 'num': 10, 'room': 'meeting_room_B', 'start': 12},
 {'end': 14, 'num': 12, 'room': 'meeting_room_A', 'start': 12},
 {'end': 19, 'num': 5, 'room': 'meeting_room_A', 'start': 18}]
"""
```


# zip()

zip 関数は，引数として与えられた 2 つの iterable オブジェクトのインデックスが同じ要素どうしを tuple にした iterable オブジェクトである zip オブジェクトを作って返します．  

次のコードでは，x 座標の list `x_lst` と y 座標の list `y_lst` から，(x, y) 座標の list `coords` を作成しています．  

```python
x_lst = [-1, -5, 4, 5, 0, -8, 5, 3, -2, 7]
y_lst = [0, 5, 0, -9, -9, -8, 8, -7, -7, 3]

coords = list(zip(x_lst, y_lst))
print(coords)   # [(-1, 0), (-5, 5), (4, 0), (5, -9), (0, -9), (-8, -8), (5, 8), (3, -7), (-2, -7), (7, 3)]
```

次の例では，ユーザ ID の list `userids` とドメインの list `domains` からメールアドレスの list を作っています．  
2 つの iterable オブジェクトの要素数が異なる場合は，短いほうに合わせられます．  

```python
userids = ["1ickitung", "9b0ne", "rhyh0rn", "snor1ax"]
domains = ["example.com", "sample.co.jp"]

emails = []
for userid, domain in zip(userids, domains):
    emails.append(userid + "@" + domain)

print(emails)   # ['1ickitung@example.com', '9b0ne@sample.co.jp']

# Extra
emails = [userid + "@" + domain for userid, domain in zip(userids, domains)]
print(emails)   # ['1ickitung@example.com', '9b0ne@sample.co.jp']
```

# type()

type 関数はオブジェクトの属するクラス (型 : type) を返す関数です．  
返り値は type オブジェクトになります．  
type オブジェクトの根本的な機能はクラスを作ることですが，私たちが使うときはたいていオブジェクトのクラスを知るために使います．  
クラスについては Chapter 7 で取り上げます．  

```python
print(type(1))          # <class 'int'>
print(type("str_obj"))  # <class 'str'>
print(type([0, 1, 2]))  # <class 'list'>
print(type(type))       # <class 'type'>
```

# isinstance()

isinstance 関数は，引数にオブジェクトとクラスオブジェクトを渡すとオブジェクトがクラスに属している場合は `True`，そうでない場合は `False` を返す関数です．  
オブジェクトの属しているクラスが継承しているすべてのクラスで `True` を返します．  
クラスや継承については Chapter 7 で取り上げます．  

```python
print(isinstance(1, int))           # True
print(isinstance("str_obj", str))   # True
print(isinstance([0, 1, 2], list))  # True

print(isinstance(1, str))           # False
print(isinstance("str_obj", int))   # False
print(isinstance([0, 1, 2], tuple))  # False
```

# 練習問題


## Q 1

実行したプロセスのプロセス ID と実行結果が dict `results` にまとめられています．  
0 の場合はプロセスが正常に終了したことを表していますが，それ以外の値の場合は異常終了を表しています．  
すべてのプロセスが正常に終了している場合は `succeeded`，1 つでも異常終了しているプロセスがあれば `failed` と出力してください．  

例 1.  

```python
results = {
    "25244": 0,
    "25263": 0,
    "26809": 0,
    "26810": 0
}
```

出力  

```
succeeded
```

例 2.  

```python
results = {
    "25244": 0,
    "25263": 0,
    "26809": 1,
    "26810": 0
}
```

出力  

```
failed
```

例 3.  

```python
results = {
    "25244": 1,
    "25263": 1,
    "26809": 1,
    "26810": 1
}
```

出力  

```
failed
```


## Q 2

次の list `integers` を絶対値が大きい順にソートした新しい list を作って，標準出力に出力してみましょう．  
`integers` は変更しないものとします．  

```python
integers = [2, -3, -6, -4, -3, 5, -1, -2, 7, 4]
```

期待される出力は次のとおりです．  

```python
[7, -6, 5, -4, 4, -3, -3, 2, -2, -1]
```


## Q 3

2 つの整数からなる tuple を要素にもつ list `pairs` があります．  
各 tuple の要素のうち，小さいほうを左側に，大きいほうを右側にした tuple を要素にもつ新しい list `arranged_pairs` を作って標準出力に出力してください．  

```python
pairs = [(3, 2), (5, 0), (4, 3), (4, 8), (1, 6)]
```

期待される出力は次のとおりです．  

```python
[(2, 3), (0, 5), (3, 4), (4, 8), (1, 6)]
```


## Q 4

電話番号の list `hyphenated_phone_numbers` があります．  
ハイフンを除去した電話番号を要素にもつ list `phone_numbers` を作って，標準出力に出力してください．  
`hyphenated_phone_numbers` には変更を加えないようにしましょう．  

```python
hyphenated_phone_numbers = [
    "XXX-XXXX-XXXX",
    "YYY-YYYY-YYYY",
    "ZZZ-ZZZZ-ZZZZ",
]
```

期待される出力は次のとおりです．  

```python
['XXXXXXXXXXX', 'YYYYYYYYYYY', 'ZZZZZZZZZZZ']
```

## Q 5

あるディレクトリの内容が list `files` として取得できました．  
`files` の中から拡張子が `.json` であるファイル数を標準出力で出力してください．  

```python
files = [
    "bower.hjson",
    "configjson"
    "devcontainer.json",
    "requirements.txt",
    "settings.json",
    "tox.ini",
]
```

期待される出力は次のとおりです．  

```
2
```


## Q 6

文字列を要素にもつ list `zen_beginning` の全文字数を数え，標準出力に出力してみましょう．  
文字数には空白やピリオドも含みます．  

```python
zen_beginning = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense."
]
```

期待される出力は次のとおりです．  

```
183
```


## Q 7

次の list `smartphones` は，スマートフォンの機種名 `device` と発売日 `released` の情報をもった dict を要素にもっています．  
発売日が早い順に要素をソートした新しい list を作って，標準出力に出力してください．  
`smartphones` には変更を加えないようにしましょう．  

```python
smartphones = [
    {
        "device": "Xperia 1 II SOG01",
        "released": "2020-06-18"
    },
    {
        "device": "iPhone SE",
        "released": "2020-04-24"
    },
    {
        "device": "HUAWEI P30 lite",
        "released": "2019-08-08"
    },
    {
        "device": "Garaxy A41",
        "released": "2020-07-08"
    },
]
```

期待される出力は次のとおりです．  

```python
[{'device': 'HUAWEI P30 lite', 'released': '2019-08-08'},
 {'device': 'iPhone SE', 'released': '2020-04-24'},
 {'device': 'Xperia 1 II SOG01', 'released': '2020-06-18'},
 {'device': 'Garaxy A41', 'released': '2020-07-08'}]
```


## Q 8

自分が読んだ Python の本の中でおすすめの本が，個人的おすすめ順に list `recommended_books` にまとめられています．  
また，これらの本の名前と ISBN の対応が dict `database` に格納されています．  
recommended_books の要素を in-place で ISBN の順に並び替えてください．  

```python
recommended_books = [
    "Fluent Python",
    "Python データサイエンスハンドブック",
    "Python による数値計算とシミュレーション",
    "Effective Python",
    "ゼロから作る Deep Learning"
]

database = {
    "Fluent Python": {
        "ISBN": "978-4873118178",
        "comment": "Python の言語使用について理解が深まり，コーディングの自由度が広がる"
    },
    "Python データサイエンスハンドブック": {
        "ISBN": "978-4873118413",
        "comment": "NumPy, Pandas, Matplotlib といったライブラリの使い方を学べる．英語版は Web 上で無料公開されている"
    },
    "Python による数値計算とシミュレーション": {
        "ISBN": "978-4274221705",
        "comment": "科学分野で使われる数値計算の方法の基礎を Python で学べる"
    },
    "Effective Python": {
        "ISBN": "978-4873119175",
        "comment": "Python を使用した開発や運用で有効なコーディングのテクニックが学べる"
    },
    "ゼロから作る Deep Learning": {
        "ISBN": "978-4873117584",
        "comment": "Deep Learning の仕組みについて Python でざっくり学べる"
    }
}
```

期待される出力は次のとおりです．  

```
['Python による数値計算とシミュレーション', 'ゼロから作る Deep Learning', 'Fluent Python', 'Pythonデータサイエンスハンドブック', 'Effective Python']
```


## Q 9

次の 2 つの list `keys` と `values` から dict `cpu_usage` を作って標準出力に出力してください．  
keys と values は，インデックスが同じ要素どうしがそれぞれ key と value に対応しています．  

```python
keys = ["us", "sy", "ni", "id", "wa", "hi", "si", "st"]
values = [0.1, 0.2, 0.0, 99.7, 0.0, 0.0, 0.0]
```

期待される出力は次のとおりです．  
なお，dict の要素の順番は問いません．  

```
{'hi': 0.0, 'id': 99.7, 'ni': 0.0, 'si': 0.0, 'sy': 0.2, 'us': 0.1, 'wa': 0.0}
```


## Q 10

ある企業向けサービスの展開を考えています．  
list `clients` には，これから運用を検討している企業の企業名とユーザー数が格納されています．  
サービスを運用できる最大ユーザー数を標準入力で与えたとき，運用する企業数が最大となるときの企業の組合せの一例を標準出力に出力するプログラムを実装してください．  

```python
clients = [("シルフカンパニー", 2000),   ("デボンコーポレーション", 4000), ("てんきけんきゅうじょ", 1000),
           ("ポケッチカンパニー", 2000), ("カントーラジオきょく", 1000), ("カントーはつでんしょ", 2000),
           ("ギンガハクタイビル", 3000), ("トクサネうちゅうセンター", 4000),  ("タマムシデパート", 1000)]
```

入力例と出力例は次のようになります．  

|入力|出力|
|:---:|:---:|
|5000|`['てんきけんきゅうじょ', 'カントーラジオきょく', 'タマムシデパート', 'シルフカンパニー']`|
|10000|`['てんきけんきゅうじょ', 'カントーラジオきょく', 'タマムシデパート', 'シルフカンパニー', 'ポケッチカンパニー', 'カントーはつでんしょ']`|
|15000|`['てんきけんきゅうじょ', 'カントーラジオきょく', 'タマムシデパート', 'シルフカンパニー', 'ポケッチカンパニー', 'カントーはつでんしょ', 'ギンガハクタイビル']`|


<hr>

[Chapter 6 練習問題解答例](Answers6.md)  
[Index](../README.md)
