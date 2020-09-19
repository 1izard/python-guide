# Chapter 0 準備


# Python のインストール

以下を参考に最新バージョンをインストールしてください．  

- Windows: https://www.python.jp/install/windows/index.html
  - フル・インストーラ版の方をインストール
  - コマンドプロンプトで `python` コマンドか `py` コマンドが実行できるところまで (片方実行できれば OK)
- MacOS: https://www.python.jp/install/macos/install_python.html
  - ターミナルで `python3` コマンドが実行できるところまで

実行環境によって Python を実行するコマンドが `python` だったり `py` だったり `python3` だったりします．  
本稿では `python` コマンドを使いますが，適宜読み替えをお願いします．  


# リポジトリのクローン / ダウンロード

Git が使える方は本リポジトリを任意のディレクトリにクローンしてください．  

```
git clone https://github.com/1izard/python-tutorial.git
```

それ以外の方は Download ZIP をクリックして zip ファイルをダウンロードし任意のディレクトリに解凍してください．  

python-tutorial 内の各 chapter ディレクトリには workspaces ディレクトリという作業用ディレクトリが用意してあります．  
この中にプログラムを書いて実行するようにしましょう．  


# VSCode のインストール

こちら ( https://code.visualstudio.com/ ) から VSCode インストーラをダウンロードしてください．  

続いてダウンロードしたインストーラを実行してインストールします．  
Agreement を読んで OK だったら `I accept the agreement` を選択し，あとは基本デフォルトのままで `Next >` をクリックします．  

ここの設定はすべてチェックを入れるのをおすすめします．  

![vscode_setup.png](img/vscode_setup.png)

- Create a desktop icon
  - デスクトップにアイコンを作成
- Add "Open with Code" action to Windows Exploer file context menu
  - エクスプローラーでファイルを右クリックしたときのメニューに "Open with Code" (VSCode でファイルを開く) を追加
- Add "Open with Code" action to Windows Exploer directory context menu
  - エクスプローラーでディレクトリを右クリックしたときのメニューに "Open with Code" (VSCode でディレクトリを開く) を追加
- Register Code as an editor for supported file types
  - ファイルを開くアプリの候補に VSCode を追加
- Add to PATH (requires shell restart)
  - VSCode でプログラムを実行するのに必要


# 最初のプログラム


## プログラムの作成

VSCode を実行すると Welcom ページが開きます．  
Start の項目の `Open folder...` をクリックして python-tutorial ディレクトリを選択しましょう．  
zip ファイルでダウンロードした方は python-tutorial-master ディレクトリです．  
解凍方法によっては python-tutorial-master ディレクトリが二重になっているので内側のほうを選択します．  

![vscode_open_folder](img/vscode_open_folder.jpg)

各 chapter ディレクトリには作業用 workspaces ディレクトリが作ってあります．  
この中にプログラムを作って実行するようにしましょう．  
まずは `chapter0/workspaces` ディレクトリに `hello.py` を作ってみます．  

左ペインの一番上にあるファイルマークをクリックすると，python-tutorial ディレクトリ以下のファイルの一覧を EXPLORER で見ることができます．  

![vscode_explorer](img/vscode_explorer.jpg)

EXPLORER 上で work ディレクトリを右クリックし，`New File` を選択して新規ファイルを作ります．  
ファイル名は hello.py にします．  

EXPLORER 上で hello.py をクリックすると hello.py を開くことができます．  
中身はこんな感じにしましょう．  

![vscode_hello](img/vscode_hello.jpg)


## Python Extension のインストール

hello.py を作るかクリックすると上の画像のように右下あたりに `Do you want to install the recommended extensions for Python?` (Python Extension をインストールしますか？) というモーダルが出てきます．  
Extension とは VSCode の拡張機能のことです．  
Google 拡張機能みたいにどんどん VSCode に機能を追加していくことができます．  
Python Extension は Python をコーディングするときに関数名などを補完してくれる便利な拡張機能です．  
`Install` をクリックしてインストールしましょう．  

拡張機能は左ペインの EXTENSIONS を開いてインストールすることができます．  
モーダルを消してしまった方はここからインストールしましょう．  

![vscode_extensions](img/vscode_extensions.jpg)


## プログラムの実行

プログラムの実行結果を標準出力 (standard output; コンソールに出力すること) するには，組込み関数 print を使います．  

プログラムの実行にはコンソール (Terminal) を使います．  

EXPLORER 上で workspaces ディレクトリを右クリックし，`Open in Integrated Terminal` を選択するとエディタ下部でコンソールが開きます．  

![vscode_open_terminal](img/vscode_open_terminal.jpg)


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



