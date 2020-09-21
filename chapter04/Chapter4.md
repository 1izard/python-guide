# Chapter 4 基本データ構造

# 基本データ構造

この章では，複数のオブジェクトを保持するために使用される基本的なデータ構造を導入します．  
具体的には以下になります．  

|       名前       |                 説明                 |                  例                   |               特徴                |
| :--------------: | :----------------------------------: | :-----------------------------------: | :-------------------------------: |
|       list       |          複数のデータを格納          |              `[1, 2, 3]`              |    ミュータブル(値を変更可能)     |
|  tuple (タプル)  |          複数のデータを格納          |              `(1, 2, 3)`              | イミュータブル (値を変更できない) |
| dict(辞書) | key, valueのペアで複数のデータを格納 | `{"name": "Flareon", "type": "Fire"}` |           ミュータブル            |

<br>

# list

例を見てわかる通り，複数のオブジェクトを保持するデータ構造です．  
list には int 型でも str 型でもなんでも格納できます．  

```python
int_lst = [10, 11, 12, 13, 14, 15]
float_lst = [3.1, -6.2, -190.2, 66.7]
str_lst = ["Eevee", "Vaporeon", "Jolteon", "Flareon"]
bool_lst = [True, False, True]
misc_lst = [10, 3.1, "Eevee"]
empty_lst = []
```

多次元にもできます．  

```python
lst_2_3 = [
  [10, 11, 12],
  [20, 21, 22]
]   # 2 x 3

lst_2_2_3 = [
  [
    [100, 101, 102],
    [110, 111, 112],
  ],
  [
    [200, 201, 202],
    [210, 211, 212]
  ]
]   # 2 x 2 x 3

misc_lst = [
  0, 1, 2,
  [10, 11],
  [
    [100, 101, 102, 103],
    [110, 111, 112, 113]
  ]
]
```


## 初期化

list の初期化にはいろいろな方法があります．  

### 要素で初期化

これまでの例のように，`[]`の中に要素を `,`(カンマ) で区切って羅列することで，それらの要素を含んだ list オブジェクトが作れます．  
`[]` の中に何も要素を入れない場合は空 list になります．  

```python
int_lst = [10, 11, 12, 13, 14, 15]
empty_lst = []
```

同じ値の複数個の要素で初期化する場合は `*`演算子で要素を繰り返して生成することができます．(`*`演算子は初期化以外のときでも list をコピーするために使用できます)

```python
ones = [1] * 5    # [1, 1, 1, 1, 1]
one_two_threes = [1, 2, 3] * 3    # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

(後回し: 以下は list 内包表記，インデックス，コピー，for文の項目のあとに読んでください)  
多次元 list の初期化に `*` を使う場合には注意が必要です．  
たとえば以下のように初期化したとしましょう．  

```python
x = [[0] * 2] * 3   # [[0, 0], [0, 0], [0, 0]]
```

これは以下と同じことをしています．  

```python
e = [0] * 2
x = [e, e, e]    # [[0, 0], [0, 0], [0, 0]]
```

この場合，たとえば `x[0][0]` に1を代入すると `x[1][0]`，`x[2][0]` も1になります．  

```python
x[0][0] = 1
print(x)    # [[1, 0], [1, 0], [1, 0]]
```

理由は，`*` による list のコピーが shallow copy であり，list `x[0]`，`x[1]`， `x[2]` がすべて同じ要素を参照しているからです．  
回避案としては，最も内側の list だけを `*` で生成し，残りを list 内包表記で書けば，`*` に準ずる簡潔さで list を作れます．  

```python
x = [[0] * 2 for _ in range(3)]   # [[0, 0], [0, 0], [0, 0]]
x[0][0] = 1
print(x)    # [[1, 0], [0, 0], [0, 0]]
```

(ここまで後回し)

(ここから下もまた後回し: list のメソッドと for 文の項目の後で読んでください)  

### 空 list に `append()` して初期化

要素数が多くて書ききれない場合や，要素をロジック的に作れる場合のわかりやすい初期化の方法として，for 文を用いて 空 list に append メソッドで繰り返し要素を追加していく方法があります．  
ロジックが 1 行で書けるような場合は，後述する list 内包表記でもっと簡潔に書けるのでそちらの方が好まれますが，list内包表記に慣れないうちは簡単なこちらの方法を使うのがいいかもしれません．  
(Python の for 文と `append()` は非常に遅いです...)

次の例は，0 から 9 までの整数を要素としてもつ list を，for 文，空 list，append メソッドで作る例です．  
同じことは `list(range(10))` でできます．  

```python
lst1 = []
for i in range(10):
    lst1.append(i)

print(lst1)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

次の例は，2 の累乗の 0 乗から 9 乗までを要素としてもつ list を，for 文，空 list，append メソッドで作る例です．  
list 内包表記では `[2 ** i for i in range(10)]` と書けます．  

```python
lst1 = []
for i in range(10):
    lst1.append(2 ** i)

print(lst1)  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

(ここまで後回し)

### `list()`で初期化

組込み関数 `list()` に Iterable オブジェクト を与えることで list オブジェクト を作ることができます．  
Iterable(=反復可能=繰り返し処理できる) オブジェクトとは list や tuple， dict などのオブジェクトのことをいいます．  
Iterable という型があるわけではなく，要素を 1 つ 1 つ取り出すなど繰り返し処理が可能なオブジェクトをまとめてそう呼んでいます．  
何となく，複数の値が並んでいるようなオブジェクトをイメージしていただけたらいいです．  

`list()` を使って，tuple や dict のオブジェクトから list オブジェクト を作れます．  
tuple はイミュータブル(=値を変更できない)ですが，list はミュータブル(=値を変更可能)です．  
また，Dicrionary を引数として与えると全ての key の list オブジェクト が作られます．  

```python
list_from_tuple = list((1, 2, 3))   # [1, 2, 3]
list_from_dicrionary = list({"name": "Flareon", "type": "Fire"})  # ["name", "type"]
```

文字列 (str オブジェクト) も 1 文字ずつ取り出せるので iterable オブジェクトの 1 つです．  

```python
list_from_str = list("一文字ずつ要素になります．")
# ['一', '文', '字', 'ず', 'つ', '要', '素', 'に', 'な', 'り', 'ま', 'す', '．']
```

よくいっしょに使われるのは組込み関数 `range()` です．  
この関数は引数として `start`，`end`，`step` をとり，それらをもとに整数の数列を作ります．  
その数列を `list()` に渡すと数列のlistを作ることができます．  
いくつか例を見てましょう．  

```python
lst_0_10_1 = list(range(0, 10, 1))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_5_20_2 = list(range(5, 20, 2))   # [5, 7, 9, 11, 13, 15, 17, 19]
lst_m3_3_1 = list(range(-3, 3, 1))   # [-3, -2, -1, 0, 1, 2]
lst_9_m1_m1 = list(range(9, -1, -1)) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

`start`，`end`，`step` の指定の仕方は文字列のスライスと同じです．  
区間は `[start, end)` で，**`end` の数は含まれません**．  
`step` を負数にすると逆順になります．  
`range(start, -1, -1)` で `start` から0まで１ずつカウントダウンするのはよく使うので，慣用的に覚えておくとよいです．  

`end` のみを指定して `start` と `step` を省略すると，`start = 0`，`step = 1` になります．  

