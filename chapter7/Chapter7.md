# Chapter 7 クラス

これまで int オブジェクトや str オブジェクト，list オブジェクトなど，多くの型 (= クラス) に属するオブジェクトを見てきました．  
クラスとは，オブジェクトの定義，やわらかく言えばオブジェクトの設計図のことです．  
オブジェクトがどんな変数をもつのか，どんな関数をもつのか，どのように扱えるのか (どのようなプロトコルをもつのか)，どのように作るのかが書かれています．  

関数は同じ処理を集約し，簡単に繰り返し使えるように導入しました．  
同様に，クラスは変数や関数をひとかたまりにしたもの (= オブジェクト) を簡単に繰り返し使えるように導入します．  


# コンストラクタ (constructor)

次の list `items` は，ネットショップで売られている商品と価格を表す dict をまとめたものです．  
要素の dict はすべて `item_name`，`unit_price` といった共通の key をもっています．  
このように，同じ構造をもつオブジェクトはクラスで定義すると扱いやすくなります．  

```python
items = [
    {
        "item_name": "モンスターボール",
        "unit_price": 200,
    },
    {
        "item_name": "スーパーボール",
        "unit_price": 600,
    },
    {
        "item_name": "ハイパーボール",
        "unit_price": 1200,
    },
    {
        "item_name": "リピートボール",
        "unit_price": 1000,
    },
    {
        "item_name": "タイマーボール",
        "unit_price": 1000,
    },
]

for item in items:
    print(f"item_name={item['item_name']}, unit_price={item['unit_price']}")

"""
item_name=モンスターボール, unit_price=200
item_name=スーパーボール, unit_price=600
item_name=ハイパーボール, unit_price=1200
item_name=リピートボール, unit_price=1000
item_name=タイマーボール, unit_price=1000
"""
```

ショップで売られている商品をクラス `Item` として定義すると次のようになります．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price


items = [
    Item("モンスターボール", 200),
    Item("スーパーボール", 600),
    Item("ハイパーボール", 1200),
    Item("リピートボール", 1000),
    Item("タイマーボール", 1000)
]

for item in items:
    print(f"item_name={item.item_name}, unit_price={item.unit_price}")

"""
item_name=モンスターボール, unit_price=200
item_name=スーパーボール, unit_price=600
item_name=ハイパーボール, unit_price=1200
item_name=リピートボール, unit_price=1000
item_name=タイマーボール, unit_price=1000
"""
```

クラス名は変数名や関数名と違いキャメルケースにします．  
各単語の先頭のみを大文字にしてつなげたもので，例えば，camel case は `CamelCase` と書きます．  
キャメルとはラクダの背中をいう英語で，でこぼこな感じをたとえています．  

Python ではクラスで定義されている変数を **属性** (attribute)，関数を **メソッド** と呼びます．  
上の例では，Item クラスは属性 item_name，unit_price と，メソッド `__init__` を定義しています．  
したがって，Item クラスのオブジェクトは属性 item_name，unit_price と，メソッド `__init__` をもちます．  

`__init__` (アンダースコア x 2 + init + アンダースコア x 2) メソッドはオブジェクトを作る際にオブジェクトを初期化するメソッドになります．  
オブジェクトを作るときに呼び出されるメソッドを **コンストラクタ** (constructor) といいます．  
`<クラス名 (クラスオブジェクト)>([引数 1, 引数 2, ...])` とするとコンストラクタが呼び出され，オブジェクトを作ることができます．  
例えば，`Item("モンスターボール", 200)` とすると `item_name = "モンスターボール"`，`unit_price = 200` で `__init__` メソッドが呼び出されます．  
`self` はオブジェクト自身を指す変数です．  
オブジェクトのメソッドはすべて第一仮引数に `self` をとります．  
また，オブジェクトのメソッドが呼ばれるときには暗黙的にオブジェクト自身が第一実引数として渡されます．  
`self.item_name = item_name`，`self.unit_price = unit_price` で作られているオブジェクトの item_name 属性と unit_price 属性に引数 item_name，unit_price の値を代入しています．  

このようにして具体的にオブジェクトの属性に値を与えたものを **インスタンス** (instance，一例) と呼びます．  
Item クラスは Item オブジェクトの設計図 (を含むオブジェクト)，Item オブジェクトは属性 item_name，unit_price をもつオブジェクト，そして属性 item_name に `モンスターボール`，unit_price に 200 をもつ Item オブジェクトは Item オブジェクトのインスタンスの 1 つです．  
オブジェクトとインスタンスの違いはこんな感じですが，作られたオブジェクトは属性に何らかの値をもつので，上の例だと Item クラスのオブジェクトを 5 個作っているとも item クラスの (オブジェクトの) インスタンスを 5 個作っているとも言えますし，話しててもオブジェクトでもインスタンスでも通じるのであんまり気にしなくていいと思います．  

インスタンスを作ることを **インスタンス化する** (instantiate) と言ったりします．  


# インスタンス属性

属性にはクラス属性とインスタンス属性の 2 種類があります．  

インスタンスの属性には `<インスタンス>.<インスタンス属性>` でアクセスし，値の取得や代入が行えます．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price


item = Item("モンスターボール", 200)
print(item.unit_price)   # 200

item.unit_price = 20000  # unit_price 属性を更新
print(item.unit_price)   # 20000
```

のちに，クラスの属性についても紹介します．  


# インスタンスメソッド

メソッドは `<インスタンス>.<インスタンスメソッド>([引数 1, 引数 2, ...])` で呼び出すことができます．  

次のコードでは，Item クラスに商品の評点をつける review メソッド，レビュー数をカウントする `review_cnt`，`review_score` を定義しています．  
メソッドの第一仮引数は必ず `self` にして，メソッドが呼び出されるときにオブジェクト自身が渡されるようにします．  
`item.review(5)` では暗黙的に第一実引数にオブジェクト自身が渡されています．  
クラス内から属性にアクセスするには `self.<属性>` のようにします．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price
        self.review_cnt = 0     # レビュー数
        self.review_score = 0.0   # レビューの評点
        self.review_users = {}  # レビューしたユーザを管理

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self.review_users[user_name] = score    # 1 ユーザにつき 1 レビューとする
        self.review_cnt = len(self.review_users)
        self.review_score = (self.review_score + score) / self.review_cnt    # 評点は平均点とする


item = Item("モンスターボール", 200)
item.review("サトシ", 5)  # 実は review(item, user_name, score)
print(item.review_score)    # 5.0

item.review("タケシ", 2)  # 実は review(item, user_name, score)
print(item.review_score)    # 3.5
```

次のコードでは，新たに `__repr__` (represent; 表現する) メソッドと `__str__` メソッドを追加しています．  
この 2 つのメソッドは組込み関数 str と repr によって呼び出されるメソッドです．  
`__str__` の返り値は str 関数にオブジェクトを渡したときに返してほしい文字列にします．  
`__repr__` はデバッグやログ用のメソッドで，デバッグ時にどんなオブジェクトかがわかるような情報を文字列として返すようにします．  
str 関数は呼び出されると，`__str__` メソッドがあれば呼び出し，なければ `__repr__` メソッドを呼び出してその返り値を返します．  
repr 関数は呼び出されると `__repr__` メソッドを呼び出してその返り値を返します．  
したがって，どちらの関数が呼び出されても所望の文字列が返るよう少なくとも `__repr__` メソッドを実装すると良いです．  

また，組込み関数 print はオブジェクトが渡されたとき str を呼び出してその返り値の文字列を標準出力に出力するようになっています．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price
        self.review_cnt = 0     # レビュー数
        self.review_score = 0.0   # レビューの評点
        self.review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self.item_name}, unit_price={self.unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self.review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self.item_name}: {self.unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self.review_users[user_name] = score    # 1 ユーザにつき 1 レビュー
        self.review_cnt = len(self.review_users)
        self.review_score = sum(self.review_users.values()) / self.review_cnt  # 評点は平均点とする



item = Item("モンスターボール", 200)
item.review("サトシ", 5)

s = str(item)
print(s)    # モンスターボール: 200: 5.0 star (1 reviews)

r = repr(item)
print(r)    # Item(item_name=モンスターボール, unit_price=200, review_cnt=1, review_score=5.0, review_users={'サトシ': 5.0})

print(item)  # モンスターボール: 200: 5.0 star (1 reviews)
```

`__init__` や `__str__`，`__repr__` のように両端がアンダースコアとなっているメソッドは特殊メソッド (special method)，あるいはダンダーメソッド (dunder method; double undersocre method) と呼ばれます．  
組込み関数はオブジェクトが渡されると，オブジェクトに実装されているこれらの特殊メソッドを使って値を返します．  
str 関数や repr 関数のほかに，例えば len 関数はオブジェクトに実装されている `__len__` メソッドを使って値を返しています．  
また，`__getitem__` メソッドを実装すると `<オブジェクト>[インデックス or key]` と書けるようになったり，`__eq__` を実装してオブジェクトを `==` で比較できるようにするなど演算子の働きを定義することもできます．  

またあとでクラスメソッドについても説明します．  


# アクセシビリティ

オブジェクトの属性やメソッドが外部から使用可能かどうかを，属性やメソッドのアクセシビリティといいます．  
内部でしか使用しない変数は，なるべく外部から使われないように隠したり外部からの値の更新を禁止したりしたほうが良いです．  

例えば，今実装している Item クラスの review_users は review_cnt，review_score の計算専用の dict であり，むやみに外部から値を変更されてほしくないです．  
その方法を検討していきます．  

一般的にアクセシビリティがどんなものかを具体的に知るため，ほかの言語を引き合いに出しながら説明します．  
まず，Python には C++ や Java の `public`，`private` といったようなアクセス指定子 / 修飾子がありません．  

次のコードは，先ほどまで実装していた Item クラスを C++ で実装したものです．  
`class Item` の下に `public` というアクセス指定子があり，その下に item_name や unit_price といった変数，review 関数が定義されています．  
アクセス指定子の下にまとめらている変数，関数のアクセシビリティは，この場合は `public` (公開) になり，外部のどこからでも変数，関数にアクセスすることができます．  

