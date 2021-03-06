# 練習問題 1 解答例

## Q 1

剰余の計算は `%` を使います．  

```python
a = 7
b = 3

ans = a % b
print(ans)  # 1
```


## Q 2

```python
a = -7
b = 3

print(a % b)  # 2
```

Pythonでは，負数を正の数で割ったときの余りはプラスになります．  
(-7 % 3 = -1 となる言語もあります)


## Q 3

```python
a = 1_234_567_890
b = 1_234_567_890_123_456_789

print(a * b)
# 1524157875171467887501905210
```

Python ではこのような大きな値も計算できます．  


## Q 4

```python
a = 2

print(a ** 10)  # 1024
```

2 の累乗の値はよく使われるので覚えておくと便利です．  

|                           |      値       |
| :-----------------------: | :-----------: |
|          2 ** 0           |       1       |
|          2 ** 1           |       2       |
|          2 ** 2           |       4       |
|          2 ** 3           |       8       |
|          2 ** 4           |      16       |
|          2 ** 5           |      32       |
|          2 ** 6           |      64       |
|          2 ** 7           |      128      |
|  2 ** 8  = 8bit = 1 Byte  |      256      |
|          2 ** 9           |      512      |
|          2 ** 10          |     1'024     |
| 2 ** 16 = 16 bit = 2 Byte |    65'536     |
| 2 ** 32 = 32 bit = 4 Byte | 4'294'967'296 |


## Q 5

1 時間を `分` に直すと 60 分，60 分を `秒` に直すと `(60 * 60) 秒`なので，3 時間を `分` に直すと `3 * (60 * 60) 秒`です．


```python
a = 3
print(3 * 60 * 60)  # 10800
```


## Q 6

```python
b = 10
h = 5

print(b * h / 2)  # 25.0
```

## Q 7

```python
a = 2
b = "は素数?: "
c = True

s = str(a) + b + str(c)
print(s)  # 2は素数?: True
```


## Q 8

`10000 / 33 = 303.03...` ですが，最大の個数を求めているので小数点以下を切り捨てます．  
そのため `//` を使います．  

```python
a = 10000
b = 33

print(a // b)   # 303
```


## Q 9

```python
p = 0.5
print(p ** 10)  # 0.0009765625
```


## Q 10

消費税率が `C = 0.08` なので，税抜価格を `(1.0 + C)` 倍したものが税込価格になります．  
最後に，小数点以下を切り捨てるため `int()` を使います．  

```python
a = 28
n = 3
C = 0.08

ans = int(a * n * (1.0 + C))
print(ans)    # 90
```

## Q 11

カレンダーのマス目を 0 から数えると，以下のようになります．  

|  日   |  月   |  火   |  水   |  木   |  金   |  土   |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   0   |   1   |   2   |   3   |   4   |   5   |   6   |
|   7   |   8   |   9   |  10   |  11   |  12   |  13   |
|  14   |  15   |  16   |  17   |  18   |  19   |  20   |
|  21   |  22   |  23   |  24   |  25   |  26   |  27   |
|  28   |  29   |  30   |  31   |  32   |  33   |  34   |
|  35   |  36   |  37   |  38   |  39   |  40   |  41   |

0 から 6 までは第 1 週目，7 から 13 までは第 2 週目，...です．
したがって，n 番目のマス目は第 `(n // 7 + 1)` 週目であることがわかります．  

一方，問題文より X 月の 1 日は金曜日なので，`マス目の番号 n = 日付 + 4` です．  
よって，22 日のマス目の番号は `22 + 4 = 26` になります．  

以上より，22 日は第 `((22 + 4) // 7 + 1) = 4` 週目であることがわかります．  

```python
n = 22

ans = ((n + 4) // 7 + 1)
print(ans)
```

(Extra)

## Q 11

1 を 1 bit 左にシフトすると 2，2 を 1 bit 左にシフトすると 4，4 を 1 bit 左にシフトすると 8，...，というように，1 を x bit だけ左シフトしたものは 2 の x 乗になります．  

| 10進数 | 2進数 |
| :----: | :---: |
|   1    | 0001  |
|   2    | 0010  |
|   4    | 0100  |
|   8    | 1000  |

したがって，1 を 10 bit だけ左シフトすると 2 の 10 乗が求まります．  
`+` や `*` といった算術演算よりシフト演算の方が高速なので，こちらの方が速く 2 の累乗を計算できます．  
`bit 全探索` を行う際に使ったりします．  

```python
a = 1

ans = 1 << 10
print(ans)  # 1024
```


<hr>

[Chapter 1 組込みデータ型](Chapter1.md)  
[Index](../README.md)