```python
lst_0_10_1 = list(range(0, 10, 1))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_x_10_x = list(range(10))         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

(Extra)

### list内包表記 (list Comprehension)

Python 特有の書き方です．  
書式は `[ expression for item in iterable ]` です．  
最初はうへーってなりますが，1 行でいろんな list を作れるので便利です (あと普通に for 文と `append()` を使って list を作るより若干速い)．  
と言いつつ自分は初めてPythonを勉強したときは全然理解できませんでした...
すんなり書けるとめっちゃ気持ちいいです．  
ほかの言語の配列やリストを使うのが面倒になります．  

```python
lst1 = [i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst2 = [2 * i for i in range(10)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

lst3 = [2 ** i for i in range(10)]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

lst4 = ["No." + str(i) for i in range(3)]
# ["No.1", "No.2", "No.3"]
```


多次元listも作ることができます．  

```python
lst1 = [[j for j in range(3)] for i in range(2)]
# [[0, 1, 2], [0, 1, 2]]

lst2 = [[2 * j for j in range(3)] for i in range(2)]
# [[0, 2, 4], [0, 2, 4]]

lst3 = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

multiples = [[i * j for j in range(1, 9)] for i in range(1, 9)]
"""
[[1, 2, 3, 4, 5, 6, 7, 8, 9],
 [2, 4, 6, 8, 10, 12, 14, 16, 18],
 [3, 6, 9, 12, 15, 18, 21, 24, 27],
 [4, 8, 12, 16, 20, 24, 28, 32, 36],
 [5, 10, 15, 20, 25, 30, 35, 40, 45],
 [6, 12, 18, 24, 30, 36, 42, 48, 54],
 [7, 14, 21, 28, 35, 42, 49, 56, 63],
 [8, 16, 24, 32, 40, 48, 56, 64, 72],
 [9, 18, 27, 36, 45, 54, 63, 72, 81]]
"""
```

if文 も使えます．  

```python
evens = [i for i in range(10) if i % 2 == 0]    # [0, 2, 4, 6, 8]
odds = [i for i in range(10) if i % 2 != 0]     # [1, 3, 5, 7, 9]
```

三項演算子も使えます．  

```python
kronecker_delta = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
"""
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
"""
```

複数の入力がある際に使えるlist内包表記を紹介します．  
次のコードでは，3 行の標準入力を読み取って list にし，アンパックしてすぐ使えるようにしています．  
Python では，使う必要のない一時的な変数を慣習的に `_` と書きます．  

```python
"""
入力:
1
2
3
"""
a, b, c = [input() for _ in range(3)]   # 1, 2, 3
```

空白で区切られた3つの数字を標準入力から読み取るコードです．  

```python
# 入力: 1 2 3
a, b, c = [int(i) for i in input().split()]  # 1, 2, 3
```

(ここまで Extra)

## インデックス

str 型と同様に，list のインデックスは 0 番目から始まります．  
`[n]` の書式で，list の n 番目の要素を取得することができます．  
存在しないインデックスを指定するとエラーになります．  

```python
lst1 = [10, 11, 12, 13, 14]

a = lst1[0]    # 10
b = lst1[3]    # 13
c = lst1[-1]   # 14

d = lst1[10]   # IndexError: list index out of range
```

変数と同様に扱えます．  
右辺でインデックスの要素にアクセスする場合は，list の中身は変わりません．   

```python
lst1 = [0, 1, 2, 3, 4]

a = 3 * lst1[2]            # 6
b = lst1[3] ** 2           # 9
c = lst1[4] // lst1[2]    # 2

c += lst1[3]    # 5

print(lst1)     # [0, 1, 2, 3, 4]
```

また，str 型と違い list はミュータブル(=値を変更可能)なので，左辺で `<listオブジェクト>[n]` とすることで n 番目に要素を代入することができます．  

```python
lst1 = [10, 11, 12, 13, 14]

lst1[0] = 100
lst1[3] = 300
lst1[-1] = 400

print(lst1)    # [100, 11, 12, 300, 400]
```

再代入とはラベルを貼り替えることでした．  
上のコードがしていることを図で表すと次のようになります (アドレスは一例です)．  

![list_assignment1](img/list_assignment1.png)

![list_assignment2](img/list_assignment2.png)

この図のように，list はオブジェクトそのものを保持しているわけではなく，オブジェクトの参照を保持しています．  
つまり，例えば `lst[0] = 100` というのは，list が持っている変数 `lst[0]` に代入する (list が持っているラベル `lst[0]` を `100` に割り当てる) ことと同じです．  

list がオブジェクトの参照を保持していることに注意してください．  
次のコードは，変数 lst1 に `[10, 11, 12, 13, 14]` を代入してから変数 lst2 に lst1 を代入しています．  
このとき，lst1 と lst2 は同じ list オブジェクトを指しているので，`lst2[0]` = 100 とすると lst1 も `[100, 11, 12, 13, 14]` になります．  

```python
lst1 = [10, 11, 12, 13, 14]
lst2 = lst1
lst2[0] = 100

print(lst1)    # [100, 11, 12, 13, 14]
print(lst2)    # [100, 11, 12, 13, 14]
```

![list_assignment3](img/list_assignment3.png)

同じ参照を持った異なる list オブジェクトを作るには，変数の代入ではなく list オブジェクトをコピーする必要があります．  
list のコピーについては後述します．  


多次元の場合も次元の数だけ `[]` を重ねることで，同様にして要素の取得，代入が行えます．  

```python
lst_2_3 = [[0, 1, 2], [10, 11, 12]]

a = lst_2_3[0][0]  # 0
b = lst_2_3[0][2]  # 2
c = lst_2_3[1][2]  # 12

lst_2_3[0][0] = 100
lst_2_3[0][2] = 200
lst_2_3[1][2] = 300

print(lst_2_3)   # [[100, 1, 200], [10, 11, 300]]
```


## len()

str 型と同様，list の長さ=要素数も組込み関数 `len()` で計算することができます．  

```python
int_lst = [10, 11, 12, 13, 14, 15]
int_lst_length = len(int_lst)   # 6

empty_lst = []
empty_lst_length = len(empty_lst)   # 0
```

## スライス

str 型と同じように，list でも `[start:end:step]` で要素の抽出が行えます．  
文字列の章でスライスに苦労した方はうんざりするかもしれません(自分も最初はもういいよ...って感じでした)．  
しかし，これほど簡単かつ柔軟に配列の要素を扱える言語はほかにないと思います．  
少しずつ慣れていきましょう．  

```python
lst1 = list(range(10, 20))    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

lst0_4 = lst1[:4]         # [10, 11, 12, 13]
lst0_m1 = lst1[:-1]       # [10, 11, 12, 13, 14, 15, 16, 17, 18]
lst3_7 = lst1[3:7]        # [13, 14, 15, 16]
lst2_9_3 = lst1[2:9:3]    # [12, 15, 18]

even_idx_vals = lst1[::2]  # [10, 12, 14, 16, 18]
odd_idx_vals = lst1[1::2]  # [11, 13, 15, 17, 19]
```

**スライスできない場合は 空 list が返されます**．  

```python
lst1 = list(range(10, 20))    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

lst100_130 = lst1[100:130]    # []
```

`[::-1]` で逆順の list も簡単に作れます．  

```python
lst1 = list(range(10, 20)   # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
lst1_r = lst1[::-1]        # [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
```

`[:]` でコピー(shallow copy)になります．   

```python
lst1 = [0, 1, 2]
lst2 = lst1[:]    # [0, 1, 2]

lst1[0] = 100
print(lst1)    # [100, 1, 2]
print(lst2)    # [0, 1, 2]
```


また，スライスによって複数の要素を一度に代入することもできます．  

```python
lst = [10, 11, 12, 13, 14]
lst[2:4] = [100, 101]
print(lst)  # [10, 11, 100, 101, 14]
```

スライスの要素数 `end - start` が代入する要素数と異なる場合は，代入する要素数が優先されます．  

代入する要素数がスライスの要素数 `end - start` より多い場合は，list の要素数はもとの要素数より多くなります．  

```python
lst = [10, 11, 12, 13, 14]
lst[2:4] = [100, 101, 102, 103]
print(lst)  # [10, 11, 100, 101, 102, 103, 14]
```

代入する要素数がスライスの要素数 `end - start` より少ない場合は，list の要素数はもとの要素数より少なくなります．  

```python
lst = [10, 11, 12, 13, 14]
lst[2:4] = [100]
print(lst)  # [10, 11, 100, 14]
```



## コピー

同じ list オブジェクトを，今の内容のままプログラム中の 2 ヶ所で使いたくなったとします．  
前に見たとおり，ただ別の変数に代入しただけでは，1 ヶ所で list の内容が変更されるともう 1 ヶ所でもその変更が反映されてしまいます．  
これを回避するには，同じ内容を持った list をもう 1 つ新しく作る，つまり list をコピーする必要があります．  

コピーには，shallow copy と deep copy の 2 種類があります．  
shallow copy と deep copy は，list だけでなくオブジェクトの参照を保持するいろいろなオブジェクトに関わってきますが，ここでは list に焦点を当てて話を進めます．  
shallow copy は，もとの list が持つオブジェクトの参照を維持したままもう 1 つの list を作ることをいいます．  
deep copy は，もとの list と， list が持つオブジェクトの参照先のオブジェクトごとコピーすることをいいます．  

list をコピーする方法は 4 種類ありますが，上の 3 つはすべて同じことをします．  

|                書式                |                    説明                     |     種類     |
| :--------------------------------: | :-----------------------------------------: | :----------: |
|      `<list オブジェクト>[:]`      |     スライスの範囲を全要素にしてコピー      | shallow copy |
|    `<list オブジェクト>.copy()`    |  list オブジェクトの copy メソッドでコピー  | shallow copy |
|   `import copy`<br>`copy.copy()`   |   copy モジュールの copy メソッドでコピー   | shallow copy |
| `import copy`<br>`copy.deepcopy()` | copy モジュールの deepcopy メソッドでコピー |  deep copy   |


まずは 1 次元の list をコピーする例を見ていきましょう．  
次のコードでは，変数 lst1 に `[10, 11, 12, 13, 14]` を代入したあと，list オブジェクトの copy メソッドを使って 変数 lst2 に lst1 の shallow copy を代入しています．  
`id()` でメモリのアドレスを見てみると，コピーされた list はもとの list の参照を維持していることがわかります．  
一方，lst1 と lst2 のアドレスは異なっているので，それぞれの変数は別々の list オブジェクトを指していることがわかります．  
これにより， `lst2[0] = 100` としても lst1 の list オブジェクトは `[10, 11, 12, 13, 14]` のままとなっています．  

```python
lst1 = [10, 11, 12, 13, 14]
lst2 = lst1.copy()  # Shallo Copy

print(f"id(lst1)    | {id(lst1)}")      # id(lst1)    | 4440134720
print(f"id(lst1[0]) | {id(lst1[0])}")   # id(lst1[0]) | 4437912288
print(f"id(lst1[1]) | {id(lst1[1])}")   # id(lst1[1]) | 4437912320
print(f"id(lst1[2]) | {id(lst1[2])}")   # id(lst1[2]) | 4437912352

print()

print(f"id(lst2)    | {id(lst2)}")      # id(lst2)    | 4440134336
print(f"id(lst2[0]) | {id(lst2[0])}")   # id(lst2[0]) | 4437912288
print(f"id(lst2[1]) | {id(lst2[1])}")   # id(lst2[1]) | 4437912320
print(f"id(lst2[2]) | {id(lst2[2])}")   # id(lst2[2]) | 4437912352

print()

lst2[0] = 100

print(f"lst1        | {lst1}")          # lst1        | [10, 11, 12]
print(f"lst2        | {lst2}")          # lst2        | [100, 11, 12]

print()

print(f"id(lst1)    | {id(lst1)}")      # id(lst1)    | 4440134720
print(f"id(lst1[0]) | {id(lst1[0])}")   # id(lst1[0]) | 4437912288
print(f"id(lst1[1]) | {id(lst1[1])}")   # id(lst1[1]) | 4437912320
print(f"id(lst1[2]) | {id(lst1[2])}")   # id(lst1[2]) | 4437912352

print()

print(f"id(lst2)    | {id(lst2)}")      # id(lst2)    | 4440134336
print(f"id(lst2[0]) | {id(lst2[0])}")   # id(lst2[0]) | 4437915168
print(f"id(lst2[1]) | {id(lst2[1])}")   # id(lst2[1]) | 4437912320
print(f"id(lst2[2]) | {id(lst2[2])}")   # id(lst2[2]) | 4437912352
```

図にするとこんな感じです．  

![1d_list_copy](img/1d_list_copy.png)

このように，1 次元 list の場合は shallow copy で別々の list が作れます．  

deep copy が必要となるのは，多次元 list のコピーが必要なときです．  

次のコードでは，2 * 2 の 多次元 list を変数 lst3 に代入したあと，shallow copy して変数 lst4 に代入しています．  
lst3 と lst4 のアドレスを見てみると，たしかに lst4 はコピーされた新しい list オブジェクトを指しています．  
しかし，`lst4[0][0]` に 100 を代入したところ，`lst[0][0]` も 100 に変更されてしまっています．  
これは，shallow copy がオブジェクトの参照を維持したままもう 1 つの list を作るからです．  

```python
lst3 = [[10, 11], [20, 21]]
lst4 = lst3.copy()

print(f"id(lst3)       | {id(lst3)}")        # id(lst3)       | 4346513792
print(f"id(lst3[0])    | {id(lst3[0])}")     # id(lst3[0])    | 4345603136
print(f"id(lst3[1])    | {id(lst3[1])}")     # id(lst3[1])    | 4345602752
print(f"id(lst3[0][0]) | {id(lst3[0][0])}")  # id(lst3[0][0]) | 4343380704
print(f"id(lst3[0][1]) | {id(lst3[0][1])}")  # id(lst3[0][1]) | 4343380736
print(f"id(lst3[1][0]) | {id(lst3[1][0])}")  # id(lst3[1][0]) | 4343381024
print(f"id(lst3[1][1]) | {id(lst3[1][1])}")  # id(lst3[1][1]) | 4343381056

print()

print(f"id(lst4)       | {id(lst4)}")        # id(lst4)       | 4346513856
print(f"id(lst4[0])    | {id(lst4[0])}")     # id(lst4[0])    | 4345603136  <- lst3[0] とアドレスが同じ！
print(f"id(lst4[1])    | {id(lst4[1])}")     # id(lst4[1])    | 4345602752  <- lst3[1] とアドレスが同じ！
print(f"id(lst4[0][0]) | {id(lst4[0][0])}")  # id(lst4[0][0]) | 4343380704
print(f"id(lst4[0][1]) | {id(lst4[0][1])}")  # id(lst4[0][1]) | 4343380736
print(f"id(lst4[1][0]) | {id(lst4[1][0])}")  # id(lst4[1][0]) | 4343381024
print(f"id(lst4[1][1]) | {id(lst4[1][1])}")  # id(lst4[1][1]) | 4343381056

print()

lst4[0][0] = 100

print(f"lst3           | {lst3}")            # lst3           | [[100, 11], [20, 21]]    <- lst3 も変更されている！
print(f"lst4           | {lst4}")            # lst4           | [[100, 11], [20, 21]]

print()

print(f"id(lst3)       | {id(lst3)}")        # id(lst3)       | 4346513792
print(f"id(lst3[0])    | {id(lst3[0])}")     # id(lst3[0])    | 4345603136
print(f"id(lst3[1])    | {id(lst3[1])}")     # id(lst3[1])    | 4345602752
print(f"id(lst3[0][0]) | {id(lst3[0][0])}")  # id(lst3[0][0]) | 4343383584
print(f"id(lst3[0][1]) | {id(lst3[0][1])}")  # id(lst3[0][1]) | 4343380736
print(f"id(lst3[1][0]) | {id(lst3[1][0])}")  # id(lst3[1][0]) | 4343381024
print(f"id(lst3[1][1]) | {id(lst3[1][1])}")  # id(lst3[1][1]) | 4343381056

print()

print(f"id(lst4)       | {id(lst4)}")        # id(lst4)       | 4346513856
print(f"id(lst4[0])    | {id(lst4[0])}")     # id(lst4[0])    | 4345603136
print(f"id(lst4[1])    | {id(lst4[1])}")     # id(lst4[1])    | 4345602752
print(f"id(lst4[0][0]) | {id(lst4[0][0])}")  # id(lst4[0][0]) | 4343383584
print(f"id(lst4[0][1]) | {id(lst4[0][1])}")  # id(lst4[0][1]) | 4343380736
print(f"id(lst4[1][0]) | {id(lst4[1][0])}")  # id(lst4[1][0]) | 4343381024
print(f"id(lst4[1][1]) | {id(lst4[1][1])}")  # id(lst4[1][1]) | 4343381056
```

図はこんな感じです (見やすさを優先し，アドレスの順序を一部無視しています)．  
中の list オブジェクトへの参照を維持したままコピーされるため，もとの list と コピーされて作られた list は同じ list オブジェクトを使うことになります．  
その結果，`lst4[0][0] = 100` で `lst3[0][0]` も 100 になってしまったのです．  

![2d_list_shallow_copy](img/2d_list_shallow_copy.png)


これを回避するには，オブジェクトの参照先からまるごとコピーする，すなわち deep copy する必要があります．  
deep copy する場合は，copy モジュールの `deepcopy`メソッド を使います．  
図からもわかるように，内側の list オブジェクトもコピーされているので，`lst4[0][0] = 100` としても lst3 が指す list オブジェクトは何も変更されません．  
(この図も見やすさ重視で一部アドレスの順序を無視しています)  

```python
import copy


lst3 = [[10, 11], [20, 21]]
lst4 = copy.deepcopy(lst3)

print(f"id(lst3)       | {id(lst3)}")        # id(lst3)       | 4451815040
print(f"id(lst3[0])    | {id(lst3[0])}")     # id(lst3[0])    | 4451760832
print(f"id(lst3[1])    | {id(lst3[1])}")     # id(lst3[1])    | 4451820736
print(f"id(lst3[0][0]) | {id(lst3[0][0])}")  # id(lst3[0][0]) | 4448627424
print(f"id(lst3[0][1]) | {id(lst3[0][1])}")  # id(lst3[0][1]) | 4448627456
print(f"id(lst3[1][0]) | {id(lst3[1][0])}")  # id(lst3[1][0]) | 4448627744
print(f"id(lst3[1][1]) | {id(lst3[1][1])}")  # id(lst3[1][1]) | 4448627776

print()

print(f"id(lst4)       | {id(lst4)}")        # id(lst4)       | 4451892992
print(f"id(lst4[0])    | {id(lst4[0])}")     # id(lst4[0])    | 4451892736  <- lst3[0] とアドレスが違う！
print(f"id(lst4[1])    | {id(lst4[1])}")     # id(lst4[1])    | 4451905920  <- lst3[1] とアドレスが違う！
print(f"id(lst4[0][0]) | {id(lst4[0][0])}")  # id(lst4[0][0]) | 4448627424
print(f"id(lst4[0][1]) | {id(lst4[0][1])}")  # id(lst4[0][1]) | 4448627456
print(f"id(lst4[1][0]) | {id(lst4[1][0])}")  # id(lst4[1][0]) | 4448627744
print(f"id(lst4[1][1]) | {id(lst4[1][1])}")  # id(lst4[1][1]) | 4448627776

print()

lst4[0][0] = 100

print(f"lst3           | {lst3}")            # lst3           | [[10, 11], [20, 21]]    <- 変更されてない！
print(f"lst4           | {lst4}")            # lst4           | [[100, 11], [20, 21]]

print()

print(f"id(lst3)       | {id(lst3)}")        # id(lst3)       | 4451815040
print(f"id(lst3[0])    | {id(lst3[0])}")     # id(lst3[0])    | 4451760832
print(f"id(lst3[1])    | {id(lst3[1])}")     # id(lst3[1])    | 4451820736
print(f"id(lst3[0][0]) | {id(lst3[0][0])}")  # id(lst3[0][0]) | 4448627424
print(f"id(lst3[0][1]) | {id(lst3[0][1])}")  # id(lst3[0][1]) | 4448627456
print(f"id(lst3[1][0]) | {id(lst3[1][0])}")  # id(lst3[1][0]) | 4448627744
print(f"id(lst3[1][1]) | {id(lst3[1][1])}")  # id(lst3[1][1]) | 4448627776

print()

print(f"id(lst4)       | {id(lst4)}")        # id(lst4)       | 4451892992
print(f"id(lst4[0])    | {id(lst4[0])}")     # id(lst4[0])    | 4451892736
print(f"id(lst4[1])    | {id(lst4[1])}")     # id(lst4[1])    | 4451905920
print(f"id(lst4[0][0]) | {id(lst4[0][0])}")  # id(lst4[0][0]) | 4448630304
print(f"id(lst4[0][1]) | {id(lst4[0][1])}")  # id(lst4[0][1]) | 4448627456
print(f"id(lst4[1][0]) | {id(lst4[1][0])}")  # id(lst4[1][0]) | 4448627744
print(f"id(lst4[1][1]) | {id(lst4[1][1])}")  # id(lst4[1][1]) | 4448627776
```

![2d_list_deep_copy1](img/2d_list_deep_copy1.png)

![2d_list_deep_copy2](img/2d_list_deep_copy2.png)

このように，多次元の list をはじめ オブジェクトを保持するオブジェクトのコピーには deep copy を使う場面があるということを覚えておいてください．  


## アンパック (Unpack)

list や tuple は，左辺に変数を複数置くことで list を分解して要素を一度に代入することができます．  

```python
lst1 = [10, 11, 12]

a, b, c = lst1
print(a, b, c)    # 10 11 12
```

list を変数と部分 list に分割したい場合は `*` を使います．  
個別に変数化したいものを並べ，`*` をつけた変数を1つ置くことで，残りを `*` のついた変数に list としてまとめることができます．  

```python
lst1 = [10, 11, 12, 13, 14]
a, b, *c = lst1

print(a)    # 10
print(b)    # 11
print(c)    # [12, 13, 14]


x, *y, z = lst1

print(x)    # 10
print(y)    # [11, 12, 13]
print(z)    # 14
```

スライスを使うとこんな感じです．   

```python
lst1 = [10, 11, 12, 13, 14]
a, b = lst1[:2]
c = lst1[2:]
```

tuple の項で説明しますが，次のようにも書けます．   

```python
lst1 = [10, 11, 12, 13, 14]
a, b, c = lst1[0], lst[1], lst[2:]
```


## 加算，乗算

list には加算と乗算の演算が用意されています．  

|     演算子      |                       説明                       |
| :-------------: | :----------------------------------------------: |
| `list1 + list2` | オペランドの **listどうし** を連結したlistを作る |
| `list1 * int1`  |    `list1` を `int1` だけコピーしたlistを作る    |

加算は list どうしのみでできます．  

```python
lst1 = [0, 1, 2, 3, 4]
lst2 = [10, 11, 12]

lst3 = lst1 + lst2    # [0, 1, 2, 3, 4, 10, 11, 12]


lst4 = [0, 1, 2, 3, 4]

lst7 = lst1 + lst2 + lst4
# [0, 1, 2, 3, 4, 10, 11, 12, 100, 101, 102, 103]


lst7 += [1000]
# [0, 1, 2, 3, 4, 10, 11, 12, 100, 101, 102, 103, 1000]
```

乗算は `list1 * int1` の形で，`list1` を `int1` だけコピーした list を作ります．   

```python
lst1 = [0, 1, 2] * 3    # [0, 1, 2, 0, 1, 2, 0, 1, 2]
```


## in

あるオブジェクト x が list に含まれるかどうかは `x in <listオブジェクト>` で確かめられます．  

```python
lst1 = [10, 11, 12, 13, 14]

x1 = 10
if x1 in lst1:
    print("Yes")
else:
    print("No")
# Yes

x2 = 20
if x2 in lst1:
    print("Yes")
else:
    print("No")
# No
```


## list のメソッド

list の代表的なメソッドを紹介します．  

|            メソッド             |                         説明                         |
| :-----------------------------: | :--------------------------------------------------: |
|           `append(x)`           |             `x` を list の末尾に追加する             |
|         `insert(i, x)`          |         インデックス `i` に値 `x` を挿入する         |
|           `remove(x)`           | `x` に等しい要素でインデックスが最小のものを除去する |
|             `pop([i])`             |           list のインデックス `i` の要素を除去して返す．インデックスを指定しなかった場合は末尾の要素を除去して返す            |
|           `index(x)`            |      `x` に等しい要素で最小のインデックスを返す      |
|           `count(x)`            |             引数と同じ値の要素の数を返す             |
| `sort(key=None, reverse=False)` |           要素を **in-place** でソートする           |

## list.append()

`append()` は引数のオブジェクトを list の末尾に追加します．  

```python
lst1 = []
lst1.append(10)    # [10]
lst1.append(11)    # [10, 11]
lst1.append(12)    # [10, 11, 12]
```

## list.index() / list.count()

`index(x)` で，`x` に等しい要素のインデックスを返します．  
複数ある場合は最小のインデックスになります．  

```python
lst1 = [10, 11, 11, 10, 11, 10]

idx11 = lst1.index(11)    # 1
```

`x` に等しい要素がない場合は ValueError になります．  
なので，まず `count(x)` で要素の数を調べ，1以上の場合に使うようにしましょう．  

```python
lsit1 = [10, 11, 11, 10, 11, 10]

cnt12 = lst1.count(12)        # 0
if cnt12 > 0:
    idx12 = lst1.index(12)
else:
    idx12 = -1

print(idx12)    # -1


cnt10 = lst1.count(10)    # 3
if cnt10 > 0:
    idx10 = lst1.index(10)
else:
    idx10 = -1

print(idx10)    # 0
```

(Extra)  
あるいは `try-except` で囲って例外処理をします．  

```python
lst1 = [10, 14, 11, 10,  12, 13]

try:
    idx12 = lst1.index(12)    # ValueError
except ValueError:
    idx12 = -1

print(idx12)    # -1
```
(ここまで Extra)


## list.sort()

`sort()` でlistの要素を昇順にできます．   

```python
lst1 = [10, 14, 11, 10, 12, 13]
lst1.sort()
print(lst1)    # [10, 10, 11, 12, 13, 14]
```

`sort(reverse=True)` とすれば降順でソートできます．  

```python
lst1 = [10, 14, 11, 10, 12, 13]
lst1.sort(reverse=True)
print(lst1)    # [14, 13, 12, 11, 10, 10]
```

`sort()` は **in-place(=その場で)なので，もとの list が変化する** ことに気を付けましょう．  
もとの list を壊したくない場合は，組込み関数 `sorted()` を使います．  

```python
lst1 = [10, 14, 11, 10,  12, 13]

lst2 = sorted(lst1)

print(lst1)    # [10, 14, 11, 10, 12, 13]
print(lst2)    # [10, 10, 11, 12, 13, 14]
```

`sort()` に `key` を渡すといろんな仕方でソートできて楽しいのですが，書くことが多くて煩雑になるのでまた別のところで説明しようと思います．  


## list.insert()

`insert(i, x)` で，`x` を `i`番目に挿入します．   

```python
lst1 = [10, 11, 12]
lst2 = lst1.insert(1, 100)

print(lst1)    # [10, 100, 11, 12]
print(lst2)
```

## list.remove()

`remove(x)` で `x` をlistから除去します．  
同じ値の要素が複数ある場合は，インデックスが最小のものを除去します．  

```python
lst1 = [10, 11, 11, 10, 11, 10]

lst1.remove(11)    # [10, 11, 10, 11, 10]
```


## list.pop()

`append()` と `pop()` を使ってlist をスタックとして扱えます．  

```python
lst1 = [10, 11, 12]

lst1.append(13)
lst1.append(14)

a = lst1.pop()    # 14
b = lst1.pop()    # 13
c = lst1.pop()    # 12

print(lst1)    # [10, 11]
```

インデックスを指定するとそのインデックスの要素を除去して返します．  

```python
lst1 = [10, 11, 12, 13, 14]

lst1.pop(1)
print(lst1)         # [10, 12, 13, 14]

a = lst1.pop(-2)    # 13
print(lst1)         # [10, 12, 14]
```


# tuple (タプル)

list がミュータブルだったのに対し，tuple はイミュータブルです．  
list と tupleは非常によく似ているので，`tuple = 要素を変更できない list` と思ってもらって OK です．  
あんま使わないんでそれさえ覚えてもらえればいいかと．  

下の例は，tuple に代入しようしてエラーになるコードです．  

```python
lst1 = [10, 11, 12, 13, 14]
lst1[2] = 100    # [10, 11, 100, 13, 14]

tpl1 = (10, 11, 12, 13, 14)
tpl1[2] = 100
# TypeError: 'tuple' object does not support item assignment
```

## 初期化

### 要素で初期化

`()` の中に `,`(カンマ)区切りで要素を並べて tuple を作ることができます．  
空タプルは `()` で定義します．  

```python
tpl1 = (10, 11, 12, 13, 14)
tpl2 = (10.9, 11.3, 12.4, 13.0, 14.4)
tpl3 = ("zero", "one", "two", "three", "four")

misc_tpl = (1, "one", [100, 200, 300])
empty_tpl = ()
```

一応 `()` がなくても OK ですが，tuple として扱ってほしい場合は `()` をつける方がわかりやすくていいです．  

```python
tpl1 = 10, 11, 12, 13, 14   # ちょっとわかりにくいかも
```

多次元にもできます．   

```python
tpl_2_3 = (
  (10, 11, 12),
  (20, 21, 22)
)   # 2 x 3

tpl_2_2_3 = (
  (
    (100, 101, 102),
    (110, 111, 112),
  ),
  (
    (200, 201, 202),
    (210, 211, 212)
  )
)   # 2 x 2 x 3

misc_tpl= (
  0, 1, 2,
  (10, 11),
  (
    (100, 101, 102, 103),
    (110, 111, 112, 113)
  )
)
```

### `tuple()` で初期化

list と同様，組込み関数 `tuple()` に iterable オブジェクトを渡すことで tuple を作ることができます．  
list の値を渡したいが値を変えられたくない場合は，list を `tuple()` で tuple 化します．  

```python
tpl_from_lst = tuple([1, 2, 3])   # (1, 2, 3)
tpl_from_dicrionary = list({"name": "Flareon", "type": "Fire"})  # ("name", "type")
```

(Extra)
### tuple 内包表記 ?

list 内包表記はあるんですが，**tuple 内包表記はありません**．  
でも `(expression for item in iterable)` という書式は存在します．  
見た目的に勘違いしやすい(自分は勘違いしてた)のですが，**`(expression for item in iterable)` は Generator(ジェネレータ)内包表記** です．  
ジェネレータは後の章で説明できたらいいんですが，イテレート可能，つまり iterable オブジェクトの 1 つです．  
しかし，generator オブジェクトは 1 回しかイテレートできません．  

次のジェネレータ内包表記で作られるのは，0 から 9 までの整数を 0 から順に 1 つずつ生成する generator オブジェクトです．  

```python
g = (i for i in range(10))
```

generator オブジェクトは iterable オブジェクトの 1 つなので，`tuple()` を使って tuple にできます．  
次の例では，同じ generator オブジェクトを使って 2 つの tuple を作ろうとしています．  
`tpl1` は思った通りに作れましたが，generator オブジェクトがイテレートできるのは 1 回きりなので `tpl2` は空になっています．  

```python
g = (i for i in range(10))

tpl1 = tuple(g)
print(tpl1)     # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

tpl2 = tuple(g)
print(tpl2)     # ()
```

list や tuple が複数の値を持ち，持っている値をイテレートするのに対し，ジェネレータは次の値が必要になったとき動的に値を生成します．  
`i for i in range(10)` という 0 から 9 までの整数を生成するロジックだけを保持しておき，必要になったときにそのロジックに従って値を生成するといったイメージですかね．  
そのため，メモリに乗り切らない大量のデータを処理するときや遅延評価が必要なときに使用されます．  

(ここまで Extra)


## アンパック

listと同様，tupleもアンパックできます．  

```python
tpl = (10, 11, 12)
a, b, c = tpl

print(a)    # 10
print(b)    # 11
print(c)    # 12
```

tupleの定義とアンパックを使用すると，複数の変数に一度に値を代入することができます．  

```python
a, b, c = 10, 11, 12

print(a)    # 10
print(b)    # 11
print(c)    # 12
```

上の例でしていることは次のことと同じです．  

```python
a, b, c = (10, 11, 12)
```

また，これを応用して2変数の値を簡単に入れ替えることができます．  

```python
a = 1
b = 2

a, b = b, a

print(a)    # 2
print(b)    # 1
```

## インデックス

要素は読み取ることができますが，代入することはできません．  

```python
tpl = (10, 11, 12, 13, 14)

a = tpl[2]    # 12

tpl[3] = 100
# TypeError: 'tuple' object does not support item assignment
```

## len()

`len()` で要素数を計算できます．  

```python
tpl = [10, 11, 12, 13, 14, 15]
tpl_length = len(tpl)   # 6

empty_tpl = (, )
empty_tpl_length = len(empty_tpl)   # 0
```


# dict (辞書)

Pythonには，keyとvalueのペアを複数保持するデータ構造として dict (辞書) があります．  
同様のデータ構造は，ほかの言語では Map という名称が多いです．  
見た目的には以下のようになります．  
key には，一意であればどんなオブジェクトでも指定できます(正確には hash値 が計算可能なオブジェクト)．  

```python
dct1 = {
    1: "one",
    2: "two",
    3: "three"
}

dct2 = {
    "one": 1,
    "two": 2,
    "three": 3
}

dct3 = {
  "evens": [0, 2, 4, 6, 8],
  "odds": [1, 3, 5, 7, 9]
}

dct4 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

empty_dct = {}
```

dict も多次元にできます．  

```python
dct1 = {
    "Vapareon": {
        "number": 134,
        "type": "Water"
    },
    "Jolteon": {
        "number": 135,
        "type": "Electric"
    },
    "Flareon": {
        "number": 136,
        "type": "Fire"
    }
}
```

## 初期化

dictも複数の初期化方法を持っています．  

### 要素で初期化

先ほどの例にもあったように，`{key: value, key: value, ... }` の書式で値を定義します．  

```python
dct1 = {
    "name": "Flareon",
    "type": "Fire"
}
```

### `dict()` で初期化

組込み関数 `dict()` を使用してdictを作ります．  
次の例は，引数としてtupleのlistを渡しています．  

```python
dct1 = dict([("name", "Flareon"), ("type", "Fire")])

print(dct1)
"""
{
    "name": "Flareon",
    "type": "Fire"
}
"""
```

キーワード引数で key と value を指定することもできます．  
キーボード引数については関数の章で紹介します．  

```python
dct1 = dict(name="Flareon", type="Fire")

print(dct1)
"""
{
    "name": "Flareon",
    "type": "Fire"
}
"""
```

(Extra)

### dict内包表記

list, Generator に並んで dict にも内包表記があります．  
書式は `{ key: value for items in iterable }` です．
key と value のペアがある分ちょっと複雑です．  

```python
dct1 = {i: i * i for i in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

dct2 = {s: len(s) for s in ("Eevee", "Vapareon", "Jolteon", "Flareon")}
"""
{
    "Eevee": 5,
    "Flareon": 7,
    "Jolteon": 7,
    "Vapareon": 8
}
"""

dct3 = {k: v for k, v in (("name", "Flareon"), ("number", 136), ("type", "Fire"))}
"""
{
    "name": "Flareon",
    "number": 136,
    "type": "Fire"
}
"""
```

### value の取得

`<dictオブジェクト>[key]` で key に対応した value を取得することができます．  
存在しない key の value を取得しようとするとエラーになります．   


```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

a = dct1["Vapareon"]   # Water
b = dct1["Espeon"]     # KeyError: 'Espeon'


dct2 = {
    "Vapareon": {
        "number": 134,
        "type": "Water"
    },
    "Jolteon": {
        "number": 135,
        "type": "Electric"
    },
    "Flareon": {
        "number": 136,
        "type": "Fire"
    }
}

c = dct2["Vapareon"]["number"]   # 134
d = dct2["Vapareon"]["weight"]   # KeyError: 'weight'
```

また，左辺で `<dictオブジェクト>[key]` を使うことで，key に対応した value を代入できます．  
存在しない key を指定した場合は，key と value のペアが新しく追加されます．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

dct1["Jolteon"] = "でんき"   # key を指定して値を更新
dct1["Espeon"] = "エスパー"  # 新しく key と value を追加
print(dct1)
"""
{
    "Vapareon": "Water",
    "Jolteon": "でんき",
    "Flareon": "Fire",
    "Espeon": "エスパー"
}
"""


dct2 = {
    "Vapareon": {
        "number": 134,
        "type": "Water"
    },
    "Jolteon": {
        "number": 135,
        "type": "Electric"
    },
    "Flareon": {
        "number": 136,
        "type": "Fire"
    }
}

dct2["Vapareon"]["type"] = "みず"
dct2["Vapareon"]["weight"] = 29.0
dct2["Espeon"] = {
    "number": 196,
    "type": "エスパー"
}

print(dct2)
"""
{
    "Vapareon": {
        "number": 134,
        "type": "みず",
        "weight": 29.0
    },
    "Jolteon": {
        "number": 135,
        "type": "Electric"
    },
    "Flareon": {
        "number": 136,
        "type": "Fire"
    },
    "Espeon": {
        "number": 196,
        "type": "エスパー"
    }
}
"""
```

ちなみに dict では `[n]` とすると n が key として解釈されるので，list や tuple のようにインデックスで値を取得することはできません．  

### len()

`len()` で key, value のペアの数を計算できます．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}
print(len(dct1))    # 3

empty_dct = {}
print(len(empty_dct))    # 0
```

## in

あるオブジェクト x が dict の **key に存在するか** は `x in <dictオブジェクト>` で確かめられます．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

x1 = "Flareon"
if x1 in dct1:
    print("Yes")
else:
    print("No")
# Yes

x2 = "Espeon"
if x2 in dct1:
    print("Yes")
else:
    print("No")
# No
```

また，あるオブジェクト x が dict の **value に存在するか** は `x in <dictオブジェクト>.values()` で確かめられます．  
`values()` は dictオブジェクト のすべての value を dictviewオブジェクト で返します．  
dictviewオブジェクトはイミュータブルで，名前の通り値を見るだけ用のオブジェクトです．

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

x1 = "Fire"
if x1 in dct1:
    print("Yes")
else:
    print("No")
# Yes

x2 = "でんき"
if x2 in dct1:
    print("Yes")
else:
    print("No")
# No
```

### dict のメソッド

dict に使用できる主なメソッドを紹介します．  

|         メソッド         |                                                           説明                                                           |
| :----------------------: | :----------------------------------------------------------------------------------------------------------------------: |
|  get(key, default=None)  | key に対応する value を返す．key が存在しなければ default で指定された値を返す．default に何も指定しなければ None を返す |
|   dict1.update(dict2)    |                 dict1 に dict2 を連結する．重複する key の value は dict2 の value に更新(update)される                  |
| setdefault(key, default) |               key に対応する value を返す．key が存在しなければ value に defaut をセットして value を返す                |
|          keys()          |                                       すべての key を dictviewオブジェクト で返す                                        |
|         values()         |                                      すべての value を dictviewオブジェクト で返す                                       |
|         items()          |                                 すべての key, value のペアを dictviewオブジェクト で返す                                 |


## dict.get()

`<dictオブジェクト>[key]` で key に紐づいた value を取得できますが，存在しない key を指定した場合は `KeyError` になるのでした．  
`get(key, default=x)` で，key が存在しない場合は default に指定した値を返すようにすることで，より安全に value を取得することができます．  
ケースによって key が存在したり存在しなかったりする dict を扱う際に重宝します．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

a = dct1.get("Vapareon", "Unknown")  # Water
b = dct1.get("Espeon", "Unknown")    # Unknown
```


## dict.update()

`dict1.update(dict2)` で，dict1 に dict2 を連結します．  
重複する key の value は dict2 の value に更新(update)されます．  
既存の dict の value をまとめて更新したいときや，複数の dict を1つにまとめたいときに使います．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

dct2 = {
    "Flareon": "ほのお",
    "Umbreon": "あく",
    "Espeon": "エスパー"
}

dct1.update(dct2)
print(dct1)
"""
{
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "ほのお",    <- 更新
    "Umbreon": "あく",      <- 新規追加
    "Espeon": "エスパー"     <- 新規追加
}
"""
```

(Extra)  

## dict.setdefault()

`setdefault(key, default)` は，key が存在すればその value を返し，存在しなければ新しく key と default のペアを dict に追加して，value(=default) を返します．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

a = dct1.setdefault("Vapareon", "Water")
print(a)  # Water

b = dct1.setdefault("Espeon", "Phychic")
print(b)  # Phychic
print(dct1)
"""
{
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}
"""
```

使用例は練習問題を参考にしてください．  
(ここまで Extra)


## dict.keys()

`keys()`, `values()`, `items()` は，後述するfor文とともによく使用されるメソッドです．  

`keys()` で dict のもつすべての key を取得できます．  
返り値は dictviewオブジェクト なのでそのままだと値は変更できません．  
list として使用したい場合は `list()` で listオブジェクト にできます．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

keys = dct1.keys()
print(keys)       # dict_keys(['Vapareon', 'Jolteon', 'Flareon'])

key_lst = list(keys)
print(key_lst)   # ['Vapareon', 'Jolteon', 'Flareon']
```


## dict.values()

`values()` で dict のもつすべての value を取得できます．  
`keys()` と同様，返り値は dictviewオブジェクト です．  
`list()` で list化できます．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

values = dct1.values()
print(values)         # dict_values(['Water', 'Electric', 'Fire'])

value_lst = list(values)
print(value_lst)     # ['Water', 'Electric', 'Fire']
```


## dict.items()

`items()` で dict のもつすべての key, value のペアを取得できます．  
返り値は dictviewオブジェクト で，1つ1つのペアは tuple になっています．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

items = dct1.items()
print(items)
# dict_items([('Vapareon', 'Water'), ('Jolteon', 'Electric'), ('Flareon', 'Fire')])
```


# for文

Pythonにおけるfor文は list や tuple，dict といった iterableオブジェクト の要素を1つ1つ取り出す(処理を繰り返す=イテレート(iterate))構文です．  
ほかの言語を知っている方は，拡張for文をイメージするとわかりやすいと思います．  
書式は次の通りです．  

![for_format](img/for_format.png)

次の例は，list の要素を1つずつ取り出して出力するコードです．  

```python
lst1 = [10, 11, 12, 13, 14]
for n in lst1:
    print(n)
"""
10
11
12
13
14
"""

lst2 = ["Vapareon", "Jolteon", "Flareon"]
for s in lst2:
    print(s)
"""
Vapareon
Jolteon
Flareon
"""

lst3 = [[100, 101, 102], [200, 201, 202], [300, 301, 302], [400, 401, 402]]
for inner_lst in lst3:
    print(inner_lst)
"""
[100, 101, 102]
[200, 201, 202]
[300, 301, 302]
[400, 401, 402]
"""

lst4 = [{"Vapareon": "Water"}, {"Jolteon": "Electric"}, {"Flareon": "Fire"}]
for d in lst4:
    print(d)
"""
{'Vapareon': 'Water'}
{'Jolteon': 'Electric'}
{'Flareon': 'Fire'}
"""
```

変数を複数置くことで，for文で取り出された要素をアンパックすることができます．  

```python
lst3 = [[100, 101, 102], [200, 201, 202], [300, 301, 302], [400, 401, 402]]

for a, b, c in lst3:
    print(a, b, c)
"""
100 101 102
200 201 202
300 301 302
400 401 402
"""
```

要素を逆順で取得したい場合はスライス `[::-1]` を使用します．  

```python
lst1 = [10, 11, 12, 13, 14]
for n in lst1[::-1]:
    print(n)
"""
14
13
12
11
10
"""
```

tuple も list と同じようにfor文が使えます．  

dict をそのままfor文で回すと，すべての key が取り出されます．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

for k in dct1:
    print(k)
"""
Vapareon
Jolteon
Flareon
"""
```

すべての value をfor文で回すには `values()` を使います．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

for v in dct1.values():
    print(v)
"""
Water
Electric
Fire
"""
```

for文で key と value をいっしょに取り出す場合は `items()` を使います．  

```python
dct1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

for k, v in dct1.items():
    print(k, v)
"""
Vapareon Water
Jolteon Electric
Flareon Fire
"""
```

## range()

組込み関数 `range()` は for文 とともによく使われます．  
`list()` のところでも説明しましたが，`range(start, end, step)` で，`step` が正の場合は `start` 以上 `end` 未満 の整数を，`step` が負の場合は `start` 以下で `end` より大きい整数を，それぞれステップ数 `step` で順に並べた数列(rangeオブジェクト)を返します．  
**`end` で指定した数は含まれない** ことに注意してください．  
`end` のみを指定した場合は `start = 0`，`step = 1` となります．  

例えば，0から9までをカウントアップする場合は for文 と `range()` を使って次のようにします．  

```python
for i in range(0, 10, 1):
    print(i)
"""
0
1
2
3
4
5
6
7
8
9
"""
```

`end` のみを指定し， `start` と `step` を省略すると次のように書けます．  

```python
for i in range(10):
    print(i)
```

`start = 0`, `end = 10`, `step = 2` とした場合は以下のようになります．  

```python
for i in range(0, 10, 2):
    print(i)
"""
0
2
4
6
8
"""
```

次の例は，`start = 9`，`end = -1`，`step = -1` とした場合です．  

```python
for i in range(9, -1, -1):
    print(i)
"""
9
8
7
6
5
4
3
2
1
0
"""
```

list の要素にインデックスでアクセスし，要素を書き換える場合にもよく使用します．  
次のコードは，list のすべての要素を 2倍 します．  

```python
lst1 = [10, 11, 12, 13, 14]

for i in range(len(lst1)):
    lst1[i] *= 2

print(lst1)    # [20, 22, 24, 26, 28]
```


次のプログラムは，for文 を使って list の中で最小値をとる要素を探して出力します．  
Python には list や tuple などの iterableオブジェクト を与えるとその中の最小値を返す `min()` という便利な組込み関数があります (ほかにも `max()` や `sum()` といった関数もあります．これらは組込み関数の章でまとめて紹介します)．  
しかし，list などのデータ構造の中から条件に合致した要素を探索するコードを書く際の基礎になるので，自分で書けるようにしておくいいと思います．  

```python
lst = [12, 11, 10, 13, 12, 10]

min_n = lst[0]
for n in lst[1:]:
    if n < min_n:
        min_n = n
print(min_n)    # 10
```


## enumerate()

`enumerate()` (enumerate = 列挙する) は，iterableオブジェクト の要素とインデックス(あるいは順序数)をfor文で同時に回したいときに使用する組込み関数です．  

これまで見た例のように，for文は iterableオブジェクト は要素のみを回し，インデックスが必要な場合は `range()` を使っていました．  

```python
lst1 = [10, 11, 12, 13, 14]

# 要素を順に取得する
for n in lst1:
    print(n)

# インデックスに相当する数列を回す
for i in range(len(lst1)):
    print(i)
```

この2つを合わせた機能をもつのが `enumerate()` です．  
enumerateメソッドは，順序数と引数で与えられた iterableオブジェクト の要素のペアを1つずつ tuple にした enumerateオブジェクト を返します．  
for文ではその tuple を1つずつ取り出すので，for文中に変数を `順序数, 要素` の順に置いてアンパックして使用します．  

```python
for i, n in enumerate(lst1):
    print(f"lst1[{i}]={n}")
"""
lst1[0]=10
lst1[1]=11
lst1[2]=12
lst1[3]=13
lst1[4]=14
"""
```

要素とペアにする整数は0始まり以外にも可能です．  
引数に `start` (デフォルトは0) を指定すると，その整数から1ずつカウントアップされていきます．

次の例では，順序数を1から開始しています．  
引数の順序と変数の順序がクロスしていて紛らわしいので注意しましょう．  

```python
for i, n in enumerate(lst1, 1):
    print(f"i={i}, n={n}")
"""
i=1, n=10
i=2, n=11
i=3, n=12
i=4, n=13
i=5, n=14
"""
```

## ネスト

if文 や while文 と同様に，for文 もネストすることができます．  
次のコードは，内側と外側の `range()` で 1 から 9 までの数列を 2つ 作り，それぞれの数を掛け合わせることで九九の表を出力します．  

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, "", end="")
    print()
"""
1 2 3 4 5 6 7 8 9 
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36 
5 10 15 20 25 30 35 40 45 
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81 
"""
```

2次元以上のデータ構造は，for文 を重ねることで要素を列挙できます．  
次のプログラムでは，2次元list の要素を順に出力しています．  

```python
lst = [
    [100, 101, 102],
    [200, 201],
    [],
    [400, 401, 402, 403]
]

for inner_lst in lst:
    for n in inner_lst:
        print(n, "", end="")
    print()
"""
100 101 102 
200 201 

400 401 402 403 
"""
```

## break文

for文 でもループから抜けるために break文 が使えます．  
次の例は，3 の累乗のうち余りが 1 から 7 になるものの累乗の数を，for文 を回して探しています．  
内側の for文 で 3 の `j`乗 を計算し，7 で割った余りが外側のループで探している余りに一致した場合は break文 ですぐ拔けるようになっています．  
if文，while文 と同様，変数のスコープが後ろに続いているため，break文 で抜けたあとも 変数`j` が使えることに注意してください．  

```python
# 3 は 7 の原始根
for i in range(1, 8):
    for j in range(10):
        if (3 ** j) % 7 == i:
            break
    print(f"3^{j} mod 7 = {i}")
"""
3^0 mod 7 = 1
3^2 mod 7 = 2
3^1 mod 7 = 3
3^4 mod 7 = 4
3^5 mod 7 = 5
3^3 mod 7 = 6
3^9 mod 7 = 7
"""
```


## continue文

for文 でも continue文 が使用できます．  

<hr>

最後に，後回しにした項目 (listの初期化) の確認をお願いします．  

とても長くなってしまった...  
list の shallow copy らへんの話がちょっと説明不足ですかね...  
関数の章でも関連してくるので，そこでまとめて詳しく書こうと思います．  


# 練習問題


## Q 1

for文を使って次のような数列を出力してください．  

```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8 9 
```

## Q 2

for文 を使って次の list の要素の和を求めてみましょう．  

```python
lst = [475, 358, -160, -385, 173, 148, 128, -265, -472, -82, 289, -465, 365, 248, 180, 451, 158, 51, 431, -6]
```


## Q 3

for文 を使って次の list の最大値を求め，出力してみましょう．  

```python
lst = [321, -325, 313, -452, 342, 281, -237, -322, 103, 143, 345, -349, -293, 487, 494, -23, 319, -154, -5, -95]
```

## Q 4

次の list で最大値をとる要素の **インデックス** を出力してください．  
最大値をとる要素が複数ある場合は，最小のインデックスを出力してください．  

```python
lst = [131, 101, 79, 134, 83, 146, 78, 143, 140, 61, 92, 56, 76, 77, 146, 58, 137, 126, 85, 82]
```

## Q 5

for文を使って 7 の階乗(`7! = 7 * 6 * 5 * 4 * 3 * 2 * 1`)を計算してみましょう．  


## Q 6

袋の中に玉が 7 個入っています．  
玉には 1 から 7 までの整数が 1 つ書かれており，数字に重複はありません．  
袋の中から玉を同時に 3 個取り出したとき，3 個の玉に書かれている数字の組合せは何通りあるでしょうか．  
Python で計算してみましょう．  


## Q 7

次の dict の key と value を入れ替えた dict を作ってください．  
なお，作成する dict の key の順序は問いません．  

```python
e2j_dct = {
    "Vapareon": "シャワーズ",
    "Jolteon": "サンダース",
    "Flareon": "ブースター",
    "Espeon": "エーフィ",
    "Umbreon": "ブラッキー"
}
```


## Q 8

サイバー攻撃の `カテゴリ名` が次の dict で与えられます．  
各 `カテゴリ名` には `カテゴリID` が割り振られており，`カテゴリID` から `カテゴリ名` を一意に特定できるようになっています．  
dict は `{ カテゴリID : カテゴリ名 }` の対応を表しています．  

```python
category_dct = {
    "TA0001": "Initial Access",
    "TA0002": "Execution",
    "TA0003": "Persistence",
}
```

セキュリティアラートのデータが list として次のように取得できました．  
しかし，各アラートデータの `category` の値は `カテゴリID` となっています．  
人が読むには不便なので，すべてのアラートデータの `category` を `カテゴリ名` に更新して出力してください．  
また，`category_dct` に存在しない `カテゴリID` の場合は `カテゴリ名` を `Unknown` に更新してください．  

```python
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
        "category": "TA0004",
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
```

なお，`pprint` モジュールの `pprint` メソッドで出力を整形できます．  
使い方は普通の `print()` と同じで， `pprint(data_lst)` で出力できます．  
`pprint` メソッドを使えるようにするため，次のコードをファイルの先頭にコピペしてください．  

```python
from pprint import pprint
```

期待される出力は次のとおりです (dict の key の順序は問いません)．  

```
[{'category': 'Execution',
  'datetime': '2020-08-15 20:10:43',
  'severity': 'Middle'},
 {'category': 'Persistence',
  'datetime': '2020-08-16 09:11:41',
  'severity': 'Low'},
 {'category': 'Persistence',
  'datetime': '2020-08-16 10:27:30',
  'severity': 'Low'},
 {'category': 'Unknown',
  'datetime': '2020-08-16 21:02:56',
  'severity': 'Middle'},
 {'category': 'Initial Access',
  'datetime': '2020-08-17 08:30:17',
  'severity': 'High'},
 {'category': 'Execution',
  'datetime': '2020-08-17 10:34:49',
  'severity': 'Low'}]
```


## Q 9

各言語で使用されるライブラリやフレームワークの名前が，次の list にまとめられています．  
言語ごとにライブラリ名・フレームワーク名を dict でまとめ，出力してください．  
出力は `pprint` で整形してください．  

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
```

期待される出力は次のとおりです．  
なお，出力する dict の key の順序は問いません．  

```
{'C++': ['Boost'],
 'Java': ['Lombok'],
 'JavaScript': ['React', 'Deno'],
 'Python': ['Pandas', 'NumPy']}
```

## Q 10

Satoshi，Kasumi，Takeshi の， TOEIC のセクション別スコアが次の dict で与えられます．  
各セクションについて3人の平均スコアを求め，dict にまとめて出力してください．  
出力は `pprint` メソッドを使用して整形してください．  

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
```

期待される出力は次のとおりです．

```
{'Listening': 243.33333333333334,
 'Reading': 318.3333333333333,
 'Speaking': 165.0,
 'Writing': 88.33333333333333}
```


(Extra)


## Q 11

次の行列の積を求めてみましょう．  

![Q_matrix](img/Q_matrix.png)

```python
A = [[2, 0, 8, 7], [2, 4, 8, 3], [9, 0, 4, 3]]
B = [[9, 9, 8, 0, 4], [5, 1, 5, 3, 8], [3, 6, 4, 1, 9], [8, 5, 5, 3, 3]]
```

期待される出力は次の通りです．  

```
[[ 98 101  83  29 101]
 [ 86  85  83  29 121]
 [117 120 103  13  81]]
```


<hr>

[Chapter 4 練習問題解答例](Answers4.md)  
[Index](../README.md)