```cpp
#include <iostream>
#include <map>
#include <string>

using namespace std;

class Item {
public:
  string item_name;
  int unit_price;
  int review_cnt = 0;
  float review_score = 0.0;
  map<string, int> review_users;
  Item(string item_name, int unit_price) : item_name(item_name), unit_price(unit_price) {}

  void review(string user_name, int score) {
    review_users[user_name] = score;
    review_cnt = review_users.size();
    double t = 0;
    for (auto user : review_users) {
      t += user.second;
    }
    review_score = t / review_cnt;
  }
};

int main() {
  Item item("モンスターボール", 200);
  item.review("サトシ", 5);

  cout << "item_name=" << item.item_name << endl;
  cout << "unit_price=" << item.unit_price << endl;
  cout << "review_score=" << item.review_score << endl;
  cout << "review_cnt=" << item.review_cnt << endl;

  // item.review_users を表示
  cout << "review_users={" << endl;
  for (auto user : item.review_users) {
    cout << "  \"" << user.first << "\" : " << user.second << ",\n";
  }
  cout << "}" << endl;
}

// item_name=モンスターボール
// unit_price=200
// review_score=5
// review_cnt=1
// review_users={
//   "サトシ" : 5,
// }
```

次のコードでは，review_users の定義を `private` 以下に変更しています．  
`private` の下の変数，つまり review_users のアクセシビリティは `private` (非公開) となり，外部から使用することはできません．  
そのため，`item.review_users` のように値を取得しようとするとエラーが出ます．  
このように，`private` を指定することでオブジェクトの変数の値を外部から読み取ったり，変更されたりするのを防ぐことができます．  

```cpp
class Item {
public:
  string item_name;
  int unit_price;
  int review_cnt = 0;
  float review_score = 0.0;
  Item(string item_name, int unit_price) : item_name(item_name), unit_price(unit_price) {}

  void review(string user_name, int score) {
    review_users[user_name] = score;
    review_cnt = review_users.size();
    double t = 0;
    for (auto user : review_users) {
      t += user.second;
    }
    review_score = t / review_cnt;
  }

private:
  map<string, int> review_users;
};

int main() {
  Item item("モンスターボール", 200);
  item.review("サトシ", 5);

  cout << "item_name=" << item.item_name << endl;
  cout << "unit_price=" << item.unit_price << endl;
  cout << "review_score=" << item.review_score << endl;
  cout << "review_cnt=" << item.review_cnt << endl;

  // item.review_users を表示
  cout << "review_users={" << endl;
  for (auto user : item.review_users) { // private 変数 review_users にはアクセスできない
    cout << "  \"" << user.first << "\" : " << user.second << ",\n";
  }
  cout << "}" << endl;
}

// example.cpp:36:25: error: ‘std::map<std::__cxx11::basic_string<char>, int> Item::review_users’ is private within this context
//    for (auto user : item.review_users) {
//                          ^~~~~~~~~~~~
// example.cpp:22:20: note: declared private here
//    map<string, int> review_users;
//                     ^~~~~~~~~~~~
```

以上が C++ のアクセス指定子の働きになります．  

一方，Python には C++ や Java の `public` や `private` のようなアクセス指定子 / 修飾子はありません．  
また，属性を完全に非公開にする方法もありません．  
Python では，オブジェクトの属性は公開が基本です．  

(Extra)  

## マングリング (mangling)

