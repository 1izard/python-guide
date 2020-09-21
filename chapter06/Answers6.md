# 練習問題 6 解答例

## Q 1

for 文で書くと  

```python
results = {
    "38738": 0,
    "39123": 0,
    "42449": 0,
    "42510": 0
}

for v in results.values():
    if v != 0:
        print("failed")
        break
else:
    print("succeeded")
```

any 関数を使うと  

```python
results = {
    "38738": 0,
    "39123": 0,
    "42449": 0,
    "42510": 0
}

if any(results.values()):
    print("failed")
else:
    print("succeeded")

```


## Q 2

```python
integers = [2, -3, -6, -4, -3, 5, -1, -2, 7, 4]
sorted_by_abs_desc = sorted(integers, key=abs, reverse=True)
print(sorted_by_abs_desc)   # [7, -6, 5, -4, 4, -3, -3, 2, -2, -1]
```


## Q 3

```python
pairs = [(3, 2), (5, 0), (4, 3), (4, 8), (1, 6)]

arragend_pairs = []
for pair in pairs:
    arragend_pairs.append((min(pair), max(pair)))
print(arragend_pairs)   # [(2, 3), (0, 5), (3, 4), (4, 8), (1, 6)]
```

(Extra)  

map 関数を使うと  

```python
pairs = [(3, 2), (5, 0), (4, 3), (4, 8), (1, 6)]

arragend_pairs = list(map(lambda x: (min(x), max(x)), pairs))
print(arragend_pairs)   # [(2, 3), (0, 5), (3, 4), (4, 8), (1, 6)
```

list 内包表記を使うと  

```python
pairs = [(3, 2), (5, 0), (4, 3), (4, 8), (1, 6)]

arragend_pairs = [(min(x), max(x)) for x in pairs]
print(arragend_pairs)   # [(2, 3), (0, 5), (3, 4), (4, 8), (1, 6)]
```

(ここまで Extra)  


## Q 4

```python
hyphenated_phone_numbers = [
    "XXX-XXXX-XXXX",
    "YYY-YYYY-YYYY",
    "ZZZ-ZZZZ-ZZZZ",
]

phonenumbers = []
for number in hyphenated_phone_numbers:
    phonenumbers.append("".join(number.split("-")))
print(phonenumbers) # ['XXXXXXXXXXX', 'YYYYYYYYYYY', 'ZZZZZZZZZZZ']
```

(Extra)  

map 関数を使うと  

```python
hyphenated_phone_numbers = [
    "XXX-XXXX-XXXX",
    "YYY-YYYY-YYYY",
    "ZZZ-ZZZZ-ZZZZ",
]

phonenumbers = list(map(lambda x: "".join(x.split("-")), hyphenated_phone_numbers))
print(phonenumbers) # ['XXXXXXXXXXX', 'YYYYYYYYYYY', 'ZZZZZZZZZZZ']
```

list 内包表記だと  

```python
hyphenated_phone_numbers = [
    "XXX-XXXX-XXXX",
    "YYY-YYYY-YYYY",
    "ZZZ-ZZZZ-ZZZZ",
]

phonenumbers = ["".join(x.split("-")) for x in hyphenated_phone_numbers]
print(phonenumbers) # ['XXXXXXXXXXX', 'YYYYYYYYYYY', 'ZZZZZZZZZZZ']
```

(ここまで Extra)  


## Q 5

```python
files = [
    "bower.hjson",
    "configjson"
    "devcontainer.json",
    "requirements.txt",
    "settings.json",
    "tox.ini",
]

cnt = 0
for f in files:
    if f[-5:] == ".json":
        cnt += 1
print(cnt)
```

(Extra)  

filter 関数を使うと次のようになります．  
filter オブジェクトから作られた list の長さが条件に合致した要素の個数になります．  

```python
files = [
    "bower.hjson",
    "configjson"
    "devcontainer.json",
    "requirements.txt",
    "settings.json",
    "tox.ini",
]

print(len([f for f in files if f[-5:] == ".json"]))
```

list 内包表記だと  

```python
files = [
    "bower.hjson",
    "configjson"
    "devcontainer.json",
    "requirements.txt",
    "settings.json",
    "tox.ini",
]

print(len(list(filter(lambda x: x[-5:] == ".json", files))))
```

(ここまで Extra)  


## Q 6

```python
zen_beginning = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense."
]

cnt = 0
for line in zen_beginning:
    cnt += len(line)

print(cnt)  # 183
```

(Extra)  

sum 関数と map 関数を使うと  

```python
zen_beginning = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense."
]

print(sum(list(map(lambda x: len(x), zen_beginning))))  # 183
```

sum 関数と list 内包表記を使うと  

```python
zen_beginning = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense."
]

print(sum([len(x) for x in zen_beginning]))  # 183
```

(ここまで Extra)  


## Q 7

```python
from pprint import pprint


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


sorted_by_released = sorted(smartphones, key=lambda x: x["released"])
pprint(sorted_by_released)
"""
[{'device': 'HUAWEI P30 lite', 'released': '2019-08-08'},
 {'device': 'iPhone SE', 'released': '2020-04-24'},
 {'device': 'Xperia 1 II SOG01', 'released': '2020-06-18'},
 {'device': 'Garaxy A41', 'released': '2020-07-08'}]
"""
```

## Q 8

in-place なので `<list オブジェクト>.sort()` を使います．  

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

recommended_books.sort(key=lambda x: database[x]["ISBN"])
print(recommended_books)
```

## Q 9

```python
keys = ["us", "sy", "ni", "id", "wa", "hi", "si", "st"]
values = [0.1, 0.2, 0.0, 99.7, 0.0, 0.0, 0.0]

cpu_usage = {}
for k, v in zip(keys, values):
    cpu_usage[k] = v
print(cpu_usage)    # {'hi': 0.0, 'id': 99.7, 'ni': 0.0, 'si': 0.0, 'sy': 0.2, 'us': 0.1, 'wa': 0.0}
```

(Extra)  

```python
keys = ["us", "sy", "ni", "id", "wa", "hi", "si", "st"]
values = [0.1, 0.2, 0.0, 99.7, 0.0, 0.0, 0.0]

cpu_usage = {k: v for k, v in zip(keys, values)}
print(cpu_usage)    # {'hi': 0.0, 'id': 99.7, 'ni': 0.0, 'si': 0.0, 'sy': 0.2, 'us': 0.1, 'wa': 0.0}
```

(ここまで Extra)


## Q 10

clients をユーザー数の昇順に並び替えて先頭から最大ユーザー数を超えるまでの企業が，企業数が最大のときの企業の組合せになります．  

```python
clients = [("シルフカンパニー", 2000),   ("デボンコーポレーション", 4000), ("てんきけんきゅうじょ", 1000),
           ("ポケッチカンパニー", 2000), ("カントーラジオきょく", 1000), ("カントーはつでんしょ", 2000),
           ("ギンガハクタイビル", 3000), ("トクサネうちゅうセンター", 4000),  ("タマムシデパート", 1000)]


print("user num capacity > ", end="")
capacity = int(input())     # 最大ユーザー数

clients.sort(key=lambda x: x[1])    # ユーザー数の昇順にソート

user_num = 0
ans = []
for client in clients:
    user_num += client[1]   # ユーザー数をカウント
    if user_num > capacity:
        break
    ans.append(client[0])   # user_num が capacity を超えなかったら ans に追加

print(ans)
```


<hr>

[Chapter 6 組込み関数](Chapter6.md)  
[INdex](../README.md)
