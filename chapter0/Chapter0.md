# 準備

## リポジトリのクローン / ダウンロード

Git が使える方は本リポジトリを次のようにクローンしてください．  

```
git clone https://github.com/1izard/python-tutorial.git
```

Git とはなんぞやという方は Download ZIP をクリックして zip ファイルをダウンロードし任意のディレクトリに解凍してください．  


## 最初のプログラム

VSCode を実行すると Welcom ページが開きます．  
Start の項目の `Open folder...` をクリックして python-tutorial ディレクトリを選択しましょう．  
すると VSCode で python-tutorial ディレクトリを開くことができます．  

各 chapter ディレクトリには作業用 work ディレクトリが作ってあります．  
この中にプログラムを作って実行するようにしましょう．  
まずは `chapter0/work` ディレクトリに `hello.py` を作ってみます．  

左ペインの一番上にあるファイルマークをクリックすると，python-tutorial ディレクトリ以下のファイルの一覧を EXPLORER で見ることができます．  

EXPLORER 上で work ディレクトリを右クリックし，`New File` を選択して新規ファイルを作ります．  
ファイル名は hello.py にします．  

EXPLORER 上で hello.py をクリックすると hello.py を開くことができます．  
中身はこんな感じにしましょう．  

```python
print("Hello, World!")
```


## コンソール
プログラムの実行結果を標準出力 (standard output; コンソールに出力すること) するには，組込み関数 print を使います．  

コンソールを開くには，EXPLORER 上で work ディレクトリを右クリックし，`Open in Integrated Terminal` を選択します．  
エディタ下部にコンソールが表示されます．  



例1.

```python
# ex1.py
# 半径r=2の円の面積
PI = 3.14159265359
r = 2
s = r * r * PI
print(s)
```

```
// コンソール (現在ex1.pyのあるディレクトリにいる)
$ python ex1.py (あるいはpython3 ex1.pyを入力してエンターキー)
12.56637061436  (実行結果)
```

例2.  
複数の値(何個でもOK)を与えると " "(空白)区切りで出力します．

```python
# ex2.py
# サイコロの出る目の期待値
s = 1 + 2 + 3 + 4 + 5 + 6
t = 6
ans = s / t
print("ans =", s / t)
```

```
// コンソール (現在ex2.pyのあるディレクトリにいる)
$ python ex2.py (あるいはpython3 ex2.pyを入力してエンターキー)
ans = 3.5             (実行結果)
```



