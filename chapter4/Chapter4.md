# Chapter4 基本データ構造

# 基本データ構造

この章では，複数の値を保持するために使用される基本的なデータ構造を導入します．  
具体的には以下になります．  

|       名前        |                 説明                 |                  例                   |               特徴                |
| :---------------: | :----------------------------------: | :-----------------------------------: | :-------------------------------: |
|       List        |          複数のデータを格納          |              `[1, 2, 3]`              |    ミュータブル(値を変更可能)     |
|  Tuple (タプル)   |          複数のデータを格納          |              `(1, 2, 3)`              | イミュータブル (値を変更できない) |
| Dictionary(=辞書) | key, valueのペアで複数のデータを格納 | `{"name": "Flareon", "type": "Fire"}` |           ミュータブル            |

<br>

# List

例を見てわかる通り，複数の値を保持するデータ構造です．  
ほかの言語では配列にあたりますが，PythonのListにはint型でもstr型でもなんでも格納できます．  

```python
int_list = [10, 11, 12, 13, 14, 15]
float_list = [3.1, -6.2, -190.2, 66.7]
str_list = ["Eevee", "Vaporeon", "Jolteon", "Flareon"]
bool_list = [True, False, True]
misc_list = [10, 3.1, "Eevee"]
empty_list = []
```

多次元にもできます．  

```python
list_2_3 = [
  [10, 11, 12],
  [20, 21, 22]
]   # 2 x 3

list_2_2_3 = [
  [
    [100, 101, 102],
    [110, 111, 112],
  ],
  [
    [200, 201, 202],
    [210, 211, 212]
  ]
]   # 2 x 2 x 3

misc_list = [
  0, 1, 2,
  [10, 11],
  [
    [100, 101, 102, 103],
    [110, 111, 112, 113]
  ]
]
```


## 初期化

Listの初期化にはいろいろな方法があります．  
後から参照しやすいよう各ケースごとにまとめようとした分ちょっと詰め込みすぎてしまったので，途中で飽きた場合はインデックスの項目に進んでもらってもOKです．  
わからなくなったり忘れたりしたらここを探してみてください．  

### 要素で初期化

これまでの例のように，`[]`の中に要素を `,`(カンマ) で区切って羅列することで，それらの要素を含んだListオブジェクト(=List型の具体物のこと．int型の値などとは違ってList型の値とは呼べないのでオブジェクトと呼ぶことにしましょう)が作れます．  
`[]` の中に何も要素を入れない場合は空リストになります．  

```python
int_list = [10, 11, 12, 13, 14, 15]
empty_list = []
```

同じ値の複数個の要素で初期化する場合は `*`演算子で要素を繰り返して生成することができます．(`*`演算子は初期化以外のときでもListをコピーするために使用できます)

```python
ones = [1] * 5    # [1, 1, 1, 1, 1]
one_two_threes = [1, 2, 3] * 3    # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

(以下はList内包表記，オフセットの項目のあとに読んでください)  
多次元Listの初期化に `*` を使う場合には注意が必要です．  
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

理由は，`*` によるListのコピーが浅いコピー(Shallow Copy)であり，リスト`x[0]`，`x[1]`， `x[2]` がすべて同じ要素を参照しているからです．  
回避案としては，最も内側のListだけを `*` で生成し，残りをList内包表記で書けば，`*` に準ずる簡潔さでListを作れます．  

```python
x = [[0] * 2 for _ in range(3)]   # [[0, 0], [0, 0], [0, 0]]
x[0][0] = 1
print(x)    # [[1, 0], [0, 0], [0, 0]]
```

(ここまで後回し)

### `list()`で初期化

組込み関数 `list()` にIterableオブジェクトを与えることでListを作成します．  
Iterable(=反復可能=要素を順々に辿ることのできる)オブジェクトとはTupleやDictionaryなどのオブジェクトのことをいいます．  
ListオブジェクトもIterableオブジェクトです．  
とりあえず値がいっぱい並んでる感じのは大体そうです．  

`list()` を使って，TupleやDictionaryオブジェクトからListオブジェクトを作れます．  
Tupleはイミュータブル(=値を変更できない)ですが，Listはミュータブル(=値を変更可能)です．  
また，Dicrionaryを引数として与えると全てのkeyのListが作られます．  

```python
list_from_tuple = list((1, 2, 3))   # [1, 2, 3]
list_from_dicrionary = list({"name": "Flareon", "type": "Fire"})  # ["name", "type"]
```

文字列(=strオブジェクト)もListにできます．  

```python
list_from_str = list("一文字ずつ要素になります．")
# ['一', '文', '字', 'ず', 'つ', '要', '素', 'に', 'な', 'り', 'ま', 'す', '．']
```

よくいっしょに使われるのは組込み関数 `range()` です．  
この関数は引数として `start`，`end`，`step` をとり，それらをもとに整数の数列を作ります．  
その数列を `list()` に渡すと数列のListを作ることができます．  
いくつか例を見てましょう．  

```python
list_0_10_1 = list(range(0, 10, 1))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_5_20_2 = list(range(5, 20, 2))   # [5, 7, 9, 11, 13, 15, 17, 19]
list_m3_3_1 = list(range(-3, 3, 1))   # [-3, -2, -1, 0, 1, 2]
list_9_m1_m1 = list(range(9, -1, -1)) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

