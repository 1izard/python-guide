# Chapter 3 練習問題回答例

## Q 1

```python
n = int(input())

if n % 3 == 0:
    print("Yes")
else:
    print("No")
```


## Q 2

```python
n = int(input())

if n % 7 == 0 and n % 2 == 0:
    print("Yes")
else:
    print("No")
```


## Q 3

```python
n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
```


## Q 4

```python
a = int(input())
b = int(input())
c = int(input())

tokiwa_price = 100 * a + 400 * b + 1200 * c - 900 * (c // 10)
hanada_price = 200 * a + 500 * b + 1000 * c - 500 * (b // 5)

if tokiwa_price <= hanada_price:
    print("トキワショップ")
else:
    print("ハナダショップ")
```

## Q 5

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

## Q 6

```python
total = 0
i = 1

while i <= 100:
    total += i
    i += 1

print(total)  # 5080
```


## Q 7

`s` を1文字ずつ照合していって，`e` に一致したら break 文で抜けます．  
i が n より大きいときは見つからなかった場合なので i に -1 を代入します．  

```python
s = input()

i = 0
n = len(s)
while i < n:
    if s[i] == "e":
        break
    i += 1

if i >= n:
    i = -1
print(i)
```


## Q 8

文字列 `s` を後ろから見ていくため，`i` を `文字列sの長さ - 1` から開始してデクリメントします．  
`a` に一致した回数を `cnt` でカウントし，`cnt` が `2` になったらbreak文で抜けます．  

```python
s = input()

n = len(s)
i = n - 1
cnt = 0
while i >= 0:
    if s[i] == "a":
        cnt += 1
        if cnt == 2:
            break
    i -= 1

print(i)
```


## Q 9

A, B の手を `(a, b)` として場合分けすると，下の表のようになります．  
表から，次のことがわかります．  
- Aが勝つ場合，`(a + 1) % 3 = b` が成り立つ
- Bが勝つ場合，`(b + 1) % 3 = a` が成り立つ

| Aが勝つ場合 | Bが勝つ場合 | 引き分け |
| :---------: | :---------: | :------: |
|   (0, 1)    |   (1, 0)    |  (0, 0)  |
|   (1, 2)    |   (2, 1)    |  (1, 1)  |
|   (2, 0)    |   (0, 2)    |  (2, 2)  |

よって，プログラムは次のように書けます．  

```python
a = 1
b = 2

if (a + 1) % 3 == b:
    print("A win")
elif a == (b + 1) % 3:
    print("B win")
else:
    print("Tie")
```


## Q 10

`n` は文字列のまま扱います．  
インデックス用の変数を `i`，移動数をカウントするための変数を `cnt` とします．  
はじめ，自分は1の位にいるので `i = len(n) - 1` とします．  
`i -= int(n[i])` で，自分がいる位の数だけ `i` を減らして左の桁に移動することを，最高位を超えるまで(`i <= 0` になるまで)繰り返します．  
ただし，`n[i] == "0"` となった場合は `i` が減らず左の桁に移動できず，最高位に辿り着けないためbreak文で抜けます．  
最後に，最高位まで辿り着いたかどうかを `i <= 0` で判定して結果を出力します．  

```python
n = input()

i = len(n) - 1
cnt = 0
while i > 0:
    if n[i] == "0":
        break
    cnt += 1
    i -= int(n[i])

if i <= 0:
    print(cnt)
else:
    print(-1)
```


## Q 11

```python
import random


player = 0
cpu = 0

print("さいしょはグー，じゃんけん > ", end="")

while player == cpu:
    player = int(input())
    cpu = random.randint(0, 2)

    print(f"プレイヤー:{player}, CPU:{cpu}")

    if (player + 1) % 3 == cpu:
        print("プレイヤーのかち！")
    elif player == (cpu + 1) % 3:
        print("CPUのかち！")
    else:
        print("あいこで > ", end="")
```

<hr>

[Chapter 3 基本構文](Chapter3.md)  
[Index](../README.md)
