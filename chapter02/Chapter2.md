# Chapter 2 文字列

この章では文字列 (str 型) について掘り下げます．  
Python では文字列をとても柔軟に扱えます．  

<br>

# 定義

文字列は `"`(ダブルクオート) あるいは `'`(シングルクオート)で書くことができます．  

```python
sentence1 = "ダブルクオートで書いた文字列"
sentence2 = 'シングルクオートで書いた文字列'
```

ダブルクオートの中ではシングルクオートは文字列として扱われます．  
同様に，シングルクオートの中ではダブルクオートは文字列として扱われます．  

```python
sentence3 = "Let's get started!"
sentence4 = 'She said "I wanna eat a Black Thunder."'
```

ダブルクオートの中でダブルクオートを，あるいはシングルクオートの中でシングルクオートを使用する場合は `\` か `¥` (エスケープシーケンス) を使用します．  

```python
s1 = "\""
s2 = '\''
```

ほかにエスケープシーケンスを使用するケースとして，改行とタブ空白があります．  

```python
s3 = "次の行に\n行きましょう"
# 次の行に
# 行きましょう

s4 = "Pythonのインデントが\t肌に合わない人もいます"
# Pythonのインデントが    肌に合わない人もいます
```

また，`"""` (ダブルクオート3つ) `'''` (シングルクオート3つ) で囲むと，改行や空白を含めそのまま文字列になります．  

```python
doc = """Form a complex number.

