# Chapter4 練習問題回答例

## Q1

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "", end="")
    print()
```

内側のforループの変数 `j` の取りうる値を，外側のforループの変数 `i` によって 1 ずつ増やしていきます．  


## Q2

```python
lst = [475, 358, -160, -385, 173, 148, 128, -265, -472, -82, 289, -465, 365, 248, 180, 451, 158, 51, 431, -6]

total = 0
for n in lst:
    total += n

print(total)    # 1620
```


## Q3

```python
lst = [321, -325, 313, -452, 342, 281, -237, -322, 103,
       143, 345, -349, -293, 487, 494, -23, 319, -154, -5, -95]

ans = lst[0]
for n in lst[1:]:
    if ans < n:
        ans = n

print(ans)      # 494
```


## Q4

最大値をとる要素がある場合は最小のインデックスを出力するため，最大値とそのインデックスを保持する変数 `max_n`，`ans` を更新する条件は `max_n < n` となります．  

```python
lst = [131, 101, 79, 134, 83, 146, 78, 143, 140, 61, 92, 56, 76, 77, 146, 58, 137, 126, 85, 82]

ans = 0
max_n = lst[0]
for i, n in enumerate(lst[1:], 1):
    if max_n < n:
        ans = i
        max_n = n
print(ans)      # 5
```


## Q5

```python
ans = 1
n = 7
for i in range(2, n + 1):
    ans *= i
print(ans)      # 5040
```


## Q6

n個の中からk個選ぶときの組合せは `nCk = n * (n - 1) * ... + (n - k + 1) / k * (k - 1) * ... * 1` で計算できます．  
for文 を使うと次のように書けます．  

```python
n = 7
k = 3

a = n
for i in range(n - 1, n - k, -1):
    a *= i

b = k
for i in range(k - 1, 0, -1):
    b *= i

ans = a // b
print(ans)      # 35
```


## Q7

```python
e2j_dct = {
    "Vapareon": "シャワーズ",
    "Jolteon": "サンダース",
    "Flareon": "ブースター",
    "Espeon": "エーフィ",
    "Umbreon": "ブラッキー"
}

j2e_dct = {}
for k, v in e2j_dct.items():
    j2e_dct[v] = k
```

(Extra)

内包表記で書くと

```python
e2j_dct = {
    "Vapareon": "シャワーズ",
    "Jolteon": "サンダース",
    "Flareon": "ブースター",
    "Espeon": "エーフィ",
    "Umbreon": "ブラッキー"
}

j2e_dct = {v: k for k, v in e2j_dct.items()}
```

(ここまでExtra)


## Q8

```python
from pprint import pprint


category_dct = {
    "TA0001": "Innitial Access",
    "TA0002": "Execution",
    "TA0003": "Persistence",
}

data_lst = [
    {
        "datetime": "2020-08-15 20:10:43",
        "category": "TA0002",
        "severity": "Middle"
    },
    {
        "datetime": "2020-08-16 09:11:41",
        "category": "TA0003",
        "severity": "Low"
    },
    {
        "datetime": "2020-08-16 10:27:30",
        "category": "TA0003",
        "severity": "Low"
    },
    {
        "datetime": "2020-08-16 21:02:56",
        "category": "TA0002",
        "severity": "Middle"
    },
    {
        "datetime": "2020-08-17 08:30:17",
        "category": "TA0001",
        "severity": "High"
    },
    {
        "datetime": "2020-08-17 10:34:49",
        "category": "TA0002",
        "severity": "Low"
    },
]

for data in data_lst:
    data["category"] = category_dct.get(data["category"], "Unknown")
pprint(data_lst)
```


## Q9

```python
from pprint import pprint


tool_lst = [
    {
        "name": "Pandas",
        "lang": "Python"
    },
    {
        "name": "React",
        "lang": "JavaScript"
    },
    {
        "name": "NumPy",
        "lang": "Python"
    },
    {
        "name": "Lombok",
        "lang": "Java"
    },
    {
        "name": "Boost",
        "lang": "C++"
    },
    {
        "name": "Deno",
        "lang": "JavaScript"
    }
]

tool_dct = {}
for tool in tool_lst:
    if tool["lang"] not in tool_dct:
        tool_dct[tool["lang"]] = []
    tool_dct[tool["lang"]].append(tool["name"])

pprint(tool_dct)
```

(Extra)

`setdefault` メソッドを使うと次のように書けます．  
`setdefault` メソッドは key に対応する value を返します．  
この場合 key に対応する list を返すので，続けて `append` メソッドを使用して list に要素を追加することができます．  

```python
from pprint import pprint


tool_lst = [
    {
        "name": "Pandas",
        "lang": "Python"
    },
    {
        "name": "React",
        "lang": "JavaScript"
    },
    {
        "name": "NumPy",
        "lang": "Python"
    },
    {
        "name": "Lombok",
        "lang": "Java"
    },
    {
        "name": "Boost",
        "lang": "C++"
    },
    {
        "name": "Deno",
        "lang": "JavaScript"
    }
]

tool_dct = {}
for tool in tool_lst:
    tool_dct.setdefault(tool["lang"], []).append(tool["name"])

pprint(tool_dct)
```

(ここまでExtra)


## Q10

```python
from pprint import pprint


result_dct = {
    "Satoshi": {
        "Listening": 5,
        "Reading": 5,
        "Speaking": 200,
        "Writing": 5
    },
    "Kasumi": {
        "Listening": 495,
        "Reading": 495,
        "Speaking": 200,
        "Writing": 200
    },
    "Takeshi": {
        "Listening": 230,
        "Reading": 455,
        "Speaking": 95,
        "Writing": 60
    }
}

avg_dct = {
    "Listening": 0,
    "Reading": 0,
    "Speaking": 0,
    "Writing": 0
}

n = len(result_dct)    # 人数
for section in avg_dct:    # keyを１つずつ回す
    t = 0
    for score_dct in result_dct.values():   # 3人のテスト結果を回す
        t += score_dct[section]  # テスト結果から外側のfor文で回しているsectionのスコアを加えて合計を求める
    avg_dct[section] = t / n  # 平均なので最後に合計を人数で割る

pprint(avg_dct)
```


(Extra)

## Q11

```python
A = [[2, 0, 8, 7], [2, 4, 8, 3], [9, 0, 4, 3]]
B = [[9, 9, 8, 0, 4], [5, 1, 5, 3, 8], [3, 6, 4, 1, 9], [8, 5, 5, 3, 3]]

L = len(A)
M = len(B[0])
N = len(B)

C = [[0] * M for _ in range(L)]
for i in range(L):
    for j in range(M):
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]

print(C)
```