そのかわり，属性を外部から見えにくくする方法があります．  
変数名の前に `__` (アンダースコア x 2) をつけることにより，変数名をマングリング (mangling; ぐちゃぐちゃに変形する) して属性にアクセスしづらくします．  
次のコードでは，review_users 属性の変数名を `__review_users` にし，`item.review_users` でアクセスできないようにしています．  
`item.review_users` のところで，`AttributeError: 'Item' object has no attribute 'review_users'` (Item オブジェクトは review_users という属性をもっていません) というエラーが出ています．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price
        self.review_cnt = 0
        self.review_score = 0.0
        self.__review_users = {}    # 変数名を隠す

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self.item_name}, unit_price={self.unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self.__review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self.item_name}: {self.unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self.__review_users[user_name] = score    # 1 ユーザにつき 1 レビュー
        self.review_cnt = len(self.__review_users)
        self.review_score = sum(self.__review_users.values()) / self.review_cnt  # 評点は平均点とする


item = Item("モンスターボール", 200)
item.review("サトシ", 5)

print(f"item_name={item.item_name}")
print(f"unit_price={item.unit_price}")
print(f"review_cnt={item.review_cnt}")
print(f"review_score={item.review_score}")
print(f"review_users={item.review_users}")  # item.review_users ではアクセスできない

"""
item_name=モンスターボール
unit_price=200
review_cnt=1
review_score=5.0
Traceback (most recent call last):
  File "example.py", line 33, in <module>
    print(f"review_users={item.review_users}")
AttributeError: 'Item' object has no attribute 'review_users'
"""
```

また，`item.__review_uesrs` のようにしてもアクセスできません．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price
        self.review_cnt = 0     # レビュー数
        self.review_score = 0.0   # レビューの評点
        self.__review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self.item_name}, unit_price={self.unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self.__review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self.item_name}: {self.unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self.__review_users[user_name] = score    # 1 ユーザにつき 1 レビュー
        self.review_cnt = len(self.__review_users)
        self.review_score = sum(self.__review_users.values()) / self.review_cnt  # 評点は平均点とする


item = Item("モンスターボール", 200)
item.review("サトシ", 5)

print(f"item_name={item.item_name}")
print(f"unit_price={item.unit_price}")
print(f"review_cnt={item.review_cnt}")
print(f"review_score={item.review_score}")
print(f"review_users={item.__review_users}")

"""
item_name=モンスターボール
unit_price=200
review_cnt=1
review_score=5.0
Traceback (most recent call last):
  File "hello3.py", line 33, in <module>
    print(f"review_users={item.__review_users}")
AttributeError: 'Item' object has no attribute '__review_users'
"""
```

`__review_uers` とすることにより，変数名は `_Item__review_users` のようにマングリングされます．  
`item._Item__review_users` とすれば一応アクセスできますが，変数名が合致してアクセスできてしまうのをある程度防ぐことができるようになっています．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price
        self.review_cnt = 0     # レビュー数
        self.review_score = 0.0   # レビューの評点
        self.__review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self.item_name}, unit_price={self.unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self.__review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self.item_name}: {self.unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self.__review_users[user_name] = score    # 1 ユーザにつき 1 レビュー
        self.review_cnt = len(self.__review_users)
        self.review_score = sum(self.__review_users.values()) / self.review_cnt  # 評点は平均点とする


item = Item("モンスターボール", 200)
item.review("サトシ", 5)

print(f"item_name={item.item_name}")
print(f"unit_price={item.unit_price}")
print(f"review_cnt={item.review_cnt}")
print(f"review_score={item.review_score}")
print(f"review_users={item._Item__review_users}")

"""
item_name=モンスターボール
unit_price=200
review_cnt=1
review_score=5.0
review_users={'サトシ': 5}
"""
```

しかしこの方法は混乱を招くとしてあんまり好まれていないようで，変数名の前に `__` (アンダースコア x 2) のかわりに `_` (アンダースコア x 1) をつけることのほうが多いです．  

(ここまで Extra)  

## シングルアンダースコアプリフィックス

変数を保護することはできませんが，外部から使用されたくない変数については変数名の前に `_` (アンダースコア x 1) をつけることで "この変数を外部から使うな" と明示するようにします．  
`_` に機能は何もなくただの目印ですが，慣習的に普通の変数名の前に `_` をつけないのでこれである程度アクセスを防ぐことができます．  
変数のアクセシビリティについては，例えば Java は setter，getter をつける (直接変数にアクセスさせず，getter, setter という関数を通して変数にアクセスさせる) のが標準的でかなり厳しいですが，Python はそこまで厳密にやらなくてもいいでしょって感じですかね．  

外部で使ってほしくないメソッドについても，メソッド名の前に `_` (アンダースコア x 1) をつけるようにします．  

次のコードでは，変数名の前に `_` をつけて `_review_users` とし，内部用の変数であることを明示しています．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self.item_name = item_name
        self.unit_price = unit_price
        self.review_cnt = 0     # レビュー数
        self.review_score = 0.0   # レビューの評点
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self.item_name}, unit_price={self.unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self.item_name}: {self.unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score    # 1 ユーザにつき 1 レビュー
        self.review_cnt = len(self._review_users)
        self.review_score = sum(self._review_users.values()) / self.review_cnt  # 評点は平均点とする


item = Item("モンスターボール", 200)
item.review("サトシ", 5)

print(f"item_name={item.item_name}")
print(f"unit_price={item.unit_price}")
print(f"review_cnt={item.review_cnt}")
print(f"review_score={item.review_score}")
print(f"review_users={item._review_users}")     # アクセスできるがアクセスしないようにする

"""
item_name=モンスターボール
unit_price=200
review_cnt=1
review_score=5.0
review_users={'サトシ': 5}
"""
```

# プロパティ (Propety)

今の Item クラスはすべての属性が公開属性です．  
基本は属性はすべて公開属性なのですが，Item クラスでは少しまずいことが起きます．  
item_name は勝手に値を更新されるといつの間にか商品名が変わってしまうことになります．  
また，review_cnt，review_score の値を直接更新すると，review メソッドの結果と合わなくなってしまいます．  
したがって，これらの属性は読み取り専用にするのが望ましいです．  
しかし，`_item_name`，`_review_cnt`，`_review_score` とするのは，値を読み取ることも制限してしまいます．  
これを解決する方法として，getter と setter の役割を見てからプロパティという手法を紹介します．  

getter，setter とは一般にオブジェクトの変数にアクセスする関数のことを言います．  
getter が値を読み取り，setter が値を設定する関数です．  
getter，setter を使う言語の代表として，例えば先の Item クラスを Java で書くと次のようになります．  

Java の文法についてはわからなくても大丈夫なので，getter と setter に注目してください．  
Item クラスで定義されている関数のうち， `getXXX` が getter，`setXXX` が setter です．  
Item クラスの変数をすべて `private` にして外部から直接変数を使用させないようにし，getter，setter を介してアクセスするようにしています．  
外部で使用する変数の一つ一つに getter と setter のペアが実装できますが，この Item クラスでは itemName，reviewCnt，reviewScore に setter を実装していません．  
これにより，itemName，reviewCnt，reviewScore は読み取り専用の変数になります．  
また，getter，setter に処理を書くことで，強制的に加工した値を代入したり取得したりすることができます．  

```java
package examples;

import java.util.HashMap;
import java.util.Map;

class Item {
    private String itemName;
    private int unitPrice;
    private int reviewCnt = 0;
    private double reviewScore = 0.0;

    private Map<String, Integer> reviewUsers = new HashMap<>();

    // Constructor
    public Item(String itemName, int unitPrice) {
        this.itemName = itemName;
        this.unitPrice = unitPrice;
    }

    // Getters
    public String getItemName() {
        return this.itemName;
    }

    public int getUnitPrice() {
        return this.unitPrice;
    }

    public int getReviewCnt() {
        return this.reviewCnt;
    }

    public double getReviewScore() {
        return this.reviewScore;
    }

    // S4tters
    public void setUnitPrice(int unitPrice) {
        this.unitPrice = unitPrice;
    }

    // Methods
    public void review(String userName, int score) {
        this.reviewUsers.put(userName, score);
        double t = 0;
        for (Integer s : this.reviewUsers.values()) {
            t += s;
        }
        this.reviewScore = t / this.reviewUsers.size();
    }
}

public class Example {
    public static void main(String[] args) {
        Item item = new Item("モンスターボール", 200);
        item.review("サトシ", 5);

        System.out.println("itemName=" + item.getItemName());       // itemName=モンスターボール
        System.out.println("unitPrice=" + item.getUnitPrice());     // unitPrice=200
        System.out.println("reviewCnt=" + item.getReviewCnt());     // reviewCnt=0
        System.out.println("reviewScore=" + item.getReviewScore()); // reviewScore=5.0

        item.setUnitPrice(20000);
        System.out.println("unitPrice=" + item.getUnitPrice());     // unitPrice=20000
    }
};
```

Java の実装例と同様のこと，つまり getter と setter を Python で実装するには **プロパティ** を使います．  
プロパティの定義には **デコレータ** を使います．  

デコレータとは，クラスやメソッドの上につける修飾子のことです．  
実態は対象の関数を修飾して返す関数ですが，文法の 1 つとして考えてください．  

`@property` は，メソッドの上につけるとそのメソッドを getter にするデコレータです．  
一方，`@<getter 名>.setter` は，メソッドの上につけるとそのメソッドを setter にするデコレータになります．  
これらの getter，setter をプロパティと呼びます．  

プロパティは属性と同じようにアクセスできます．  
getter の場合は `<オブジェクト>.<getter 名>` で値が取得でき，setter の場合は `<オブジェクト>.<setter 名> = <値>` で値を代入することができます．  

この 2 つのデコレータを使って Item クラスを実装し直すと，次のようになります．  
unit_price に getter，setter をつけたのは冗長です，setter を使いたかったので...  

getter，setter を設ける場合は，まず属性名の前に `_` をつけて外部から使わせないようにします．  
値を読み取りたい，あるいは設定したい属性の名前で getter と setter を定義します．  
すると，プロパティの仕様によって公開属性にアクセスするのと同じような書き方で，getter と setter を介して隠している属性にアクセスさせることができます．  
また，getter のみを定義すれば属性を読み取り専用にすることができます．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_cnt = 0     # レビュー数
        self._review_score = 0.0   # レビューの評点
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self._review_cnt}, review_score={self._review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self._review_score} star ({self._review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return self._review_cnt

    @property   # getter
    def review_score(self):
        return self._review_score

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score
        self._review_cnt = len(self._review_users)
        self._review_score = sum(self._review_users.values()) / self.review_cnt  # 評点は平均点とする


item = Item("モンスターボール", 200)
item.review("サトシ", 5)

print(f"item_name={item.item_name}")        # item.item_name() を呼び出している
print(f"unit_price={item.unit_price}")      # item.unit_price() (getter) を呼び出している
print(f"review_cnt={item.review_cnt}")      # item.review_cnt() を呼び出している
print(f"review_score={item.review_score}")  # item.review_score() を呼び出している

item.unit_price = 20000                     # item.unit_price(20000) (setter) を呼び出している
print(f"unit_price={item.unit_price}")      # unit_price=20000
```

Python には属性を private にする機能がないので，このようにしても `_<属性名>` で属性の値を変更されてしまう可能性は残ります．  
また，どれかの属性が変更されたときに変わってしまう計算結果を属性として保持するのはあんまり良くないです．  
そのため，計算結果を保持する属性はなるべくなくし，メソッドにするか getter の中に処理を書いて毎回計算するようにしましょう．  

例えば，Item クラスの review_cnt と review_score は計算する処理を getter に書いてその結果を返すようにします．  
すると review_cnt，review_score の値を取得するときに毎回 getter の中で計算されるので，いつでも正しい値が得られます．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        # 属性 review_cnt, review_score をなくしてプロパティだけにする
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        # item.review_cnt でアクセスされたとき毎回計算される
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        # item.review_score でアクセスされたとき毎回計算される
        user_num = len(self._review_users)
        if user_num == 0:
            return 0.0
        return sum(self._review_users.values()) / user_num

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score
        # review_cnt，review_score の処理をそれぞれの getter に移植


item = Item("モンスターボール", 200)
item.review("サトシ", 5)

print(f"item_name={item.item_name}")        # item_name=モンスターボール
print(f"unit_price={item.unit_price}")      # unit_price=200
print(f"review_cnt={item.review_cnt}")      # review_cnt=1
print(f"review_score={item.review_score}")  # review_score=5.0

item.unit_price = 20000
print(f"unit_price={item.unit_price}")      # unit_price=20000
```


# クラス属性

インスタンスを作らずにクラスからそのまま参照できる属性のことをクラス属性といいます．  
`<クラスオブジェクト>.<クラス属性>` でアクセスできます．  
インスタンスと全く同じように属性を参照できることからも察せられるように，Python ではクラスもオブジェクトの 1 つ (クラスオブジェクト) として実装されています．  
クラスオブジェクトはクラスの定義を内包するオブジェクトになります (だから `<クラスオブジェクト>.<クラス属性>` で参照できる)．  

Item クラスを取り扱う Shop クラスを作っていきます．  
今回はネットショップなので店舗は 1 つとし，インスタンスを作らない体で実装していくことにします．  

次のコードでは，Shop クラスにクラス属性として，ショップ名を表す shop_name，取り扱う商品を表す items を定義しています．  

```python
from pprint import pprint


class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        user_num = len(self._review_users)
        if user_num == 0:
            return 0
        return sum(self._review_users.values()) / user_num

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class Shop:
    shop_name = "タマムシデパート オンライン"
    items = []


Shop.items = [  # Shop に取扱商品を追加
    Item("モンスターボール", 200),
    Item("スーパーボール", 600),
    Item("ハイパーボール", 1200),
    Item("リピートボール", 1000),
    Item("タイマーボール", 1000)
]

print(Shop.shop_name)   # タマムシデパート オンライン
pprint(Shop.items)

"""
[Item(item_name=モンスターボール, unit_price=200, review_cnt=0, review_score=0, review_users={}),
 Item(item_name=スーパーボール, unit_price=600, review_cnt=0, review_score=0, review_users={}),
 Item(item_name=ハイパーボール, unit_price=1200, review_cnt=0, review_score=0, review_users={}),
 Item(item_name=リピートボール, unit_price=1000, review_cnt=0, review_score=0, review_users={}),
 Item(item_name=タイマーボール, unit_price=1000, review_cnt=0, review_score=0, review_users={})]
"""
```

クラス定義内からクラス属性にアクセスするには `cls.<クラス属性>` か `self.<クラス属性>` でアクセスできます (-> 練習問題)．  


# クラスメソッド

クラス属性と同様，インスタンスを作らずにクラスから直接参照できるメソッドをクラスメソッドといいます．  
クラスメソッドを実装するには，メソッド名の上にデコレータ `@classmethod` をつけてクラスメソッドであることを示します．  
また，インスタンスメソッドの第一仮引数が `self` だったのに対し，クラスメソッドでは自クラスの参照をもつ `cls` を第一仮引数にします．  
クラスメソッドは `<クラスオブジェクト>.<クラスメソッド>([引数 1, 引数 2, ...])` で呼び出します．  
このとき，第一実引数として暗黙的にクラスオブジェクトが第一仮引数 `cls` に渡されています．  

次のコードでは，item_name を引数にとり，Shop クラスの商品とその在庫数を管理するクラス属性 stock から同名の item オブジェクトがあればそれと在庫数を返し，なければ `None` を返すクラスメソッド `search` を実装しています．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        user_num = len(self._review_users)
        if user_num == 0:
            return 0
        return sum(self._review_users.values()) / user_num

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class Shop:
    shop_name = "タマムシデパート オンライン"
    stock = {}  # { 商品: 在庫数 }

    @classmethod
    def search(cls, item_name):
        """商品名から商品を検索する関数．
        見つかれば商品と在庫数を，見つからなければ None を返す
        """
        for item, num in cls.items.items():
            if item.item_name == item_name:
                return (item, num)
        return None


Shop.stock = {
    Item("モンスターボール", 200): 400,
    Item("スーパーボール", 600): 300,
    Item("ハイパーボール", 1200): 100,
    Item("リピートボール", 1000): 200,
    Item("タイマーボール", 1000): 200
}

res = Shop.search("モンスターボール")
print(res)  # (Item(item_name=モンスターボール, unit_price=200, review_cnt=0, review_score=0, review_users={}), 400)

res = Shop.search("マスターボール")
print(res)  # None
```

クラス属性と同様，クラス定義内からクラスメソッドには `cls.<クラスメソッド>` か `self.<クラスメソッド>` でアクセスできます．  


# スタティックメソッド (static method)

インスタンスを作らずに使用するメソッドとして，クラスメソッドのほかに **スタティックメソッド** があります．  
クラスメソッドとスタティックメソッドの違いは，クラスメソッドが第一仮引数に `cls` をもつのに対して，スタティックメソッドはもたない点です．  
したがって，スタティックメソッドはクラスには関係するがクラスの属性やメソッドに関わらないメソッドのときに定義されます．  
あんま使わないですし，よくわからないときはクラスメソッドにしといても特に問題ないと思います．  

スタティックメソッドはメソッドの上に `@staticmethod` をつけることで定義できます．  
次のコードでは，Shop クラスにスタティックメソッド bulk を定義しています．  
bulk メソッドは複数の Item を引数として与えると，それらをセット販売の商品にします．  
メソッド内で Shop クラスのクラス属性やメソッドを使わないが，Shop クラスに関係のあるメソッドなのでスタティックメソッドにしています．  


```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        user_num = len(self._review_users)
        if user_num == 0:
            return 0
        return sum(self._review_users.values()) / user_num

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class Shop:
    shop_name = "タマムシデパート オンライン"
    items = {}  # { 商品: 在庫数 }

    @staticmethod
    def bulk(*items):
        """複数の商品をセット販売用にまとめるメソッド"""
        item_names = []
        unit_prices = 0
        for item in items:
            item_names.append(item.item_name)
            unit_prices += item.unit_price
        item_name = " + ".join(item_names)
        return Item(item_name, unit_prices)

    @classmethod
    def search(cls, item_name):
        """商品名から商品を検索するメソッド．
        見つかれば商品と在庫数を，見つからなければ None を返す
        """
        for item, num in cls.items.items():
            if item.item_name == item_name:
                return (item, num)
        return None


poke_ball = Item("モンスターボール", 200)
great_ball = Item("スーパーボール", 600)
ultra_ball = Item("ハイパーボール", 1200)

standard_ball_set = Shop.bulk(poke_ball, great_ball, ultra_ball)
print(standard_ball_set)  # モンスターボール + スーパーボール + ハイパーボール: 2000: 0 star (0 reviews)

Shop.items = {
    pokemon_ball: 400,
    great_ball: 300,
    ultra_ball: 100,
    standard_ball_set: 100,
    Item("リピートボール", 1000): 200,
    Item("タイマーボール", 1000): 200
}
```


# 継承 (inheritance)

既存のクラスをベースにして，そこに属性やメソッドを追加して新しいクラスを定義することができます．  
この方法を **継承** (inheritance) と言います．  

今回は Item クラスをこのショップで売られている商品の最も基本のクラスとして， Item クラスを継承して EC ショップで売られている本の商品のクラス BookItem クラスを実装します．  

まずは単純に継承するとどうなるかを見てみましょう．  

次のコードでは，Item クラスを継承して新しく BookItem クラスを定義してます．  
継承元クラスを親クラス，親クラスを継承するクラスを子クラスと呼びます．  
`class <子クラス名>(親クラス名)` で継承できます．  
`pass` は何もしないことを示します．  

このように BookItem クラスには何も実装していませんが，Item クラスを継承しているので Item クラスに定義されている属性やメソッドがそのまま使えます．  
したがって，BookItem クラスは Item クラスとしても扱うことができます．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        return sum(self._review_users.values()) / len(self._review_users)

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class BookItem(Item):
    pass    # 何もしない


book_item = BookItem("Fluent Python", 6380)
book_item.review("サトシ", 5)

print(book_item.item_name)      # Fluent Python
print(book_item.unit_price)     # 6380
print(book_item.review_cnt)     # 1
print(book_item.review_score)   # 5.0
```

この BookItem クラスに，本の商品特有の属性を追加していきましょう．  
次の例では，属性 `item_name` のほかに商品を一意に特定できるよう `isbn` 属性を追加しています．  

BookItem クラスの属性は isbn だけがユニークであり，item_name と unit_price は Item クラスと共通です．  
そこで，BookItem クラスのコンストラクタの中では `super()` で親クラスを呼び出し，`super().__init__(item_name, unit_price)` で親クラスのコンストラクタを使って BookItem クラスのインスタンスを初期化しています．  
そのあと，`self._isbn = isbn` で isbn 属性を追加しています．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        return sum(self._review_users.values()) / len(self._review_users)

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class BookItem(Item):
    def __init__(self, item_name, unit_price, isbn):    # 仮引数に isbn を追加
        super().__init__(item_name, unit_price)     # 親クラスのコンストラクタを使ってインスタンスを初期化
        self._isbn = isbn   # isbn は BookItem 独自の属性

    @property
    def isbn(self):
        return self._isbn


book_item = BookItem("Fluent Python", 6380, "9784873118178")    # isbn を追加
book_item.review("サトシ", 5)

print(book_item.item_name)      # Fluent Python
print(book_item.unit_price)     # 6380
print(book_item.review_cnt)     # 1
print(book_item.review_score)   # 5.0

print(book_item.isbn)           # 9784873118178
```

BookItem クラスは Item クラスを継承しているので，Item クラスとしても扱うことができます．  
次のコードでは，Item クラスといっしょに Shop クラスの stock 属性に BookItem クラスのインスタンスを格納しています．  
また，Item クラスと同様に search メソッドで商品名から BookItem クラスのインスタンスを探すことができます．  
このように，子クラスを親クラスとまったく同じように扱える性質をオブジェクト指向の言葉で **ポリモーフィズム** (polymorphism : 多態性) といいます．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        user_num = len(self._review_users)
        if user_num == 0:
            return 0
        return sum(self._review_users.values()) / user_num

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class BookItem(Item):
    def __init__(self, item_name, unit_price, isbn):
        super().__init__(item_name, unit_price)
        self._isbn = isbn

    @property
    def isbn(self):
        return self._isbn


class Shop:
    shop_name = "タマムシデパート オンライン"
    items = {}  # { 商品: 在庫数 }

    @staticmethod
    def bulk(*items):
        """複数の商品をセット販売用にまとめるメソッド"""
        item_names = []
        unit_prices = 0
        for item in items:
            item_names.append(item.item_name)
            unit_prices += item.unit_price
        item_name = " + ".join(item_names)
        return Item(item_name, unit_prices)

    @classmethod
    def search(cls, item_name):
        """商品名から商品を検索するメソッド．
        見つかれば商品と在庫数を，見つからなければ None を返す
        """
        for item, num in cls.items.items():
            if item.item_name == item_name:
                return (item, num)
        return None


Shop.items = {
    Item("モンスターボール", 200): 400,
    Item("スーパーボール", 600): 300,
    Item("ハイパーボール", 1200): 100,
    Item("リピートボール", 1000): 200,
    Item("タイマーボール", 1000): 200,
    BookItem("Fluent Python", 6380, "9784873118178"): 10
}

res = Shop.search("Fluent Python")
print(res)  # (Item(item_name=Fluent Python, unit_price=6380, review_cnt=0, review_score=0, review_users={}), 10)
```


## オーバーライド (override)

親クラスにあるメソッドを子クラスで再定義することを，そのメソッドを **オーバーライド** するといいます．  

次のコードでは，Shop クラスを継承して本の商品に特化したオンラインショップのクラス BookShop を定義しています．  
BookShop では本の商品のみを取り扱うので，search メソッドで本の名前のほかに ISBN でも検索できると便利です．  
そこで，Shop クラスの search メソッドを BookItem オブジェクトの isbn 属性でも検索できるようにオーバーライドしています．  

```python
class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        user_num = len(self._review_users)
        if user_num == 0:
            return 0
        return sum(self._review_users.values()) / user_num

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class BookItem(Item):
    def __init__(self, item_name, unit_price, isbn):
        super().__init__(item_name, unit_price)
        self._isbn = isbn

    @property
    def isbn(self):
        return self._isbn


class Shop:
    shop_name = "タマムシデパート オンライン"
    items = {}  # { 商品: 在庫数 }

    @staticmethod
    def bulk(*items):
        """複数の商品をセット販売用にまとめるメソッド"""
        item_names = []
        unit_prices = 0
        for item in items:
            item_names.append(item.item_name)
            unit_prices += item.unit_price
        item_name = " + ".join(item_names)
        return Item(item_name, unit_prices)

    @classmethod
    def search(cls, item_name):
        """商品名から商品を検索するメソッド．
        見つかれば商品と在庫数を，見つからなければ None を返す
        """
        for item, num in cls.items.items():
            if item.item_name == item_name:
                return (item, num)
        return None


class BookShop(Shop):
    @classmethod
    def search(cls, item_name_or_isbn):
        """商品名とISBNから商品を検索するメソッド．
        見つかれば商品と在庫数を，見つからなければ None を返す
        """
        for item, num in cls.items.items():
            if item_name_or_isbn in (item.item_name, item.isbn):
                return (item, num)
        return None


BookShop.items = {
    BookItem("Fluent Python", 6380, "9784873118178"): 10,
    BookItem("Python データサイエンスハンドブック", 4620, "978873118413"): 15,
    BookItem("Python による数値計算とシミュレーション", 2475, "9784274221705"): 10,
    BookItem("Effective Python", 3960, "9784873119175"): 5,
    BookItem("ゼロから作る Deep Learning", 3740, "9784873117584"): 20
}

res = BookShop.search("978873118413")
print(res)  # (Item(item_name=Python データサイエンスハンドブック, unit_price=4620, review_cnt=0, review_score=0, review_users={}), 15)
```

## UserDict / UserList

dict や list の実装はとても精密です．  
そのため，dict や list といったデータ構造を継承したクラスを自作する場合は dict や list をそのまま継承するのではなく，継承しやすいように作られた collections モジュールの UserDict や UserList を使うのが良いです．  

ここでは，例として ShoppingCart クラスを実装します．  
ShoppingCart クラスに求められる機能は，複数の Item オブジェクトとその購入数を格納できること，合計金額が計算できることです．  
また，購入数の追加や減量，カート内の商品の削除が簡単にできると便利です．  
こういった機能は dict オブジェクトのデータ構造を利用できると実現できそうです．  

UserDict を継承して ShoppingCart クラスを実装すると次のようになります．  
実行例から，継承しただけで ShoppingCart オブジェクトが普通の dict と同じように扱えていることがわかります．  

UserDict に格納されているデータを使用する場合は，データがインスタンス属性の dict `data` に格納されているのでそれを使います．  
同様に，UserList の格納しているデータは list である `data` 属性にあります．  

```python
from collections import UserDict
from pprint import pprint


class Item:
    def __init__(self, item_name, unit_price):
        self._item_name = item_name
        self._unit_price = unit_price
        self._review_users = {}  # レビューしたユーザを管理

    def __repr__(self):
        """str 関数で呼び出されるメソッド．デバッグやログ用"""
        return f"Item(item_name={self._item_name}, unit_price={self._unit_price}, " +\
            f"review_cnt={self.review_cnt}, review_score={self.review_score}, " +\
            f"review_users={self._review_users})"

    def __str__(self):
        """str 関数で使われるメソッド"""
        return f"{self._item_name}: {self._unit_price}: {self.review_score} star ({self.review_cnt} reviews)"

    @property   # getter
    def item_name(self):
        return self._item_name

    @property   # getter
    def unit_price(self):
        return self._unit_price

    @unit_price.setter  # setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property   # getter
    def review_cnt(self):
        return len(self._review_users)

    @property   # getter
    def review_score(self):
        user_num = len(self._review_users)
        if user_num == 0:
            return 0
        return sum(self._review_users.values()) / user_num

    def review(self, user_name, score):
        """評点をつけるメソッド"""
        self._review_users[user_name] = score


class ShoppingCart(UserDict):
    @property
    def total_price(self):
        """カート内商品の合計金額を計算して返す"""
        total = 0
        # dict のデータは dict `data` に格納されている
        for item, num in self.data.items(): # for item, num in self.items() でも OK
            total += item.unit_price * num
        return total


# 普通の dict と似たような感じで初期化できる
cart = ShoppingCart({
    Item("モンスターボール", 200): 40,
    Item("スーパーボール", 600): 30,
})

pprint(cart)
"""
{Item(item_name=スーパーボール, unit_price=600, review_cnt=0, review_score=0, review_users={}): 300,
 Item(item_name=モンスターボール, unit_price=200, review_cnt=0, review_score=0, review_users={}): 400}
"""

# key を指定して value を追加できる
cart[Item("ハイパーボール", 1200)] = 10

pprint(cart)
"""
{Item(item_name=スーパーボール, unit_price=600, review_cnt=0, review_score=0, review_users={}): 300,
 Item(item_name=ハイパーボール, unit_price=1200, review_cnt=0, review_score=0, review_users={}): 100,
 Item(item_name=モンスターボール, unit_price=200, review_cnt=0, review_score=0, review_users={}): 400}
"""

# dict のメソッドが使える
cart.update(
    {
        Item("リピートボール", 1000): 20,
        Item("タイマーボール", 1000): 20,
    }
)

pprint(cart)
"""
{Item(item_name=タイマーボール, unit_price=1000, review_cnt=0, review_score=0, review_users={}): 20,
 Item(item_name=スーパーボール, unit_price=600, review_cnt=0, review_score=0, review_users={}): 30,
 Item(item_name=リピートボール, unit_price=1000, review_cnt=0, review_score=0, review_users={}): 20,
 Item(item_name=ハイパーボール, unit_price=1200, review_cnt=0, review_score=0, review_users={}): 10,
 Item(item_name=モンスターボール, unit_price=200, review_cnt=0, review_score=0, review_users={}): 40}
"""

# ShoppingCart 独自のプロパティ total_price でカート内の合計金額を取得
total = cart.total_price
print(total)    # 78000
```

# Enum クラス

Enum クラス (enumeration : 列挙) は，定数や一意な値に名前をつけて保持するクラスです．  
通常，定数は変数名を大文字にした変数に格納すればよいのですが，複数の定数をグループとしてまとめて管理したい場合は Enum クラスを使います．  

次のコードは，棒グラフを描画するプログラムで棒グラフに使用する色のコードを定数として定義したものです．  

```python
RED = "#ff000"
GREEN = "#008000"
BLUE = "#0000ff"
```

これをまとめて管理するため，Enum クラスを使用すると次のようになります．  
継承するため，`from enum import Enum` で enum モジュールの Enum クラスをインポートしています．  

```python
from enum import Enum


class BarChartColors(Enum):
    RED = "#ff0000"
    GREEN = "#008000"
    BLUE = "#0000ff"
```

Enum クラスの属性 (変数名と値のペア) のことを Enum クラスの **member** といいます．  
また，属性名を name，値を value と呼びます．  
例えば，属性 `RED = "#ff0000"`，`GREEN = "#008000"`，`BLUE = "#0000ff"` は BarChartColors の member であり，属性名 `RED` は member `RED` の name，値 `"#ff0000"` は member `RED` の value です．  

member には通常の属性と同様 `<Enum クラスオブジェクト>.<member>` でアクセスできます．  
また，member の name は `<member>.name`，member の value は `<member>.value` で取得できます．  
ただし，定数なので代入することはできません．  

```python
from enum import Enum


class BarChartColors(Enum):
    RED = "#ff0000"
    GREEN = "#008000"
    BLUE = "#0000ff"


red = BarChartColors.RED
print(red)          # BarChartColors.RED
print(red.name)     # RED
print(red.value)    # #ff0000
```

Enum クラスは iterable オブジェクトなので，for 文で要素を取得したり list 関数で list 化したりすることができます．  

```python

from enum import Enum


class BarChartColors(Enum):
    RED = "#ff0000"
    GREEN = "#008000"
    BLUE = "#0000ff"


for color in BarChartColors:
    print(color)

"""
name=RED, value=#ff0000
name=GREEN, value=#008000
name=BLUE, value=#0000ff
"""

colors = list(BarChartColors)
print(colors)
# [<BarChartColors.RED: '#ff000'>, <BarChartColors.GREEN: '#008000'>, <BarChartColors.BLUE: '#0000ff'>]
```

Enum クラスの member どうしが等しいかどうかを評価するには `is` 演算子を使います．  

```python
from enum import Enum


class BarChartColors(Enum):
    RED = "#ff0000"
    GREEN = "#008000"
    BLUE = "#0000ff"


print(BarChartColors.RED is BarChartColors.RED)     # True
print(BarChartColors.RED is BarChartColors.GREEN)   # False
```

str や int などほかのオブジェクトと比較するには `==` を使います．  

```python
from enum import Enum


class BarChartColors(Enum):
    RED = "#ff0000"
    GREEN = "#008000"
    BLUE = "#0000ff"


print(BarChartColors.RED == "RED")      # False
print(BarChartColors.RED == "#ff0000")  # False

print(BarChartColors.RED.name == "RED")         # True
print(BarChartColors.RED.value == "#ff0000")    # True

```

Enum クラスを使用する主要な場面の 1 つとして，関数のオプションを Enum クラスで定義しておくことが挙げられます．  
例えば，棒グラフを描画する関数 draw_bar_chart を実装する際，関数で使える色を Enum クラスで定義しておくことで使える色を明示することができます．  

関数のはじめに，オプションが有効なものであるかバリデーションを設けます．  
今回の例では，draw_bar_chart 関数で引数 color でとる有効なオプションは BarChartColors クラスの member のみとします．  
例えば str で引数 color をとった場合 `"red"`，`"RED"`，`"Red"` などの曖昧さが生まれますが，Enum クラスを使うと有効なオプションを厳密に定義できます．  

```python
from enum import Enum


class BarChartColors(Enum):
    RED = "#ff0000"
    GREEN = "#008000"
    BLUE = "#0000ff"


def draw_bar_chart(x_list, y_list, color):
    if color not in list(BarChartColors):
        raise ValueError("Invalid Argument: color must be member of BarChartColors.")

    print(f"drew a bar chart with {color.name}.")


x_list = list(range(10))
y_list = list(range(10))
draw_bar_chart(x_list, y_list, BarChartColors.RED)
# drew a bar chart with RED.

draw_bar_chart(x_list, y_list, "RED")
"""
Traceback (most recent call last):
  File "example.py", line 22, in <module>
    draw_bar_chart(x_list, y_list, "RED")
  File "example.py", line 12, in draw_bar_chart
    raise ValueError("Invalid Argument: color must be member of BarChartColors.")
ValueError: Invalid Argument: color must be member of BarChartColors.
"""
```

オプションだけを定義したい，つまり member の name だけが必要で value が重要でない場合には auto 関数を使って value を定義すると良いです．  
auto 関数は自動的に value を割り振ってくれる関数です．  

```python
from enum import Enum, auto


class BarChartColors(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


for color in BarChartColors:
    print(f"name={color.name}, value={color.value}")

"""
name=RED, value=1
name=GREEN, value=2
name=BLUE, value=3
"""
```

(Extra)  

Type Hint を使うと引数に何を渡せばいいかパッとわかっていい感じです．  

```python
from enum import Enum
from typing import Iterable


class BarChartColors(Enum):
    RED = "#ff0000"
    GREEN = "#008000"
    BLUE = "#0000ff"


def draw_bar_chart(x_list: Iterable[int or float], y_list: Iterable[int or float], color: BarChartColors):
    if color not in list(BarChartColors):
        raise ValueError("Invalid Argument: color must be member of BarChartColors.")

    print(f"drew a bar chart with {color.name}.")


x_list = list(range(10))
y_list = list(range(10))
draw_bar_chart(x_list, y_list, BarChartColors.RED)
# drew a bar chart with RED.

draw_bar_chart(x_list, y_list, "RED")
"""
Traceback (most recent call last):
  File "example.py", line 22, in <module>
    draw_bar_chart(x_list, y_list, "RED")
  File "example.py", line 12, in draw_bar_chart
    raise ValueError("Invalid Argument: color must be member of BarChartColors.")
ValueError: Invalid Argument: color must be member of BarChartColors.
"""
```

(ここまで Extra)  


(Extra)  

# namedtuple

namedtuple は要素に名前をつけられる tuple です．  
tuple とついていますが，実際にはクラスを作ることができます．  
属性はイミュータブルなので，読み取り専用の簡易クラスが必要なときに便利です．  

まず `namedtuple(<typename>, (属性名 1, 属性名 2, ...))` でクラスオブジェクトを作ります.  
引数にはクラス名と属性名を保持した iterable オブジェクトを渡します．  

インスタンスは通常のクラスと同じように作ることができます．  

```python
from collections import namedtuple


Item = namedtuple("Item", ("item_name", "unit_price"))

poke_ball = Item("モンスターボール", 200)
print(poke_ball.item_name)  # モンスターボール
print(poke_ball.unit_price)  # 200
```



# 特殊メソッド (special method)

特殊メソッドの数はとても多く，オブジェクトの振舞いの根幹に関わるため奥が深いです．  
詳しくは公式 doc (https://docs.python.org/ja/3/reference/datamodel.html) か著書 `Fluent Python` を読むことをおすすめします．  

ここでは Vector クラスの自作を通していくつかの特殊メソッド (special method, dunder method) とその機能を紹介していきます．  

Vector クラスは原点から伸びる n 次元ベクトルをモデルにしたものです．  
コンストラクタに各座標軸の値を格納した iterable オブジェクトを与えて初期化します．  
例えば，`Vector([3, 4, 5])` は xyz 空間内の点 (3, 4, 5) に伸びるベクトルを表します．  

Vector オブジェクトはミュータブルであるとし，`__init__` メソッド内で引数として渡された iterable オブジェクトを list 化して array 属性に代入します．  
`__str__` メソッドで str 関数の返り値としての文字列を，`__repr__` メソッドで repr 関数の返り値としてデバッグ用の文字列を定義します．  

```python
from typing import Iterable


class Vector:
    def __init__(self, array: Iterable[int or float]):
        self.array = list(array)

    def __str__(self):
        return f"<{', '.join([str(a) for a in self.array])}>"

    def __repr__(self):
        return f"Vector({repr(self.array)})"


v = Vector([3, 4, 5])
print(v)        # <3, 4, 5>
print(repr(v))  # Vector([3, 4, 5])
```

続いて，`__len__` メソッドで len 関数の返り値として Vector オブジェクトの次元数を，`__abs__` メソッドで abs 関数の返り値として Vector オブジェクトのノルム (大きさ) を返すようにします．  

```python
from typing import Iterable


class Vector:
    def __init__(self, array: Iterable[int or float]):
        self.array = list(array)

    def __str__(self):
        return f"<{', '.join([str(x) for x in self.array])}>"

    def __repr__(self):
        return f"Vector({repr(self.array)})"

    def __len__(self):
        return len(self.array)

    def __abs__(self):
        return sum([x * x for x in self.array]) ** 0.5


v = Vector([3, 4, 5])
print(len(v))   # 3
print(abs(v))   # 7.0710678118654755
```

`-` 演算子で符号を反転できるよう `__neg__` メソッドを定義します．  
すべての要素の符号を反転した新しい Vector オブジェクトを返すようにします．  

```python
from typing import Iterable


class Vector:
    def __init__(self, array: Iterable[int or float]):
        self.array = list(array)

    def __str__(self):
        return f"<{', '.join([str(a) for a in self.array])}>"

    def __repr__(self):
        return f"Vector({repr(self.array)})"

    def __len__(self):
        return len(self.array)

    def __abs__(self):
        return sum([a * a for a in self.array]) ** 0.5

    def __neg__(self):
        return Vector([-a for a in self.array])


v1 = Vector([3, 4, 5])
print(-v1)  # <-3, -4, -5>
```

次に，ベクトルどうしの加減乗算ができるよう `__add__` メソッドと `__sub__` メソッド，`__mul__` メソッドを定義します．  
これは **演算子のオーバーロード** (overload) にあたり，Vector オブジェクトどうしの加減算に `+` 演算子と `-` 演算子が使えるようになります．  
オーバーロードとは一般にシグネチャ (関数名 + 引数の数や型 + 返り値の型) が異なる同名の関数やメソッドを定義することをいいます．  
演算子をオーバーロードすることで，`+` 演算子と `-` 演算子が作用するときオペランドが Vector クラスであれば Vector クラスで定義された `__add__` メソッドと `__sub__` メソッドが使用されることになります．  
(個人的にはオーバーライドな感じがするんですが公式 doc いわくオーバーロードらしいです : https://docs.python.org/ja/3/reference/datamodel.html)

オペランドの Vector オブジェクトの次元数が異なる場合は演算が定義できないので ValueError を送出するようにします．  

また，`__mul__` メソッドで乗算を定義します．  
Vector オブジェクトどうしの乗算は内積を，Vector オブジェクトと数値の場合はスカラー籍を返すようにします．  

```python
from typing import Iterable


class Vector:
    def __init__(self, array: Iterable[int or float]):
        self.array = list(array)

    def __str__(self):
        return f"<{', '.join([str(a) for a in self.array])}>"

    def __repr__(self):
        return f"Vector({repr(self.array)})"

    def __len__(self):
        return len(self.array)

    def __abs__(self):
        return sum([a * a for a in self.array]) ** 0.5

    def __neg__(self):
        return Vector([-a for a in self.array])

    def __add__(
        self,
        other   # Vector
    ):
        if len(self.array) != len(other.array):
            raise ValueError(
                "Both the dimension of Vector object  must the same; " +
                f"{len(self.array)} != {len(other.array)}"
            )
        return Vector([a + b for a, b in zip(self.array, other.array)])

    def __sub__(
        self,
        other   # Vector
    ):
        if len(self.array) != len(other.array):
            raise ValueError(
                "Both the dimension of Vector object  must the same; " +
                f"{len(self.array)} != {len(other.array)}"
            )
        return Vector([a - b for a, b in zip(self.array, other.array)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.array])
        elif isinstance(other, Vector):
            return sum([a * b for a, b in zip(self.array, other.array)])
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(other).__name__}'")


v1 = Vector([3, 4, 5])
v2 = Vector([1, 5, 9])

print(v1 + v2)  # <4, 9, 14>
print(v1 - v2)  # <2, -1, -4>
print(v2 - v1)  # <-2, 1, 4>

print(v1 * v2)  # 68
print(v1 * 10)  # <30, 40, 50>
```

次に，比較演算子をオーバーロードしていきます．  
`==` 演算子の働きは `__eq__` メソッドで定義できます．  
Vector オブジェクトの `==` による評価は，両 Vector オブジェクトの成分が等しいとき `True`，そうでないときは `False` を返すようにします．  

`<` 演算子の働きは `__lt__` メソッドで，`>` 演算子の働きは `__gt__` メソッドで定義できます．  
また，`<=` 演算子の働きは `__le__` メソッドで，`>=` 演算子の働きは `__ge__` メソッドで定義できます．  
Vector オブジェクトどうしの大小関係はノルムによって，Vector オブジェクトと数値の大小関係はノルムと数値によって評価することにします．  

比較演算子の作用を定義したので，Vector オブジェクトの list をノルムの大小関係にしたがってソートできます．  

```python
from typing import Iterable


class Vector:
    def __init__(self, array: Iterable[int or float]):
        self.array = list(array)

    def __str__(self):
        return f"<{', '.join([str(a) for a in self.array])}>"

    def __repr__(self):
        return f"Vector({repr(self.array)})"

    def __len__(self):
        return len(self.array)

    def __abs__(self):
        return sum([a * a for a in self.array]) ** 0.5

    def __neg__(self):
        return Vector([-a for a in self.array])

    def __add__(
        self,
        other   # Vector
    ):
        if len(self.array) != len(other.array):
            raise ValueError(
                "Both the dimension of Vector object  must the same; " +
                f"{len(self.array)} != {len(other.array)}"
            )
        return Vector([a + b for a, b in zip(self.array, other.array)])

    def __sub__(
        self,
        other   # Vector
    ):
        if len(self.array) != len(other.array):
            raise ValueError(
                "Both the dimension of Vector object  must the same; " +
                f"{len(self.array)} != {len(other.array)}"
            )
        return Vector([a - b for a, b in zip(self.array, other.array)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.array])
        elif isinstance(other, Vector):
            return sum([a * b for a, b in zip(self.array, other.array)])
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(other).__name__}'")

    def __eq__(
        self,
        other   # Vector
    ):
        return self.array == other.array

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return abs(self) < other
        elif isinstance(other, Vector):
            return abs(self) < other
        else:
            raise TypeError(
                f"unsupported operand type(s) for <: '{type(self).__name__}' and '{type(other).__name__}'")

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return abs(self) > other
        elif isinstance(other, Vector):
            return abs(self) > other
        else:
            raise TypeError(
                f"unsupported operand type(s) for >: '{type(self).__name__}' and '{type(other).__name__}'")

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return abs(self) <= other
        elif isinstance(other, Vector):
            return abs(self) <= other
        else:
            raise TypeError(
                f"unsupported operand type(s) for <=: '{type(self).__name__}' and '{type(other).__name__}'")

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return abs(self) >= other
        elif isinstance(other, Vector):
            return abs(self) >= other
        else:
            raise TypeError(
                f"unsupported operand type(s) for >=: '{type(self).__name__}' and '{type(other).__name__}'")


v1 = Vector([3, 4, 5])
v2 = Vector([1, 5, 9])
v3 = Vector([3, 4, 5])

print(abs(v1))  # 7.0710678118654755
print(abs(v2))  # 10.344080432788601

print(v1 == v2)  # False
print(v1 == v3)  # True

print(v1 > v2)  # False
print(v1 >= v2)  # False
print(v1 <= v3)  # True
print(v1 < v2)  # True


vectors = [v1, v2, v3]
vectors.sort()
print(vectors)  # [Vector([3, 4, 5]), Vector([3, 4, 5]), Vector([1, 5, 9])]
```

こんな感じで，特殊メソッドで組込み関数や演算子の働きを定義することができます．  
実務で使えるか使えないかは別として，クラスを自作するのはとても楽しいのでぜひ遊んでみてください．  

(ここまで Extra)  

# 練習問題

## Q 1

タスクを管理するクラスを実装することになりました．  
必要なクラスを順に実装していきましょう．  

### Q 1 - 1

タスクの情報を保持する Task クラスを実装しましょう．  
仕様は以下のようになります．  

|インスタンス属性|説明|
|:---:|:---:|
|`content: str`|タスクの内容|
|`created: str`|タスクが作られた日付|
|`deadline: str`|タスクの期日|
|`finished: bool`|タスクが完了した場合 `True`，そうでない場合 `False`|

|インスタンスメソッド|説明|
|:---:|:---:|
|`__init__(self, content: str, created: str, deadline: str)`|コンストラクタ．属性 content, created, deadline を引数 content, created, deadline で初期化する|
|`__repr__(self) -> str`|Task オブジェクトであることとインスタンス属性を明示する|
|`done(self)`|属性 finished を `True` にする|

使用例  

```python
task = Task("Open a new issue", "2020-08-01", "2020-08-07")
print(task)
# Task(content=Open a new issue, created=2020-08-01, deadline=2020-08-07)
```

### Q 1 - 2

複数のタスクを保持し，タスクをタスクが作られた日付かタスクの期日でソートする機能を持つ Schedule クラスを実装しましょう．  
Schedule オブジェクトが保持する Task オブジェクトの list は，Task オブジェクトの deadline 属性でソートしておくことにします．  

|インスタンス属性|説明|
|:---:|:---:|
|`tasks: List[Task]`|Task オブジェクトの list を保持する|

|クラス属性|説明|
|:---:|:---:|
|`CREATED: int`|タスクをソートするインスタンスメソッド sorted メソッドのオプション．enum モジュールの `auto()` で値を振ること|
|`DEADLINE: int`|タスクをソートするインスタンスメソッド sorted メソッドのオプション．enum モジュールの `auto()` で値を振ること|

|インスタンスメソッド|説明|
|:---:|:---:|
|`__init__(self, tasks: Iterable[Task])`|コンストラクタ．Task オブジェクトを格納する iterable オブジェクトを引数にとり，list にして tasks 属性を初期化する|
|`__len__(self) -> int`|属性 tasks の要素数を返す|
|`push(self, task)`|Task オブジェクトを引数にとり tasks 属性に追加する．そのあと tasks 属性を `tasks.deadline` でソートする|
|`get(self, index: int) -> Task`|属性 tasks の `index` 番目の要素を返す|
|`top(self) -> Task`|属性 tasks の 0 番目の要素を返す|
|`sorted(self, option: Schedule.CREATED or Schedule.DEADLINE) -> List[Task]`|option が `Schedule.CREATED` であれば属性 tasks を Tasks オブジェクトの created 属性で，`Schedule.DEADLINE` であれば deadline 属性でソートした新しい list を返す．option がどちらでもない場合は ValueError を送出する．もとの tasks 属性には変更を加えないこと．|
|`archive(self)`|finished 属性が `True` の Task オブジェクトを tasks 属性から取り除く|

使用例  

```python
from enum import auto
from pprint import pprint


schedule = Schedule([
    Task("Send a Pull Request", "2020-08-30", "2020-09-02"),
    Task("Open a new issue", "2020-08-01", "2020-08-07"),
    Task("Fix bug", "2020-08-13", "2020-08-25"),
])

schedule.push(Task("Review a Pull Request", "2020-08-15", "2020-08-20"))
print(len(schedule))    # 4

task1 = schedule.top()
print(task1)
# Task(content=Open a new issue, created=2020-08-01, deadline=2020-08-07)

sorted_by_deadline = schedule.sorted(Schedule.DEADLINE)
pprint(sorted_by_deadline)
"""
[Task(content=Open a new issue, created=2020-08-01, deadline=2020-08-07),
 Task(content=Review a Pull Request, created=2020-08-15, deadline=2020-08-20),
 Task(content=Fix bug, created=2020-08-13, deadline=2020-08-25),
 Task(content=Send a Pull Request, created=2020-08-30, deadline=2020-09-02)]
"""

sorted_by_created = schedule.sorted(Schedule.CREATED)
pprint(sorted_by_created)
"""
[Task(content=Open a new issue, created=2020-08-01, deadline=2020-08-07),
 Task(content=Fix bug, created=2020-08-13, deadline=2020-08-25),
 Task(content=Review a Pull Request, created=2020-08-15, deadline=2020-08-20),
 Task(content=Send a Pull Request, created=2020-08-30, deadline=2020-09-02)]
"""

task2 = schedule.get(2)
print(task2)
# Task(content=Fix bug, created=2020-08-13,deadline=2020-08-25, finished=False)

task2.done()
print(task2)
# Task(content=Fix bug, created=2020-08-13,deadline=2020-08-25, finished=True)

schedule.archive()
pprint(schedule.tasks)
"""
[Task(content=Open a new issue, created=2020-08-01,deadline=2020-08-07, finished=False),
 Task(content=Review a Pull Request, created=2020-08-15,deadline=2020-08-20, finished=False),
 Task(content=Send a Pull Request, created=2020-08-30,deadline=2020-09-02, finished=False)]
"""
```

## Q 2

ある社内システムのログインシステムを実装することになりました．  
ログインシステムの動作に必要なクラスを順に実装していきましょう．  

### Q 2 - 1

システムに登録されているユーザ情報を保持する User クラスを実装してみましょう．  
仕様は以下のようになります．  

|インスタンス属性|説明|
|:---:|:---:|
|`_email: str`|ユーザのメールアドレス|
|`password: str`|ユーザのログインパスワード|
|`_userid: str`|ユーザ ID．メールアドレスの `@` より前の部分を自動的にユーザ ID に設定する|

|インスタンスメソッド|説明|
|:---:|:---:|
|`__init__(self, email: str. password: str)`|コンストラクタ．属性 `_email`，password を 引数 email, password で初期化する|
|`__repr__(self) -> str`|User オブジェクトであることとインスタンス属性を明示する|
|`__str__(self) -> str`|ユーザ ID を返す|
|`_make_userid(self, email: str) -> str`|メールアドレスの `@` より前の部分の文字列を返す|

|getter (`@property`)|説明|
|:---:|:---:|
|`email(self) -> str`|メールアドレスを返す|
|`userid(self) -> str`|ユーザ ID を返す|

|setter (`<プロパティ名>.setter`)|説明|
|:---:|:---:|
|`email(self, email: str)`|メールアドレスを設定する．同時にユーザ ID も更新する|

使用例  

```python
user1 = User("user1@example.com", "password1")
print(user1.email)      # user1@example.com
print(user1.password)   # password1
print(user1.userid)     # user1

user1.email = "user1.new@example.com"
print(user1.email)      # user1.new@example.com
print(user1.userid)     # user1.new
```

### Q 2 - 2

ログインしようとしているユーザを表す LoginUser を実装しましょう．  
ログイン画面で入力されたユーザ ID とパスワードをインスタンス属性に保持します．  

|インスタンス属性|説明|
|:---:|:---:|
|`userid: str`|ログイン画面で入力されたユーザ ID|
|`password: str`|ログイン画面で入力されたパスワード|

|インスタンスメソッド|説明|
|:---:|:---:|
|`__init__(self, userid: str, password: str)`|コンストラクタ．属性 userid，password を 引数 userid，password で初期化する|

使用例  

```python
login_user1 = LoginUser("user1", "password1")
print(login_user1.userid)   # user1
print(login_user1.password)  # password1
```

### Q 2 - 3

ログイン機能を持つ LoginSystem クラスを実装しましょう．  
このクラスはインスタンスを作らずに使います．  
クラス属性の list `users` に User オブジェクトを格納し，ログインしようとしている LoginUser オブジェクトのユーザ ID とパスワードが `users` のいずれかの User オブジェクトのユーザ ID とパスワードに合致する場合にログインを許可します．  

|クラス属性|説明|
|:---:|:---:|
|`users: List[User]`|社内システムに登録されている User オブジェクトを格納する|

|クラスメソッド|説明|
|:---:|:---:|
|`authorize(cls, login_user: LoginUser) -> User or None`|引数 login_user のユーザ ID とパスワードと一致する User オブジェクトが属性 users の中にあればその User オブジェクトを，なければ `None` を返す|

使用例  

```python
UserSystem.users = [
    User("user1@example.com", "password1"),
    User("user2@example.com", "password2"),
    User("user3@example.com", "password3"),
]

login_user1 = LoginUser("user1", "password1")
res = UserSystem.authorize(login_user1)
print(res)  # user1

login_user2 = LoginUser("user2", "PASSWORD2")
res = UserSystem.authorize(login_user2)
print(res)  # None
```

## Q 3

普通の list オブジェクトの機能に加えて，格納している数値データの統計情報を計算できる StatsList クラスを実装しましょう．  

基本的な統計情報である平均，分散，標準偏差は，N 個のデータを `x1, x2, ..., xN` として以下の数式で計算できます．  

![stats](stats.png)

以下のインスタンス属性とインスタンスメソッドを実装して StatsList クラスを作ってみましょう．  
また，例を参考に StatsList オブジェクトで実際に平均，分散，標準偏差を計算してみましょう．  

|インスタンス属性|説明|
|:---:|:---:|
|`data: List[int or float]`|数値データを格納する|

|インスタンスメソッド|説明|
|:---:|:---:|
|`__init__(self, data: Iterable[int or float])`|仮引数に int あるいは float オブジェクトを保持した iterable オブジェクト data をとり，list にしてインスタンス属性 data に代入する|
|`mean(self) -> float`|格納しているデータの平均を計算して返す|
|`var(self) -> float`|格納しているデータの分散を計算して返す|
|`std(self) -> float`|格納しているデータの標準偏差を計算して返す|


例 1. 区間 `0.0 <= n < 1.0` で特に特徴のないデータ  

```python
import random
random.seed(0)  # シードを固定することで同じ乱数が得られる

# 0.0 <= n < 1.0 でランダムな乱数を 100'000 個生成してデータとする
data = []
for _ in range(100_000):
    data.append(random.random())
# (Extra) data = [random.random() for _ in range(100_000)]

stats_lst = StatsList(data)
print(f"mean={stats_lst.mean()}")   # mean=0.4994751702579762
print(f"var={stats_lst.var()}")     # var=0.08361639460894141
print(f"std={stats_lst.std()}")     # std=0.28916499547652963
```


例 2. 標準正規分布 (平均 0.0，標準偏差 1.0) に従うデータ (のつもり)  

```python
import random
random.seed(0)  # シードを固定することで同じ乱数が得られる

# 標準正規分布をシミュレートする乱数を 100'000 個生成してデータとする
data = []
for _ in range(100_000):
    data.append(random.gauss(0, 1))
# (Extra) data = [random.gauss(0, 1) for _ in range(100_000)]


stats_lst = StatsList(data)
print(f"mean={stats_lst.mean()}")   # mean=0.005310303456398197
print(f"var={stats_lst.var()}")     # var=0.9971375617592916
print(f"std={stats_lst.std()}")     # std=0.9985677552170867
```


例 3. 指数分布 (`λ = 0.5`) に従うデータ (のつもり)  

```python
import random
random.seed(0)  # シードを固定することで同じ乱数が得られる

# lambda = 0.5 の指数分布をシミュレートする乱数を 100'000 個生成してデータとする
data = []
for _ in range(100_000):
    data.append(random.expovariate(0.5))
# (Extra) data = [random.expovariate(0.5) for _ in range(100_000)]


stats_lst = StatsList(data)
print(f"mean={stats_lst.mean()}")   # mean=1.9980466260331897
print(f"var={stats_lst.var()}")     # var=3.9834215502219186
print(f"std={stats_lst.std()}")     # std=1.995851084179859
```


## Q 4

現在地から目的地までの経路の候補の中からかかる時間や交通費をもとに最適なものを選択するプログラムを実装してみましょう．  

このプログラムでは次の 4 つのクラスを使います．  

|クラス|説明|
|:---:|:---:|
|Direction|実際の交通手段を表すクラス|
|Route|経路を表す list クラス．複数の Direction オブジェクトを保持する|
|Navi|経路を選択するクラス．複数の Route クラスを保持し，条件に合致する Route クラスを選択する機能をもつ|
|Way|交通手段の種類を表す Enum クラス|

### Direction クラス

Directoin クラスは実際の交通手段を表すクラスです．  
以下のようなインスタンス属性とこれらを初期化する `__init__` メソッドを持ちます．  

|インスタンス属性|説明|例|
|:---:|:---:|:---:|
|name: str|交通手段の名称|train1, bus2|
|way: Way|交通手段|Way.TRAIN, Way.BUS|
|duration: int|所要時間 (分)|35, 50|
|cost: int|費用|250, 400|

|インスタンスメソッド|説明|例|
|:---:|:---:|:---:|
|`__init__(self, name: str, way: Way, duration: int, cost: int)`|コンストラクタ|問題の入力例参照|

### Route クラス

経路を表すクラスです．  
複数の交通手段 (Direction オブジェクト) を保持します．  
list オブジェクトとしても扱えるよう UserList クラスを継承してください．  

インスタンス属性は Direction クラスを格納する data のみです．  
Direction オブジェクトを保持した iterable オブジェクトを仮引数にとる `__init__` メソッドで data を Direction オブジェクトの list に初期化できるようにしましょう．  

|インスタンス属性|説明|例|
|:---:|:---:|:---:|
|data: List\[Direction\]|Direction オブジェクトを格納する|`[Direction("train1", Way.TRAIN, 30, 250), Direction("bus2", Way.BUS, 20, 200)]`|

|インスタンスメソッド|説明|例|
|:---:|:---:|:---:
|`__init__(self, directions: Iterable[Direction])`|Direction オブジェクトを保持した iterable オブジェクトを引数にとるコンストラクタ．iterable オブジェクトを list にして data に格納する|問題の入力例参照|
|`__repr__(self) -> str`|Route オブジェクトであることを明示し，経路が持つ交通手段の名称 (`<Direction オブジェクト>.name`) を列挙して返す|`print(repr(route1)) # Route(train1->train2->bus1)`|
|`__str__(self) -> str`|経路が持つ交通手段の名称 (`<Direction オブジェクト>.name`) を列挙して返す|`print(route1) # train1->train2->bus1`|

|getter (`@property`) |説明|例|
|:---:|:---:|:---:|
|`durations(self) -> int`|経路の所要時間，すなわち保持する交通手段の所要時間の合計を返す|`print(route1.durations) # 65`|
|`costs(self) -> int`|経路の費用，すなわち保持する交通手段の費用の合計を返す|`print(route1.costs) # 750`|

### Navi クラス

複数の経路 (Route オブジェクト) を保持するクラスです．  
自身が保持する経路の中から条件に合致した経路を選択して返すメソッドを持ちます．  

また，Route オブジェクトを格納するインスタンス属性 routes を持ちます．  
Route オブジェクトを保持した iterable オブジェクトを仮引数にとる `__init__` メソッドで routes を Route オブジェクトの list に初期化できるようにしましょう．  

|インスタンス属性|説明|例|
|:---:|:---:|:---:|
|`routes: List[Route]`|Route オブジェクトを格納する|`[route1, route2, route3]`|

|インスタンスメソッド|説明|例|
|:---:|:---:|:---:|
|`__init__(self, routes: Iterable[Route])`|Route オブジェクトを保持した iterable オブジェクトを引数にとるコンストラクタ．iterable オブジェクトを list にして routes に格納する|問題の入力例参照|
|`easiest(self, way: Way or None = None)`|交通手段の種類 (Way メンバー) をとるデフォルト引数 way を持つ．way が `None` の場合はすべての経路の中から最も乗り換えの少ない経路を返す．way が Way オブジェクトの場合は交通手段の種類がすべて way に合致する経路の中から最も乗り換え回数の少ない (交通手段の少ない) 経路を返す．複数ある場合はそのうちの 1 つを返す．条件に合致した経路が見つからなければ `None` を返す．way が `None` あるいは Way のメンバーでなければ `ValueError` を送出する|`print(navi.easiest()) # train1->train2->bus1`|
|`fastest(self, way: Way or None = None)`|交通手段の種類 (Way メンバー) をとるデフォルト引数 way を持つ．way が `None` の場合はすべての経路の中から最も所要時間の短い経路を返す．way が Way オブジェクトの場合は交通手段の種類がすべて way に合致する経路の中から最も所要時間の少ない経路を返す．複数ある場合はそのうちの 1 つを返す．条件に合致した経路が見つからなければ `None` を返す．way が `None` あるいは Way メンバーでなければ `ValueError` を送出する|`print(navi.fastest(Way.TRAIN)) # train1->train2->bus1`|
|`cheapest(self, way: Way or None = None)`|交通手段の種類 (Way メンバー) をとるデフォルト引数 way を持つ．way が `None` の場合はすべての経路の中から最も費用の少ない経路を返す．way が Way オブジェクトの場合は交通手段の種類がすべて way に合致する経路の中から最も費用の少ない経路を返す．複数ある場合はそのうちの 1 つを返す．条件に合致した経路がなければ `None` を返す．way が `None` あるいは Way メンバーでなければ `ValueError` を送出する|`print(navi.cheapest()) # train1->train2->bus1`|

### Q

Navi オブジェクトを使って以下の経路を出力してください
- 一番乗り換えが少ない経路
- 一番所要時間の短い経路
- 一番費用の少ない経路
- 電車のみを使う経路で一番費用の少ない経路

例 1.  

```python
route1 = Route([
    Direction("train1", Way.TRAIN, 30, 250),
    Direction("train2", Way.TRAIN, 20, 200),
    Direction("bus1", Way.BUS, 15, 200),
])

route2 = Route([
    Direction("train1", Way.TRAIN, 30, 250),
    Direction("train3", Way.TRAIN, 40, 450),
])

route3 = Route([
    Direction("train4", Way.TRAIN, 35, 300),
    Direction("train5", Way.TRAIN, 50, 400)
])


navi = Navi([route1, route2, route3])
print("easiest |", navi.easiest())      # easiest | train1->train3
print("fastest |", navi.fastest())      # fastest | train1->train2->bus1
print("cheapest |", navi.cheapest())    # cheapest | train1->train2->bus1
print("cheapest by train |", navi.cheapest(Way.TRAIN))     # cheapest by train | train1->train3
```

例 2.  

```python
route1 = Route([
    Direction("train1", Way.TRAIN, 40, 350),
    Direction("train2", Way.TRAIN, 10, 200),
    Direction("bus1", Way.BUS, 10, 200),
])

route2 = Route([
    Direction("train1", Way.TRAIN, 40, 350),
    Direction("bus2", Way.BUS, 40, 350),
])

route3 = Route([
    Direction("train4", Way.TRAIN, 20, 200),
    Direction("bus3", Way.BUS, 30, 200),
    Direction("bus4", Way.BUS, 35, 250),
])


navi = Navi([route1, route2, route3])
print("easiest |", navi.easiest())      # easiest | train1->bus2
print("fastest |", navi.fastest())      # fastest | train1->train2->bus1
print("cheapest |", navi.cheapest())    # cheapest | train4->bus3->bus4
print("cheapest by train |", navi.cheapest(Way.TRAIN))  # cheapest by train | None
```




## Q

setter に処理をはさむ