Keyword arguments:
real -- the real part (default 0.0)
imag -- the imaginary part (default 0.0)
"""
```

# インデックス

プログラミング言語では，配列 (Python では list．そのうち紹介します) や文字列の `n 番目` の要素を 0 から数えます．  
以下の例では，
- float_lst の 0 番目の要素は "0.3"，3 番目の要素は "3.1"
- str1の 1 番目の文字は "q"，7 番目の文字は "e"
- str2の 2 番目の文字は "ガ"

```python
float_lst = [0.3, 1.4, 2.9, 3.1, 4.2, 5.8, 6.0]
str1 = "squirtle"
str2 = "ゼニガメ"
```

![count index](img/string_index.png)

<br>

# 文字列長

文字列の長さは組込み関数 `len()`(length = 長さ)で計算できます．  
また，`文字列 s の最後のインデックス = len(s) - 1`です．  
空文字の長さは 0 です．  

```python
str1 = "squirtle"
str2 = "ゼニガメ"
str3 = ""

str1_length = len(str1)   # 8
str2_length = len(str2)   # 4
str3_length = len(str3)   # 0

str1_last_idx = str1[len(str1) - 1]   # str1[8 - 1] = str1[7] = e
str2_last_idx = str2[len(str2) - 1]   # str2[4 - 1] = str2[3] = メ
```

# オフセット

Pythonでは `[]` を使用して文字列から部分文字列の抽出を行うことができます．  

以下の例は，文字列の x 番目を `[x]` で抽出しています．  

```python
str1 = "squirtle"

str1_0 = str1[0]  # s
str1_3 = str1[3]  # i
str1_7 = str1[7]  # e
```

`[-1]` は最後の文字，`[-2]` は最後から 1 番目の文字，というように，負数を指定すると後ろから x 番目の文字を抽出できます．  
後ろから数える場合は -1 番目，-2 番目，...，-(文字列長)番目になります．  

```python
str1 = "squirtle"

str1_m1 = str1[-1]  # e
str1_m5 = str1[-5]  # i
str1_m8 = str1[-8]  # s
```

最後の文字のインデックスより大きい値を指定した場合はエラーになります．  
`最後の文字のインデックス = 文字列長` では **ない** ことに注意しましょう．  
例えば，str1 の文字列長は 8 文字ですが，インデックスは 0 から始まるので最後の文字のインデックスは 7 です．  
8番目の文字を指定するとエラーになります．  
`[-1]` を使えば，どんな文字列でも最後の文字を安全に抽出できます．  

```python
str1 = "squirtle"

str1_7 = str1[7]  # e
str1_m1 = str1[-1]  # e
str1_8 = str1[8]  # IndexError: string index out of range
```

また，`[]` はあくまで文字列の抽出(正確には抽出される文字列と同じ文字列を新規作成する．もとの文字列は破壊されない．後述するスライスも同様)をするものです．  
例えば，文字列 str1 の 2 文字目に `"a"` を代入しようとして `str1[2] = "a"` とすることはできません．  
Python の str型は **イミュータブル** (immutable = 値を変更できない)です．  
ミュータブル，イミュータブルに関しては章末で詳しく取り上げます．  

```python
str1 = "squirtle"

str1[2] = "a"   # TypeError: 'str' object does not support item assignment
```

<br>

# スライス

`[start:end:step]` といった書式を用いると，`start` 番目の文字から `end-1` 番目の文字までの文字列をステップ数 `step` で抽出できます．  
ほかの言語だと `substring()` や `substr()` のような関数を使わなければいけませんが，Pythonではこのスライスによって簡易的かつ直感的に文字列の抽出を行えます．  

(`step` が正の数の場合，)  
`start` を省略すると `start = 0` となり，  
`end` を省略すると`end = 文字列長 (= 最後の文字のインデックス + 1)` となり，  
`step` を省略すると `step = 1 (= 普通通り1文字ずつ抽出)`となります．  

なお，**`end` 番目の文字は抽出されない** ことに注意してください．  
数学の区間で表すと `[start, end)` です．  

具体例を見ながらじっくり見ていきます．  

```python
str1 = "squirtle"

str1_1_6_1 = str1[1:6:1]  # 1文字目から(6-1=5)文字目までステップ数1で = quirt
str1_1_6_3 = str1[1:6:3]  # 1文字目から(6-1=5)文字目までステップ数3で = qr

str1_2_5_1 = str1[2:5:1]  # 2文字目から(5-1=4)文字目までステップ数1で = uir
str1_2_5_2 = str1[2:5:2]  # 2文字目から(5-1=4)文字目までステップ数2で = ur
```
![slice1](img/string_slice1.png)

![slice2](img/string_slice2.png)

以下の例では `step` を省略しています．  
この場合は `step = 1` とするのと同じ結果になります．  
`start <= end` の場合は空文字になります．  

```python
str1 = "squirtle"

str1_1_6 = str1[1:6]    # 1文字目から(6-1=5)文字目まで = quirt
str1_2_5 = str1[2:5]    # 2文字目から(5-1=4)文字目まで = uir
str1_2_m1 = str1[2:-1]  # 2文字目から(-1-1=-2)文字目まで = uirtl
str1_4_2 = str1[4:2]    # 4文字目から(2-1=1)文字目まで = ""(空文字)
```

![slice3](img/string_slice3.png)

`step = 1` のときは，`抽出される文字列長 = end - start`であることを覚えておきましょう．  
例えば，`str1[1:6]` の場合 1 番目の文字から(6 - 1 = 5)文字を抽出します．  

このことを利用すれば，x 番目の文字から n 文字抽出したいといったときは `end` となるインデックスを調べなくても `end = start + n` と計算できます．  
例えば，str1 の 2 番目の文字から 3 文字抽出したい場合は `end = 2 + 3 = 5` だから `str1[2:5]` とすればよいとわかります．  

<br>

さらに `start` を省略すると，0 番目の文字から `end - 1` 番目の文字までを抽出します．  

```python
str1 = "squirtle"

str1_3 = str1[:3]   # squ
str1_5 = str1[:5]   # squir
```

`end` を省略すると，`start` 番目の文字から文字列の最後までを抽出します．  

```python
str1 = "squirtle"

str1_2 = str1[2:]   # uirtle
str1_6 = str1[6:]   # le
```

以下の例では，`start` と `end` を省略して `step` だけ指定しています．  

```python
str1 = "squirtle"

str1_2 = str1[::2]   # surl
str1_3 = str1[::3]   # sil
```

`step` に負数を指定すると，逆順に文字列を抽出します．
つまり `end` 番目の文字から `start + 1` 番目の文字までをステップ数 `step` で抽出します．  
このことを利用すると，`step` と `end` を省略 (すなわち `step = 0`，`end = 文字列長`)，`step = -1` とすることで反転した文字列を簡単に作れます．  
あんま使う機会はないです．  

```python
str1 = "squirtle"

str1_5_2_m2 = str1[5:2:-2]  # ti
str1_2_5_m2 = str1[2:5:-2]  # ""(空文字)

str1_m3 = str1[::-3]   # erq
str1_m1 = str1[::-1]   # eltriuqs
```

![string_slice](img/string_slice4.png)

<br>

# str 型で使用できる主なメソッド

ここでは，str 型で使用できる主要なメソッドを紹介します．  

|   メソッド   |                             説明                             |
| :----------: | :----------------------------------------------------------: |
|   lower()    |         もとの文字列を小文字にした新しい文字列を返す         |
|   upper()    |         もとの文字列を大文字にした新しい文字列を返す         |
| capitalize() |         文字列の先頭を大文字にした新しい文字列を返す         |
|   split()    |                 引数の文字で文字列を分割する                 |
|    join()    |                指定した文字で文字列を連結する                |
|   strip()    |             引数の文字を文字列の前後から除去する             |
|   format()   | 引数の変数の値を文字列中の`{}`に代入した，新しい文字列を返す |

Python では数値，文字列，データ構造，関数，クラスといったあらゆるものが **オブジェクト** として実装されています．  
今まで見てきた int 型 や float 型，bool 型，str 型の値もオブジェクトです．  
オブジェクトは物体を指す言葉ですが，ここでは "変数や関数のかたまり" と考えてください．  
**メソッド** とはオブジェクトが持っている関数のことで，便利な機能を提供してくれています (Extra) Python ではクラスのメンバーである変数は **属性** (attribute)，関数はメソッドと呼ばれます．(ここまで Extra)  
**引数** というパラメータを渡すことで，いろいろな条件でメソッドを使うことができます．  

それでは，str オブジェクトが使えるメソッドを順に見ていきましょう．  

<br>

## lower()

もとの文字列をすべて小文字にした新しい文字列を生成します．  
`<str オブジェクト>.lower()` の書式で使用できます．  
もとの文字列はそのままです．  

```python
str1 = "APPLE"
str1_lower = str1.lower()
print(str1)         # "APPLE"
print(str1_lower)   # "apple"
```

使用例として，ある文字列`str_a` とある文字列 `str_b`が一致するか調べる際，小文字と大文字を区別しない場合に`lower()` を使ってどちらの文字列も小文字(あるいは大文字)にしてしまってから比較することが挙げられます．  

```python
str_a = "Apple"
str_b = "APPLE"
is_same = str_a.lower() == str_b.lower()  # True
```

ちょっと不思議に見えますが，以下のようにも書けます．  

```python
str1_lower = "APPLE".lower()    # "apple"
```

## upper()

もとの文字列をすべて大文字にした新しい文字列を生成します．  
もとの文字列はそのままです．  

```python
str1 = "apple"
str1_upper = str1.upper()
print(str1)         # "apple"
print(str1_upper)   # "APPLE"
```

## capitalize()

もとの文字列の先頭の文字を大文字にした文字列を生成します．  
もとの文字列はそのままです．  

```python
str1 = "apple"
str1_cap = str1.capitalize()
print(str1)       # "apple"
print(str1_cap)   # "Apple"
```


## split()

引数に与えた文字で文字列を分割して list を返します(list については他の章で説明しますが，配列のようなものです)．  
例えば，以下では `,` (カンマ) を区切り文字として分割しています．  

```python
line1 = "1,2,3,4,5"
numbers = line1.split(",")
# ['1', '2', '3', '4', '5']
```

引数を省略した場合は " "(空白)になります．  

```python
line2 = "I love cry of Fearow."
words = line2.split()
# ['I', 'love', "Fearow's", 'cry']
```

以下のようにも書けます．  

```python
words = "I love Fearow's cry".split()
# ['I', 'love', "Fearow's", 'cry']
```


## join()

`split()` とは反対に，引数に与えた文字で文字列を連結します．  
初めは(見た目的に)理解しづらいですが，便利なのでよく使われるメソッドです．  

```python
numbers = ['1', '2', '3', '4', '5']
line1 = ",".join(numbers)   # "1,2,3,4,5"
```

```python
words = ["I", "love", "Fearow's", "cry."]
line2 = " ".join(words)   # "I love Fearow's cry."
```

## strip()

引数で与えた文字を，文字列の前後から除去するメソッドです．  
引数なしの場合は " "(空白)，`\t`，`\n` をすべて除去します．  
一番わかりやすい利用例としては，入力された文字列の前後の余分な空白を取り除いて，ちゃんと入力文字列と比較文字列を比較したいときです．  

```python
input_str = " 0番目の文字と最後の文字が空白    "
comp_str = "0番目の文字と最後の文字が空白"

is_same = input_str == comp_str   # False


input_str_after = input_str.strip()   # "0番目の文字と最後の文字が空白"

is_same = input_str_after == comp_str   # True
```

文字列中の空白は除去されません．  

```python
str1 = "2番 目の文字が空白".strip()   # "2番 目の文字が空白"
```

## fotmat()

引数に与えた値を，文字列中の `{}` に代入して新しい文字列を作ります．  
説明だとわかりにくいので例を見てみましょう．  

```python
sudowoodo_type = "Rock"
str1 = "The type of Sudowoodo is {}.".format(sudowoodo_type)
# The type of Sudowoodo is Rock.

a = 3.0
b = 4.0
str2 = "長さa={}，b={}の2辺をもつ直角三角形の残り1辺の長さ={}".format(a, b, (a * a + b * b) ** 0.5)
# 底辺の長さ=3.0，高さ=4.0の直角三角形の斜辺の長さ=5.0

line1 = "1,2,3,4,5"
str3 = "line1.split(',')={}".format(line1.split(','))
# line1.split(',')=['1', '2', '3', '4', '5']
```

`{}`に入れられる値はintでもlistでもたいてい何でもOKです．  
イメージとしては，変数nを `str(n)` でstr型に変換して `{}` に入れている感じです．  
`print()`を使ってコンソールに出力するための文字列を整形(=format)するときにもよく使われます．  
計算の途中経過を見るときも変数名とその値がわかって便利です．  

```python
# mod の分配法則
res1 = 0
res2 = 0

x = 10
y = 32
z = 61

print("res1={}".format(res1))   # res1=0

res1 += x % 3

print("res1={}".format(res1))   # res1=1

res1 += y % 3

print("res1={}".format(res1))   # res1=3

res1 += z % 3

print("res1={}".format(res1))   # res1=4

res1 %= 3

print("res1={}".format(res1))   # res1=1


res2 = (x + y + z) % 3

print("res2={}".format(res2))   # res2=1
```

format メソッドでは `{}` 内の文字列を成形するための Format String Syntax が用意されています (公式 doc: https://docs.python.org/ja/3/library/string.html#formatstrings ) ．  
かなりたくさんあるのでここでは主要なものを紹介します．  

`{:<文字数>s}` で表示する文字列の文字数を，`{:<桁数>d}` で表示する整数の桁数を決めることができます．  

```python
print("***{:10s}***".format("Lapras"))  # ***Lapras    ***
print("***{:5d}***".format(10))         # ***   10***
```

`{:[<全体の文字数>].<小数点以下の桁数>:f}` で表示する実数の桁数を決めることができます．  
小数点以下の桁数は必須ですが，全体の文字数は省略することができます．  
全体の文字数に小数点 `.` が含まれることに注意してください．  

```python
print("***{:10.2f}***".format(3.141592653589793))    # ***      3.14***
print("***{:.2f}***".format(3.141592653589793))     # ***3.14***
```

指定した小数点以下の桁数に実数の小数点以下の桁数が足りない場合，小数点以下が 0 埋めされます．  
また，`:` のあとに `0` をつけることで整数部分も 0 埋めすることができます．  

```python
print("***{:10.5f}***".format(3.14))    # ***   3.14000***
print("***{:010.5f}***".format(3.14))   # ***0003.14000***
```

int 型も 0 埋めできます．  

```python
print("***{:010d}***".format(10))       # ***0000000010***
```

次の文字を `:` のあとにつけると文字列を左右中央に揃えることができます．  

|Option|説明|
|:---:|:---:|
|`<`|左揃え|
|`>`|右揃え|
|`^`|中央揃え|

```python
print("***{:>10s}***".format("Lapras"))  # ***    Lapras***
print("***{:<10d}***".format(10))       # ***10        ***
print("***{:^10.5f}***".format(3.14))   # *** 3.14000  ***
```

また，Python3.6から `format()` と同等の機能として `f 文字列` (f-strings) が使えるようになりました．  
ダブルクオート，あるいはシングルクオートの前に `f` をつけることで，文字列中の `{}` に直接変数を入れることができます．  
先に`format()`を紹介しましたが，f 文字列の方が楽に書けるのでこちらの方がおすすめです．  

```python
sudowoodo_type = "Rock"
str1 = f"The type of Sudowoodo is {sudowoodo_type}."
# The type of Sudowoodo is Rock.

a = 3.0
b = 4.0
str2 = f"長さa={a}，b={b}の2辺をもつ直角三角形の残り1辺の長さ={(a * a + b * b) ** 0.5}"
# 底辺の長さ=3.0，高さ=4.0の直角三角形の斜辺の長さ=5.0

line1 = "1,2,3,4,5"
str3 = f"line1.split(',')={line1.split(',')}"
# line1.split(',')=['1', '2', '3', '4', '5']
```

```python
res1 = 0
res2 = 0
x = 10
y = 32
z = 61

print(f"res1={res1}")   # res1=0

res1 += x % 3

print(f"res1={res1}")   # res1=1

res1 += y % 3

print(f"res1={res1}")   # res1=3

res1 += z % 3

print(f"res1={res1}")   # res1=4

res1 %= 3

print(f"res1={res1}")   # res1=1


res2 = (x + y + z) % 3

print(f"res2={res2}")   # res2=1
```

```python
s = "Lapras"
n = 10
r = 3.14

print(f"***{s:10s}***")     # ***Lapras    ***
print(f"***{n:10d}***")     # ***        10***
print(f"***{r:10.5f}***")   # ***   3.14000***

print(f"***{n:010d}***")    # ***0000000010***
print(f"***{r:010.5f}***")  # ***0003.14000***

print(f"***{s:>10s}***")    # ***    Lapras***
print(f"***{n:<10d}***")    # ***10        ***
print(f"***{r:^10.5f}***")  # *** 3.14000  ***
```


<br>

# 変数

ミュータブル (mutable) とは値が変更可能なことをいい，イミュータブル (immutable) は値が変更できないことをいいます．  
str オブジェクトはイミュータブルという話をしましたが，そのことに疑問を持たれるかもれません．  

例えば，次のコードは 変数 `s1` に `"first"` を代入したあと，`"second"` を代入しています．  

```python
s1 = "first"
s1 = "second"
```

値変わってるじゃないかって感じですね．  
次のコードも変数 `s2` に "Hello, " を代入したあと，`+=` を使って `"Hello, World!"` にしています．  

```python
s2 = "Hello, "
s2 += "World!"  # Hello, World!
```

Python において，オブジェクトがミュータブル，あるいはイミュータブルであるというのは，**オブジェクトの値が変更可能か可能でないか** のことをいいます．  
実は，これらの 2 つのコードにおいてそれぞれの str オブジェクトの値は変更されていません．  
変わったのは変数が指すオブジェクトです．  

![s1](img/s1.png)

![s2](img/s2.png)

このことは，組込み関数 `id()` を使うことで確かめられます．  
`id()` は，オブジェクトが格納されているメモリのアドレスを返す関数です．  
返ってくる値は環境によって変わりますが，同一オブジェクトであれば同じ値を返します．  
たしかに，同じ変数でも前後でメモリのアドレスが変わっている，つまり変数の指すオブジェクトが変わっていることがわかります．  

```python
s1 = "first"
print(f"s1-1 | {id(s1)}")

s1 = "second"
print(f"s1-2 | {id(s1)}")

"""
s1-1 | 4393755312
s1-2 | 4394403376
"""
```

```python
s2 = "Hello, "
print(f"s2-1 | {id(s2)}")

s2 += "World"
print(f"s2-2 | {id(s2)}")

"""
s2-1 | 4325458480
s2-2 | 4326024944
"""
```

では，変数に変数を代入する場合はどうでしょうか．  

```python
s3 = "Ditto"
s4 = s3

print(f"s3 | {id(s3)}")
print(f"s4 | {id(s4)}")
"""
s3 | 4378886960
s4 | 4378886960
"""
```

2 つの変数は同じオブジェクトを指しているようです．  
つまり，**変数に変数を代入した場合は，オブジェクトを指す変数が 2 種類に増えるだけで，オブジェクトがコピーされるわけではありません．**  
イメージとしては次のようになります．  

![Ditto](img/Ditto.png)

このように，Python における変数はメモリと一対一の関係にはなく，オブジェクトを指すためのラベルとして働きます．  
"変数に代入する" という言い方が紛らわしいですね...
この言い方は一般的ですし，本稿でも以降使用していきますが，Python での変数の働きは "箱に値を入れる" ようなものではなく "値にラベルをつける" というイメージを忘れないようにしてください．  

変数がラベルっぽくみえる例をもう少し紹介します．  

次のコードでは，変数 s1 に `"first"` を代入し，変数 s2 に s1 を代入しています．  
このとき，s1 と s2 はともに str オブジェクト `"first"` を指しています．  
そのあと，s2 に `"second"` を代入していますが，s1 にも `"second"` が代入されるわけではありません．  
Python において変数はラベルなので，s2 は `"first"` から離れ `"second"` を指すようになります．  
結局，s1 は `"first"` を指したままで，s2 だけ新しく `"second"` を指します．  

```python
s1 = "first"
s2 = s1
s2 = "second"

print(s1)   # first
print(s2)   # second
```

次のコードは，変数 s1 に `"first"` を代入し，変数 s2 に s1 を代入したあと，今度は s1 に `"second"` を代入しています．  
`s2 = s1` で s1 と s2 はともに `"first"` を指すようになります．  
そのあと，`s1 = "second"` で s1 は `"second"` を指すようになりますが，s2 は "first" を指したままです．  

```python
s1 = "first"
s2 = s1
s1 = "second"

print(s1)   # second
print(s2)   # first
```

このように，再代入することはラベルを貼り替えることと同じです．  
同じオブジェクトを指す複数の変数のうちのどれかに新しくオブジェクトを代入したとしても，ほかの変数が指すオブジェクトが変わるわけではありません．  


# 練習問題

## Q 1

`s = "Bulbasaur"` の最初の文字と最後の文字を連結した文字列を作って出力してみましょう．  

```python
s = "Bulbasaur"
```


## Q 2

`a = 954256109364964217539864` は何桁の数字でしょうか．  

```python
a = 954256109364964217539864
```

## Q 3

`a = 954256109364964217539864` の， `n = 1_000_000_000`の位の数字を出力してください．  
なお，1 の位は 4，10 の位は 6，100 の位は 8，...，です．

```python
a = 954256109364964217539864
n = 1_000_000_000
```

## Q 4

`alp = "abcdefghijklmnopqrstuvwxyz"` の 5 文字目 から 15 文字目まで (**1 文字目を最初の文字** とし，5 文字目，15 文字目を含む) を使ってできる文字列は何になるでしょうか．  
(紛らわしいですが，プログラミングに関する Web サイトや本，ドキュメントでも，文字列について `n` 文字目というときは 1 文字目はじまりが一般的です)

```python
alp = "abcdefghijklmnopqrstuvwxyz"
```


## Q 5

`alp = "abcdefghijklmnopqrstuvwxyz"` の 11 文字目から 6 文字 (**1 文字目を最初の文字** とし，11 文字目を含む) を使ってできる文字列は何になるでしょうか．  

```python
alp = "abcdefghijklmnopqrstuvwxyz"
```

## Q 6

`alp = "abcdefghijklmnopqrstuvwxyz"` の奇数番目の文字を全て抽出してください．  

<details>
  <summary>ヒント</summary>
  <p><code>alp[start::step]</code> の <code>start</code> と <code>step</code> に適切な値を設定しましょう</p>
</details>

```python
alp = "abcdefghijklmnopqrstuvwxyz"
```

## Q 7

次の文章を，行ごとに区切ってlistにしてみましょう．  
なお，空文字は list に入れないようにしてください．  

<details>
  <summary>ヒント</summary>
  <p>区切り文字は <code>\n</code> です</p>
</details>

```python
recipe = """(1) フタをあける
(2) 粉末スープを入れる
(3) お湯を注ぐ
(4) 3分待つ
(5) できあがり
"""
```

## Q 8

次の list から，文字列 `123456789` を作って出力してください．  

```python
numbers = ["123", "456", "789"]
```


## Q 9

文字列 `Mr.Mime` を使って回文を1つ作ってください．  
回文とは，始めから読んでも終わりから読んでも同じ文のことをいいます．  
意味は通ってなくてもよく，始めから読んでも終わりから読んでも同じ文字列であればよいです．  
例) しんぶんし，level  

<details>
  <summary>ヒント</summary>
  <p>単純に，もとの文字列に，もとの文字列を反転した文字列を連結させれば回文になります</p>
</details>

```python
s = "Mr.Mime"
```


## Q 10

`t = 7529` 秒は何時間何分何秒でしょうか．  
コンソールに `x時間x分x秒`の形式で出力してください．  

```python
t = 7529
```


<hr>

[Chapter 2 練習問題解答例](Answers2.md)  
[Index](../README.md)