`start`，`end`，`step` の指定の仕方は文字列のスライスと同じです．  
区間は `[start, end)` で，**`end` の数は含まれません**．  
`step` を負数にすると逆順になります．  
`range(start, -1, -1)` で `start` から0まで１ずつカウントダウンするのはよく使うので覚えておくとよいです．  

`start` を省略すると `start = 0`， `step` を省略すると `step = 1` になります．  

```python
list_0_10_1 = list(range(0, 10, 1))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_x_10_1 = list(range(10, 1))      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_x_10_x = list(range(10))         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

(Extra)

### List内包表記 (List Comprehension)

Python特有の書き方です．  
書式は `[ expression for item in iterable ]` です．  
最初はうへーってなりますが，1行でいろんなリストを作れるので便利です．  
と言いつつ自分は初めてPythonを勉強したときは理解できなくて飛ばしました．  
なぜこんな書き方ができるのかとかあんまり深いことは考えずに，丸暗記して慣れることをおすすめします．  

```python
list1 = [i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list2 = [2 * i for i in range(10)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

list3 = [2 ** i for i in range(10)]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

list4 = ["No." + str(i) for i in range(3)]
# ["No.1", "No.2", "No.3"]
```


多次元Listも作ることができます．  

```python
list1 = [[j for j in range(3)] for i in range(2)]
# [[0, 1, 2], [0, 1, 2]]

list2 = [[2 * j for j in range(3)] for i in range(2)]
# [[0, 2, 4], [0, 2, 4]]

list3 = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

multiples = [[i * j for j in range(1, 9)] for i in range(1, 9)]
'''
[[1, 2, 3, 4, 5, 6, 7, 8, 9],
 [2, 4, 6, 8, 10, 12, 14, 16, 18],
 [3, 6, 9, 12, 15, 18, 21, 24, 27],
 [4, 8, 12, 16, 20, 24, 28, 32, 36],
 [5, 10, 15, 20, 25, 30, 35, 40, 45],
 [6, 12, 18, 24, 30, 36, 42, 48, 54],
 [7, 14, 21, 28, 35, 42, 49, 56, 63],
 [8, 16, 24, 32, 40, 48, 56, 64, 72],
 [9, 18, 27, 36, 45, 54, 63, 72, 81]]
'''
```

if文も使えます．  

```python
evens = [i for i in range(10) if i % 2 == 0]    # [0, 2, 4, 6, 8]
odds = [i for i in range(10) if i % 2 != 0]       # [1, 3, 5, 7, 9]
```

三項演算子も使えます．  

```python
kronecker_delta = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
'''
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
'''
```

練習問題で複数の入力がある際に使えるList内包表記を紹介します．  
次のコードでは，3行の標準入力を読み取ってListにし，アンパックしてすぐ使えるようにしています． 
Pythonでは，使う必要のない一時的な変数を慣習的に `_` と書きます．

```python
a, b, c = [input() for _ in range(3)]
```

空白で区切られた3つの数字を標準入力から読み取るコードです．  

```python
a, b, c = [str(i) for i input().split()]
```

(ここまでExtra)

## インデックス

str型と同様に，Listのインデックスは0番目から始まります．  
`[n]` の書式で，Listのn番目の要素を取得することができます．  

```python
list1 = [0, 1, 2, 3, 4]

a = list1[0]    # 0
b = list1[3]    # 3
c = list1[-1]    # 5
```

変数と同様に扱えます．  
右辺でインデックスの要素にアクセスする場合は，Listの中身は変わりません．   

```python
list1 = [0, 1, 2, 3, 4]

a = 3 * list1[2]    # 6
b = list1[3] ** 2    # 9
c = list1[4] // list1[2]    # 2

c += list1[3]    # 5

print(list1)    # [0, 1, 2, 3, 4]
```

また，str型と違いListはミュータブル(=値を変更可能)なので，左辺で `<Listオブジェクト>[n]` とすることでn番目に要素を代入することができます．  

```python
list1 = [0, 1, 2, 3, 4]

list1[0] = 10
list1[3] = 30
list1[-1] = 40

print(list1)    # [10, 1, 2, 30, 40]
```

多次元の場合も次元の数だけ `[]` を重ねることで，同様にして要素の取得，代入が行えます．  

```python
list_2_3 = [[0, 1, 2], [10, 11, 12]]

a = list_2_3[0][0]  # 0
b = list_2_3[0][2]  # 2
c = list_2_3[1][2]  # 12

list_2_3[0][0] = 100
list_2_3[0][2] = 200
list_2_3[1][2] = 300

print(list_2_3)   # [[100, 1, 200], [10, 11, 300]]
```


## len()

str型と同様，Listの長さ=要素数も組込み関数 `len()` で計算することができます．  

```python
int_list = [10, 11, 12, 13, 14, 15]
int_list_length = len(int_list)   # 6

empty_list = []
empty_list_length = len(empty_list)   # 0
```

## スライス

str型と同じように，Listでも `[start:end:step]` で要素の抽出が行えます．  
文字列の章でスライスに苦労した方はうんざりするかもしれません(自分も最初はまたかよ...って感じでした)．
しかし，これほど簡単かつ柔軟に配列の要素を扱える言語はほかにありません．  
少しずつ慣れていきましょう．  

```python
list1 = list(range(10, 20))    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

list0_4 = list1[:4]         # [10, 11, 12, 13]
list0_m1 = list1[:-1]       # [10, 11, 12, 13, 14, 15, 16, 17, 18]
list3_7 = list1[3:7]        # [13, 14, 15, 16]
list2_9_3 = list1[2:9:3]    # [12, 15, 18]

even_idx_vals = list1[::2]  # [10, 12, 14, 16, 18]
odd_idx_vals = list1[1::2]  # [11, 13, 15, 17, 19]
```

`[::-1]` で逆順のListも簡単に作れます．  

```python
list1 = list(range(10, 20)   # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list1_r = list1[::-1]        # [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
```

`[:]` でコピー(Shallow Copy)になります．   

```python
list1 = [0, 1, 2]
list2 = list1[:]    # [0, 1, 2]

list1[0] = 100
print(list1)    # [100, 1, 2]
print(list2)    # [0, 1, 2]
```

Shallow CopyなのでList内のListの要素は共有されます．    

```python
list3 = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
list4 = list3[:]

list3[0][0] = 100
print(list3)    # [[100, 1, 2], [0, 1, 2], [0, 1, 2]]
print(list4)    # [[100, 1, 2], [0, 1, 2], [0, 1, 2]]
```

## アンパック (Unpack)

ListやTupleは，左辺に変数を複数置くことでListを分解して要素を一度に代入することができます．  

```python
list1 = [10, 11, 12]

a, b, c = list1
print(a, b, c)    # 10 11 12
```

Listを変数と部分Listに分割したい場合は `*` を使います．
個別に変数化したいものを並べ，`*` をつけた変数を1つ置くことで，残りを `*` のついた変数にListとしてまとめることができます．  

```python
list1 = [10, 11, 12, 13, 14]
a, b, *c = list1

print(a)    # 10
print(b)    # 11
print(c)    # [12, 13, 14]


x, *y, z = list1

print(x)    # 10
print(y)    # [11, 12, 13]
print(z)    # 14
```

スライスを使うとこんな感じです．   

```python
list1 = [10, 11, 12, 13, 14]
a, b = list1[:2]
c = list1[2:]
```

Tupleの項でも見ますが，次のようにも書けます．   

```python
list1 = [10, 11, 12, 13, 14]
a, b, c = list1[0], list[1], list[2:]
```


## 加算，乗算

Listには加算と乗算の演算が用意されています．  

|     演算子      |                       説明                       |
| :-------------: | :----------------------------------------------: |
| `list1 + list2` | オペランドの **Listどうし** を連結したListを作る |
| `list1 * int1`  |    `list1` を `int1` だけコピーしたListを作る    |

加算はListどうしのみでできます．  

```python
list1 = [0, 1, 2, 3, 4]
list2 = [10, 11, 12]

list3 = list1 + list2    # [0, 1, 2, 3, 4, 10, 11, 12]


list4 = [0, 1, 2, 3, 4]

list7 = list1 + list2 + list4
# [0, 1, 2, 3, 4, 10, 11, 12, 100, 101, 102, 103]


list7 += [1000]
# [0, 1, 2, 3, 4, 10, 11, 12, 100, 101, 102, 103, 1000]
```

乗算は `list1 * int1` の形で，`list1` を `int1` だけコピーしたListを作ります．   

```python
list1 = [0, 1, 2] * 3    # [0, 1, 2, 0, 1, 2, 0, 1, 2]
```

これは次のことと同じです．  

```python
list1 = [0, 1, 2]
list2 = [list0, list0, list0]
```

(Extra)

しかし，次のコードとは異なります．  

```python
list3 = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

違いは，上のコードは共通のListオブジェクト(`list0`)を要素としてもっているのに対して，下は独立したListオブジェクトを要素としていることです．  
この違いは，例えば次のように影響します．  

```python
list2[0] = 100
print(list2)

list3[0] = 100
print(list3)
```

(ここまでExtra)

## in

あるオブジェクト x が List に含まれるかどうかは `x in <listオブジェクト>` で確かめられます．  

```python
list1 = [10, 11, 12, 13, 14]

x1 = 10
if x1 in list1:
    print("Yes")
else:
    print("No")
# Yes

x2 = 20
if x2 in list1:
    print("Yes)
else:
    print("No")
# No
```


## List のメソッド

List の代表的なメソッドを紹介します．  

|            メソッド             |                        説明                         |
| :-----------------------------: | :-------------------------------------------------: |
|           `append(x)`           |             `x` をListの末尾に追加する              |
|         `insert(i, x)`          |          インデックス`i`に値`x`を挿入する           |
|           `remove(x)`           | `x`に等しい要素でインデックスが最小のものを除去する |
|             `pop()`             |           Listの末尾の要素を除去して返す            |
|           `index(x)`            |     `x` に等しい要素で最小のインデックスを返す      |
|           `count(x)`            |            引数と同じ値の要素の数を返す             |
| `sort(key=None, reverse=False)` |          要素を **in-place** でソートする           |

`copy`モジュール
|`deepcopy()`|引数のListをDeep Copyする|

`append()` は引数のオブジェクトをListの末尾に追加します．  

```python
list1 = []
list1.append(10)    # [10]
list1.append(11)    # [10, 11]
list1.append(12)    # [10, 11, 12]
```

`index(x)` で，`x` に等しい要素のインデックスを返します．  
複数ある場合は最小のインデックスになります．  

```python
list1 = [10, 11, 11, 10, 11, 10]

idx11 = list1.index(11)    # 1
```

`x` に等しい要素がない場合は ValueError になります．  
なので，まず `count(x)` で要素の数を調べ，1以上の場合に使うようにしましょう．  

```python
lsit1 = [10, 11, 11, 10, 11, 10]

cnt12 = list1.count(12)        # 0
if cnt12 > 0:
    idx12 = list1.index(12)
else:
    idx12 = -1

print(idx12)    # -1


cnt10 = list1.count(10)    # 3
if cnt10 > 0:
    idx10 = list1.index(10)
else:
    idx10 = -1

print(idx10)    # 0
```

(Extra)
あるいは `try-except` で囲って例外処理をします．  

```python
list1 = [10, 14, 11, 10,  12, 13]

try:
    idx12 = list1.index(12)    # ValueError
except ValueError:
    idx12 = -1

print(idx12)    # -1
```
(ここまでExtra)

`sort()` でListの要素を昇順にできます．   

```python
list1 = [10, 14, 11, 10, 12, 13]
list1.sort()
print(list1)    # [10, 10, 11, 12, 13, 14]
```

`sort(reverse=True)` とすれば降順でソートできます．  

```python
list1 = [10, 14, 11, 10, 12, 13]
list1.sort(reverse=True)
print(list1)    # [14, 13, 12, 11, 10, 10]
```

`sort()` は **in-place(=その場で)なので，もとのListが変化する** ことに気を付けましょう．  
もとのListを壊したくない場合は，組込み関数 `sorted()` を使います．  

```python
list1 = [10, 14, 11, 10,  12, 13]

list2 = sorted(list1)

print(list1)    # [10, 14, 11, 10, 12, 13]
print(list2)    # [10, 10, 11, 12, 13, 14]
```

`sort()` に `key` を渡すといろんな仕方でソートできて楽しいのですが，書くことが多くて煩雑になるので `sort()` だけの章か項目でも作ろうと思ってます．   


(Extra)  
2次元以上の List を，全く別の List としてコピー(Deep Copy)するには `copy`モジュールの `deepcopy()` を使います．  

```python
import copy

list1 = [[0, 1, 2], [0, 1, 2]]

shallow_copied_list = list1[:]
deep_copied_list = copy.deepcopy(list1)

deep_copied_list[0][0] = 100
print(deep_copied_list)    # [[100, 1, 2], [0, 1, 2]]
print(list1)                      # [[0, 1, 2], [0, 1, 2]]

shallow_copied_list[0][0] = 100
print(shallow_copied_list)    # [[100, 1, 2], [0, 1, 2]]
print(list1)                          # [[100, 1, 2], [0, 2, 2]]
``` 


あと，以下は一応表には載せたんですがあんま使ったことないのメソッドになります．  

`insert(i, x)` で，`x` を `i`番目に挿入します．   

```python
list1 = [10, 11, 12]
list2 = list1.insert(1, 100)

print(list1)    # [10, 100, 11, 12]
print(list2)
```

`remove(x)` で `x` をListから除去します．  
同じ値の要素が複数ある場合は，インデックスが最小のものを除去します．  

```python
list1 = [10, 11, 11, 10, 11, 10]

list1.remove(11)    # [10, 11, 10, 11, 10]
```

`append()` と `pop()` を使ってListをスタックとして扱えます．  

```python
list1 = [10, 11, 12]

list1.append(13)
list1.append(14)

a = list1.pop()    # 14
b = list1.pop()    # 13
c = list1.pop()    # 12

print(list1)    # [10, 11, 12]
```
(ここまでExtra)


# Tuple (タプル)

Listがミュータブルだったのに対し，Tupleはイミュータブルです．  
ListとTupleは非常によく似ているので，`Tuple = 要素を変更できないList` と思ってもらっていいです．  
あんま使わないんでそれさえ覚えてもらえればいいかと．  

下の例は，Tupleに代入しようしてエラーになるコードです．  

```python
list1 = [10, 11, 12, 13, 14]
list1[2] = 100    # [10, 11, 100, 13, 14]

tpl1 = (10, 11, 12, 13, 14)
tpl1[2] = 100
# TypeError: 'tuple' object does not support item assignment
```

## 初期化

### 要素で初期化

`()` の中に `,`(カンマ)区切りで要素を並べてTupleを作ることができます．  
空タプルは `(, )` で定義します．  

```python
tpl1 = (10, 11, 12, 13, 14)
tpl2 = (10.9, 11.3, 12.4, 13.0, 14.4)
tpl3 = ("zero", "one", "two", "three", "four")

misc_tpl = (1, "one", [100, 200, 300])
empty_tpl = (, )
```

一応 `()` がなくてもOKですが，Tupleとして扱ってほしい場合は `()` をつける方がわかりやすくていいです．  

```python
tpl1 = 10, 11, 12, 13, 14
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

tpl_list = (
  0, 1, 2,
  (10, 11),
  (
    (100, 101, 102, 103),
    (110, 111, 112, 113)
  )
)
```

### `tuple()` で初期化

Listと同様，組込み関数 `tuple()` にiterableオブジェクトを渡すことでTupleを作ることができます．  
Listの値を渡したいが値を変えられたくない場合は，Listを `tuple()` でTuple化します．  

```python
tpl_from_list = tuple([1, 2, 3])   # (1, 2, 3)
tpl_from_dicrionary = list({"name": "Flareon", "type": "Fire"})  # ("name", "type")
```

(Extra)
### Tuple内包表記

List内包表記はあるんですが，**Tuple内包表記はありません**．  
でも `(expression for item in iterable)` という書式は存在します．  
見た目的に勘違いしやすい(自分は勘違いしてた)のですが，**`(expression for item in iterable)` は Generator(ジェネレータ)内包表記** です．  
Generatorは後の章で説明できたらいいんですが，イテレーション機能をもつオブジェクト(generatorオブジェクト)を提供する関数です．  
次に示すのは，2の累乗を0乗から9乗までイテレートするgeneratorオブジェクトを作るジェネレータになります．  

```python
def generator1():
    i = 0
    while i < 10:
        yield 2 ** i
        i += 1
```

このジェネレータは次のジェネレータ内包表記と同じ動作をします．  

```python
(2 ** i for i in range(10))
```

iterableオブジェクトがイテレートできるのはこういったジェネレータがオブジェクト(のクラスの `__iter__` と `__next__`)に実装されているからです．  
逆に言えば，オブジェクト(のクラスの `__iter__` と `__next__`)にジェネレータを実装するとiterableオブジェクトになります．  
ワクワクしてきたところですが，一旦この話は置いておきましょう．  

ジェネレータはgeneratorオブジェクトを返します．  
generatorオブジェクトはiterableなので，`tuple()` とジェネレータ内包表記を用いて次のようにTupleが作れます．  

```python
tpl = tuple((2 ** i for i in range(10))
# (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
```

上のジェネレータからも作ることができます．  

```python
gen1 = generator1()

tpl = tuple(gen1)    # (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
```

(ここまでExtra)


## アンパック

Listと同様，Tupleもアンパックできます．  

```python
tpl = (10, 11, 12)
a, b, c = tpl

print(a)    # 10
print(b)    # 11
print(c)    # 12
```

Tupleの定義とアンパックを使用すると，複数の変数に一度に値を代入することができます．  

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


# Dictionary (辞書)

Pythonには，keyとvalueのペアを複数保持するデータ構造として Dictionary (辞書) があります．  
同様のデータ構造は，ほかの言語では Map という名称が多いです．  
見た目的には以下のようになります．  
key には，一意であればどんなオブジェクトでも指定できます(正確には hash値 が計算可能なオブジェクト)．  

```python
dict1 = {
    1: "one",
    2: "two",
    3: "three"
}

dict2 = {
    "one": 1,
    "two": 2,
    "three": 3
}

dict3 = {
  "evens": [0, 2, 4, 6, 8],
  "odds": [1, 3, 5, 7, 9]
}

dict4 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

empty_dict = {}
```

Dictionary も多次元にできます．  

```python
dict1 = {
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

Dictionaryも複数の初期化方法を持っています．  

### 要素で初期化

先ほどの例にもあったように，`{key: value, key: value, ... }` の書式で値を定義します．  

```python
dict1 = {
    "name": "Flareon",
    "type": "Fire"
}
```

### `dict()` で初期化

組込み関数 `dict()` を使用してDictionaryを作ります．  
次の例は，引数としてTupleのListを渡しています．  

```python
dict1 = dict([("name", "Flareon"), ("type", "Fire")])

print(dict1)
'''
dict1 = {
    "name": "Flareon",
    "type": "Fire"
}
'''
```

キーワード引数で key と value を指定することもできます．  
キーボード引数については関数の章で紹介します．  

```python
dict1 = dict(name="Flareon", type="Fire")

print(dict1)
'''
dict1 = {
    "name": "Flareon",
    "type": "Fire"
}
'''
```

(Extra)

### Dictionary内包表記

List, Generator に並んで Dictionary にも内包表記があります．  
書式は `{ key: value for items in iterable }` です．
key と value のペアがある分ちょっと複雑です．  

```python
dict1 = {i: i * i for i in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

dict2 = {s: len(s) for s in ("Eevee", "Vapareon", "Jolteon", "Flareon")}
'''
{
    "Eevee": 5,
    "Flareon": 7,
    "Jolteon": 7,
    "Vapareon": 8
}
'''

dict3 = {k: v for k, v in (("name", "Flareon"), ("number", 136), ("type", "Fire"))}
'''
{
    "name": "Flareon",
    "number": 136,
    "type": "Fire"
}
'''
```

### value の取得

`<dictオブジェクト>[key]` で key に対応した value を取得することができます．  
存在しない key の value を取得しようとするとエラーになります．   


```python
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

a = dict1["Vapareon"]   # Water
b = dict2["Espeon"]     # KeyError: 'Espeon'
```

また，左辺で `<dictオブジェクト>[key]` を使うことで，key に対応した value を代入できます．  
存在しない key を指定した場合は，key と value のペアが新しく追加されます．  

```python
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

dict1["Jolteon"] = "でんき"
print(dict1)
'''
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "でんき",
    "Flareon": "Fire"
}
'''

dict1["Espeon"] = "エスパー"
print(dict1)
'''
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "でんき",
    "Flareon": "Fire",
    "Espeon": "エスパー"
}
'''
```

ちなみに Dictionary では `[n]` とすると n が key として解釈されるので，List や Tuple のようにインデックスで値を取得することはできません．  

### len()

`len()` で key, value のペアの数を計算できます．  

```python
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}
print(len(dict1))    # 3

empty_dict = {}
print(len(empty_dict))    # 0
```

## in

あるオブジェクト x が Dictionary の key に存在するかは `x in <dictオブジェクト>` で確かめられます．  

```python
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

x1 = "Flareon"
if x1 in dict1:
    print("Yes")
else:
    print("No")
# Yes

x2 = "Espeon"
if x2 in dict1:
    print("Yes")
else:
    print("No")
# No
```

また，あるオブジェクト x が Dictionary の value に存在するかは `x in <dictオブジェクト>.values()` で確かめられます．  
`values()` は dictオブジェクト のすべての value を dictviewオブジェクト で返します．  
dictviewオブジェクトはイミュータブルで，名前の通り値を見るだけ用のオブジェクトです(values()で返したオブジェクトが変更され，もとのdictオブジェクトのvalueが変わるのを防ぐため) ．

```python
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

x1 = "Fire"
if x1 in dict1:
    print("Yes")
else:
    print("No")
# Yes

x2 = "でんき"
if x2 in dict1:
    print("Yes")
else:
    print("No")
# No
```

### Dictionary のメソッド

Dictionary に使用できる主なメソッドを紹介します．  

|        メソッド        |                                                           説明                                                           |
| :--------------------: | :----------------------------------------------------------------------------------------------------------------------: |
| get(key, default=None) | key に対応する value を返す．key が存在しなければ default で指定された値を返す．default に何も指定しなければ None を返す |
|  dict1.update(dict2)   |                 dict1 に dict2 を連結する．重複する key の value は dict2 の value に更新(update)される                  |
|         keys()         |                                     すべての key を dictviewオブジェクト にして返す                                      |
|        values()        |                                    すべての value を dictviewオブジェクト にして返す                                     |
|        items()         |                                      すべての key, value のペアを Tuple にして返す                                       |

`<dictオブジェクト>[key]` で key に紐づいた value を取得できますが，存在しない key を指定した場合は `KeyError` になるのでした．  
`get(key, default=x)` で，key が存在しない場合は default に指定した値を返すようにすることで，より安全に value を取得することができます．  
ケースによって key が存在したり存在しなかったりする Dictionary を扱う際に重宝します．  

```python
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

a = dict1.get("Vapareon", "Unknown")  # Water
b = dict1.get("Espeon", "Unknown")    # Unknown
```

`dict1.update(dict2)` で，dict1 に dict2 を連結します．  
重複する key の value は dict2 の value に更新(update)されます．  
既存の Dictionary の valueまとめて更新したいときや，複数の Dictionary を1つにまとめたいときに使います．  

```python
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "Fire"
}

dict2 = {
    "Flareon": "ほのお",
    "Umbreon": "あく",
    "Espeon": "エスパー"
}

dict1.update(dict2)
print(dict1)
'''
dict1 = {
    "Vapareon": "Water",
    "Jolteon": "Electric",
    "Flareon": "ほのお",    <- 更新
    "Umbreon": "あく",      <- 新規追加
    "Espeon": "エスパー"     <- 新規追加
}
'''
```

# for文

# 練習問題
















