# Chapter 8 ファイルI/O，モジュール，システム

この章ではファイル I/O や，プログラムの実行に関する変数や関数，Python プログラムのディレクトリ構造について説明します．  

# os

os モジュールはオペレーティングシステム (OS) に関する変数や関数の集まりです．  
主に環境変数やファイルパスを扱うときに使います．  

環境変数 (environment variable) とは OS 上で動作するプログラム (プロセス) が共有で使用する設定のことです．  
プログラムを実行可能にするためプログラムのパスを設定したりします．  

## ファイルパス

ファイルパス (file path) はファイルが存在する場所を表す文字列です．  
ファイルパスには絶対パスと相対パスの 2 種類があります．  
絶対パスはディレクトリの階層のうち最上層を基準としたファイルの場所のことで，相対パスはカレントディレクトリ (current directory : 今いるディレクトリ) を基準としたファイルの場所のことをいいます．  

以降，例として以下のディレクトリ構造を想定します．  

```
workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.json
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── file1_1.html
    └── file1_2.xlsx
```

カレントディレクトリを dir1_1 とすると，file1_1_1.txt，file1_1.html，file1_2_1.md の絶対パスと相対パスは次のようになります．  
パスは Linux や MacOS では `/` (スラッシュ)，Windows では `\` (バックスラッシュ) か `¥` (円マーク) で区切ります．  
本稿の説明では `/` で区切ることにしますが，Python のプログラムでファイルパスを扱う場合は Python のメソッドが自動的に解決してくれます．  
`.` (ピリオド x 1) はカレントディレクトリを表し，`..` (ピリオド x 2) は親ディレクトリ (parent directory) を表します．  

|ファイル|絶対パス|相対パス|
|:---:|:---:|:---:|
|file1_1_1.txt|`/workspaces/dir1/dir1_1/file1_1_1.txt`|`./file1_1_1.txt` or `file1_1_1.txt`|
|file1_1.html|`/workspaces/dir1/file1_1.html`|`../file1_1.html`|
|file1_2_1.md|`/workspaces/dir1/dir1_2/file1_2_1.md`|`../dir1_2/file1_2_1.md`|

### `os.path.join()`

ファイルパスの区切り文字を自動的に解決してパスを連結するメソッドです．  
連結したパスを str オブジェクトで返します．  
ファイルパスを書くときは `os.path.join()` か後述する `pathlib.Path` を使うようにしましょう．  

file1.html と file2_1.md のパスを `os.path.join()` メソッドで作ると Linux や MacOS では次のようになります．  
コードはファイル example.py として実行するものとします．  

```python
import os


file1_1_rel_path = os.path.join("..", "file1_1.html")
print(file1_1_rel_path)   # ../file1_1.html

file1_2_1_rel_path = os.path.join("..", "dir1_2", "file1_2_1.md")
print(file1_2_1_rel_path)  # ../dir1_2/file1_2_1.md
```

Windows ではこんな感じです．  

```python
import os


file1_1_rel_path = os.path.join("..", "file1_1.html")
print(file1_1_rel_path)   # ..\file1_1.html

file1_2_1_rel_path = os.path.join("..", "dir1_2", "file1_2_1.md")
print(file1_2_1_rel_path)  # ..\dir1_2\file1_2_1.md
```

### `os.path.abspath()`

相対パスから絶対パスを取得するには `os.path.abspath()` メソッドを使います．  

```python
import os


file1_1_rel_path = os.path.join("..", "file1_1.html")
print(file1_1_rel_path)     # ../file1_1.html

file1_2_1_rel_path = os.path.join("..", "dir1_2", "file1_2_1.md")
print(file1_2_1_rel_path)     # ../dir1_2/file1_2_1.md

print(os.path.abspath(file1_1_rel_path))      # /workspaces/dir1/file1_1.html
print(os.path.abspath(file1_2_1_rel_path))    # /workspaces/dir1/dir1_2/file1_2_1.md
```

### `os.path.dirname()`

ファイルパスの末尾のディレクトリ名 (最後の区切り文字の手前) を返すメソッドです．  
ファイルパスから，そのファイルのあるディレクトリ名を取得するときに使います．  


### `os.path.basename()`

ファイルパスの末尾 (最後の区切り文字以降) を返すメソッドです．  
ファイルパスからディレクトリ名やファイル名だけを取り出すときに使います．  
`<ファイルパス> == os.path.join(os.path.dirname(<ファイルパス>), os.path.basename(<ファイルパス>))` になります．  


```python
import os


file1_1_abs_path = os.path.abspath(os.path.join("..", "file1_1.html"))
print(file1_1_abs_path)                       # /workspaces/dir1/file1_1.html
print(os.path.dirname(file1_1_abs_path))      # /workspaces/dir1
print(os.path.basename(file1_1_abs_path))     # file1_1.html

file1_2_1_abs_path = os.path.abspath(os.path.join("..", "dir1_2", "file1_2_1.md"))
print(file1_2_1_abs_path)                     # /workspaces/dir1/dir1_2/file1_2_1.md
print(os.path.dirname(file1_2_1_abs_path))    # /workspaces/dir1/dir1_2
print(os.path.basename(file1_2_1_abs_path))   # file1_2_1.md

dir1_1_abs_path = os.path.abspath(os.path.join("."))
print(dir1_1_abs_path)                      # /workspaces/dir1/dir1_1
print(os.path.dirname(dir1_1_abs_path))     # /workspaces/dir1
print(os.path.basename(dir1_1_abs_path))    # dir1_1
```

### `os.path.splitext()`

ファイルパスを拡張子 (extension) とそれ以外の部分とで分割するメソッドです．  
split + text ではなく split + ext ですね．  

動作としては単純にファイルパスの最後のピリオド以降とそれより前の部分とで分けているだけなので，`.tar.gz` といった拡張子は `.gz` とそれ以外の部分に分割されてしまうことに注意してください．  
この場合は str オブジェクトの `split(".")` で対処します．  

```python
file1_1_abs_path = os.path.abspath(os.path.join("..", "file1_1.html"))
print(file1_1_abs_path)   # /workspaces/dir1/file1_1.html
print(os.path.splitext(file1_1_abs_path))  # ('/workspaces/dir1/file1_1', '.html')


file1_2_2_abs_path = os.path.abspath(os.path.join("..", "dir1_2", "file1_2_2.tar.gz"))
print(file1_2_2_abs_path)  # /workspaces/dir1/dir1_2/file1_2_2.tar.gz
print(os.path.splitext(file1_2_2_abs_path))   # ('/workspaces/dir1/dir1_2/file1_2_2.tar', '.gz')

separated = file1_2_2_abs_path.split(".")
root = ".".join(separated[:-2])
ext = "." + ".".join(separated[-2:])
print((root, ext))  # ('/workspaces/dir1/dir1_2/file1_2_2', '.tar.gz')
```


### `os.path.exists()`

ファイルパスが示す場所にファイルあるいはディレクトリがちゃんと存在する場合 `True`，存在しない場合 `False` を返すメソッドです．  

```python
import os


file1_1_abs_path = os.path.abspath(os.path.join("..", "file1_1.html"))
print(file1_1_abs_path)                   # /workspaces/dir1/file1_1.html
print(os.path.exists(file1_1_abs_path))   # True

dir1_1_abs_path = os.path.abspath(os.path.join("."))
print(dir1_1_abs_path)                  # /workspaces/dir1/dir1_1
print(os.path.exists(dir1_1_abs_path))  # True

imaginary_file_abs_path = os.path.abspath(os.path.join("..", "imaginary_file.cpp"))
print(imaginary_file_abs_path)                  # /workspaces/dir1/imaginary_file.cpp
print(os.path.exists(imaginary_file_abs_path))  # False
```

### `os.path.isfile()`

ファイルパスが示す場所にファイルが存在する場合 `True`，存在しない場合 `False` を返します．  
ディレクトリの場合も `False` となります．  

### `os.path.isdir()`

ファイルパスが示す場所にディレクトリが存在する場合 `True`，存在しない場合 `False` を返します．  
ファイルの場合も `False` となります．  

```python
import os


file1_1_abs_path = os.path.abspath(os.path.join("..", "file1_1.html"))
print(file1_1_abs_path)                   # /workspaces/dir1/file1_1.html
print(os.path.isfile(file1_1_abs_path))   # True
print(os.path.isdir(file1_1_abs_path))    # False

dir1_1_abs_path = os.path.abspath(os.path.join("."))
print(dir1_1_abs_path)                  # /workspaces/dir1/dir1_1
print(os.path.isfile(dir1_1_abs_path))  # False
print(os.path.isdir(dir1_1_abs_path))   # True

imaginary_file_abs_path = os.path.abspath(os.path.join("..", "imaginary_file.cpp"))
print(imaginary_file_abs_path)                  # /workspaces/dir1/imaginary_file.cpp
print(os.path.isfile(imaginary_file_abs_path))  # False
print(os.path.isdir(imaginary_file_abs_path))   # False
```

### `os.makedirs()`

引数で与えたファイルパスに新しくディレクトリを作るメソッドです．  

```
// 実行前

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.json
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── file1_1.html
    └── file1_2.xlsx
```

```python
import os


dir1_3_path = os.path.join("..", "dir1_3")
os.mkdir(dir1_3_path)
```

```
// 実行後

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.json
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_3  <- New !!
    ├── file1_1.html
    └── file1_2.xlsx
```

多層ディレクトリを一度に作ることもできます．  
今度は dir1 以下に新しく `dir1_4/dir1_4_1` を作ってみます．  

```
// 実行前

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.json
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_3  <- New !!
    ├── file1_1.html
    └── file1_2.xlsx
```

```python
import os

dir1_4_1_path = os.path.join("..", "dir1_4", "dir1_4_1")
os.makedirs(dir1_4_1_path)
```

```
// 実行後

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.json
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_3
    ├── dir1_4  <- New !!
    │   └── dir1_4_1  <- New !!
    ├── file1_1.html
    └── file1_2.xlsx
```

すでにファイルやディレクトリが存在するファイルパスを指定した場合は `FileExistsError` が送出されます．  
引数 `exist_ok` を `True` にすると，ファイルやディレクトリがすでに存在した場合何もしないという動作になりエラーも送出されなくなります．  

```python
import os

dir1_4_1_path = os.path.join("..", "dir1_4", "dir1_4_1")
os.makedirs(dir1_4_1_path, exist_ok=True)
```


### `os.remove()`

指定したファイルパスのファイルを削除するメソッドです．  
ディレクトリの場合は `IsADirectoryError` が送出され，ファイルが存在しない場合は `FileNotFoundError` が送出されます．  
使用前に `os.path.isfile()` でファイルが存在するかどうかを確認するのが良いです．  

次の例では，`dir1/dir1_1/file1_2.json` を削除しています．  

```
// 実行前

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.json
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_3
    ├── dir1_4
    │   └── dir1_4_1
    ├── file1_1.html
    └── file1_2.xlsx
```

```python
import os


file1_1_2_path = "file1_1_2.json"
if os.path.isfile(file1_1_2_path):
    os.remove(file1_1_2_path)
```

```
// 実行後

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   └── file1_1_1.txt
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_3
    ├── dir1_4
    │   └── dir1_4_1
    ├── file1_1.html
    └── file1_2.xlsx
```


### `os.rmdir()`

ディレクトリを削除するときに使用するメソッドです．  
引数にはディレクトリのパスを渡します．  
ファイルパスに何も存在しなかった場合は `FileNotFoundError` が，ディレクトリではなくファイルが存在した場合は `NotADirectoryError` が送出されます．  
使用前に `os.path.isdir()` でディレクトリの存在を確認するのをおすすめします．  

また，ディレクトリが空でない場合は `OSError` が送出されます．  
つまり，空のディレクトリしか削除できません．  

次のコードでは `dir1/dir1_3` を削除しています．  

```
// 実行前

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   └── file1_1_1.txt
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_3
    ├── dir1_4
    │   └── dir1_4_1
    ├── file1_1.html
    └── file1_2.xlsx
```

```python
import os

dir1_3_path = os.path.join("..", "dir1_3")
if os.path.isdir(dir1_3_path):
    os.rmdir(dir1_3_path)
```

```
// 実行後

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   └── file1_1_1.txt
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_4
    │   └── dir1_4_1
    ├── file1_1.html
    └── file1_2.xlsx
```

### `os.removedirs()`

多層ディレクトリを最深のディレクトリから順に削除するメソッドです．  
ファイルパスに何も存在しなかった場合は `FileNotFoundError` が，ディレクトリではなくファイルが存在した場合は `NotADirectoryError` が送出されます．  
最深から順に削除していきますが，途中で空でないディレクトリにあたった場合は `OSError` が送出されてそこで削除をやめます．  

次の例では，`dir1/dir1_4` と `dir1/dir1_4/dir1_4_1` を削除しています．  

```
// 実行前

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   └── file1_1_1.txt
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── dir1_4
    │   └── dir1_4_1
    ├── file1_1.html
    └── file1_2.xlsx
```

```python
import os

dir1_4_1_path = os.path.join("..", "dir1_4", "dir1_4_1")
if os.path.isdir(dir1_4_1_path):
    os.removedirs(dir1_4_1_path)
```

```
// 実行後

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   └── file1_1_1.txt
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── file1_1.html
    └── file1_2.xlsx
```

### `os.rename()`

ファイルやディレクトリのパスを変更するメソッドです．  
`os.rename(src, dst)` のように使用します (src; source: ソース，dst; destination: 目的地)．  

Windows だと dst にすでにファイルが存在している場合は `FileExistsError` が送出されますが，Linux や MacOS だと上書きされます．  

次の例では，`dir1/file1.html` を `dir1/dir1_1/file1_2.html` に変更しています．  

```
// 実行前

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   └── file1_1_1.txt
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── file1_1.html
    └── file1_2.xlsx
```

```python
import os


src = os.path.join("..", "file1.html")
dst = "file1_2.html"
os.rename(src, dst)
```

```
// 実行後 

workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.html
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    └── file1_2.xlsx
```


(Extra)  

## 環境変数


環境変数を Python のプログラムの中で参照するには os モジュールの environ オブジェクトを使います．  
dict に似たオブジェクトで，環境変数名を key，設定値を value に見立てて扱うことができます．  

次のコードでは `os.environ` ですべての環境変数を取得しています．  
実行環境は Docker コンテナ内です．  

```python
import os

print(os.environ)

"""
environ({
    'SHELL': '/bin/bash',
    'COLORTERM': 'truecolor', 
    'TERM_PROGRAM_VERSION': '1.49.0-insider', 
    'HOSTNAME': 'a0a39f87b797', 
    'PYTHON_VERSION': '3.8.5', 
...
})
"""
```

Windows だとこんな感じです．  

```python
import os

print(os.environ)

"""
environ({
    'ALLUSERSPROFILE': 'C:\\ProgramData', 
    'APPDATA': 'C:\\Users\\dee1b\\AppData\\Roaming', 
    'ASL.LOG': 'Destination=file', 
    'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
    'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
    ...
})
"""
```

特定の環境変数にアクセスする場合は `os.environ[<環境変数名>]` のようにします．  
下のコードでは環境変数 `PATH` の設定値を取得しています．  
PATH はプログラムを実行するためプログラムがある場所を保持する環境変数です．  

```python
import os


path = os.environ["PATH"]
print(path)
# /root/.vscode-server-insiders/bin/e4256dd1a02339bb1d56647ecd9134bf38bc7c03/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/py-utils/bin:/root/.local/bin
```

環境変数を設定する場合，例えば `PATH` の末尾に新しく `/workspace/.poetry/bin` というプログラムのパスを追加する場合は次のようにします．  
`os.pathsep` は `PATH` 内のパスの区切り文字です．  
Linux や MacOS では `:`，Windows では `;` になるので `os.pathsep` を使って自動的に解決してもらうようにします．  

```python
import os
from pathlib import Path


print(os.environ["PATH"])
# /root/.vscode-server-insiders/bin/e4256dd1a02339bb1d56647ecd9134bf38bc7c03/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/py-utils/bin:/root/.local/bin

path = Path("/workspace/.poetry/bin")
os.environ["PATH"] += os.pathsep + str(path)
print(os.environ["PATH"])
# /root/.vscode-server-insiders/bin/e4256dd1a02339bb1d56647ecd9134bf38bc7c03/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/py-utils/bin:/root/.local/bin:/workspace/.poetry/bin
```

(ここまで Extra)  

# glob.glob()

glob モジュールの glob メソッドは，引数に与えられたファイルパスのパターンに合致するファイルを走査して list にしてそのファイルパスを返すメソッドです．  
ファイルパスのパターンにはワイルドカードが使えます．  
`*` には 1 文字以上の任意の文字列，`?` には任意の 1 文字が当てはまります．  
また，`[a-z]` はアルファベットの小文字 1 文字，`[A-Z]` はアルファベットの大文字 1 文字，`[0-9]` は数字 1 文字を表します．  
`*` は正規表現の機能と若干異なることに注意しましょう．  

例えば，次のようなディレクトリ構造とファイルがあったとします．  
プログラムは example.py で実行します．  

```
workspace
├── dir1
│   ├── dir1_1
│   │   ├── file1_1_1.txt
│   │   ├── file1_1_2.json
│   │   └── file1_1_3.txt
│   ├── dir1_2
│   │   ├── file1_2_1.md
│   │   ├── file1_2_2.tar.gz
│   │   └── file1_2_3.txt
│   ├── file1_1.html
│   ├── file1_2.xlsx
│   ├── file1_3.txt
│   └── file1_4.txt
└── example.py
```

dir1 直下にある，拡張子が `.txt` のファイルのパスをすべて取得するには，パターンが `dir1/*.txt` になるように引数を指定して glob.glob メソッドを使います．  

```python
import glob
import os


files = glob.glob(os.path.join("dir1", "*.txt"))
print(files)
# ['dir1/file1_3.txt', 'dir1/file1_4.txt']
```

dir1_1 直下と dir1_2 直下の `.txt` ファイルのパスをすべて取得したい場合は，パターンを `dir1/*/*.txt` として dir1 直下のすべてのディレクトリが当てはまるようにします．  

```python
import glob
import os


files = glob.glob(os.path.join("dir1", "*", "*.txt"))
print(files)
# ['dir1/dir1_1/file1_1_1.txt', 'dir1/dir1_1/file1_1_3.txt', 'dir1/dir1_2/file1_2_3.txt']
```

dir1 以下のすべての `.txt` ファイルのパスを取得する場合は，`recursive=True` としてワイルドカード `**` を使います．  

```python
import glob
import os


files = glob.glob(os.path.join("dir1", "**", "*.txt"), recursive=True)
print(files)
# ['dir1/file1_3.txt', 'dir1/file1_4.txt', 'dir1/dir1_1/file1_1_1.txt', 'dir1/dir1_1/file1_1_3.txt', 'dir1/dir1_2/file1_2_3.txt']
```


# Path

pathlib モジュールは Python 3.4 で新しく追加されたファイルパスを操作するためのプログラム群です．  
os.path モジュールではファイルパスを文字列で扱っていましたが，pathlib モジュールではファイルパスを pathlib.Path クラスのオブジェクトとして扱います．  
公式で os.path モジュールよりファイルパスを操作しやすいとしてすすめられているので，今後はこちらが主流になると思われます．  
ただ，多くのプログラムはまだ `os.path`モジュールを使っているので．既存のコードに触れたり複数人での開発を行う方は `os.path` モジュールの使い方も覚えておいたほうが良いです．  

`os.path` モジュールと同様に次のディレクトリ構造を用いて説明していきます．  

```
workspaces
└── dir1
    ├── dir1_1
    │   ├── example.py
    │   ├── file1_1_1.txt
    │   └── file1_1_2.json
    ├── dir1_2
    │   ├── file1_2_1.md
    │   └── file1_2_2.tar.gz
    ├── file1_1.html
    └── file1_2.xlsx
```

## インスタンス化 (instantiate)

Path オブジェクトはファイルパスの文字列で初期化します．  
ファイルパスの区切り文字は `/` を使うと OS ごとに自動的に解決したファイルパスにしてくれます．  

Linux や Mac の場合は自動的に Path クラスを継承した PosixPath クラスのオブジェクトが作られます．    

```python
from pathlib import Path


file1_1_rel_path = Path("../file1_1.html")
print(file1_1_rel_path)         # ../file1_1.html
print(type(file1_1_rel_path))   # <class 'pathlib.PosixPath'>

file1_2_1_rel_path = Path("../dir1_2/file1_2_1.md")
print(file1_2_1_rel_path)       # ../dir1_2/file1_2_1.md
```

Windows の場合は自動的に Path クラスを継承した WindowsPath クラスのオブジェクトが作られます．  
ファイルパスの区切り文字がちゃんと `\` になってます．  

```python
from pathlib import Path


file1_1_rel_path = Path("../file1_1.html")
print(file1_1_rel_path)         # ..\file1_1.html
print(type(file1_1_rel_path))   # <class 'pathlib.WindowsPath'>

file1_2_1_rel_path = Path("../dir1_2/file1_2_1.md")
print(file1_2_1_rel_path)       # ..\dir1_2\file1_2_1.md
```

Path クラスのクラス図はこんな感じです (公式 doc https://docs.python.org/3/library/pathlib.html )．  

![path](path.png)



## `/` 演算子

Path オブジェクトは `/` 演算子で連結することができます．  
オペランドは Path オブジェクトと str オブジェクトのどちらでも OK です．  
`os.path.join()` の機能にあたります．  

```python
dir1_path = Path("..")

file1_1_rel_path = dir1_path / "file1_1.html"
print(file1_1_rel_path)     # ../file1_1.html

file1_2_1_rel_path = dir1_path / Path("dir1_2") / Path("file1_2_1.md")
print(file1_2_1_rel_path)   # ../dir1_2/file1_2_1.md
```

## `PurePath.parts`

`parts` はファイルパスの区切り文字で分割したすべての要素をタプルとして保持しています．  

```python
from pathlib import Path


file1_1_rel_path = Path("../file1_1.html")
print(file1_1_rel_path.parts)   # ('..', 'file1_1.html')

file1_2_1_rel_path = Path("../dir1_2/file1_2_1.md")
print(file1_2_1_rel_path.parts) # ('..', 'dir1_2', 'file1_2_1.md')
```


## `PurePath.parents`

`parents` はファイルパスから最上層までのすべてのディレクトリを保持しています．  

```python
from pathlib import Path


file1_1_abs_path = Path("/workspace/dir1/file1_1.html")
file1_1_parents = file1_1_abs_path.parents
print(repr(file1_1_parents))    # <PosixPath.parents>
print(len(file1_1_parents))     # 3
print(file1_1_parents[0])       # /workspace/dir1
print(file1_1_parents[1])       # /workspace
print(file1_1_parents[2])       # /

file1_2_1_abs_path = Path("/workspace/dir1/dir1_2/file1_2_1.md")
file1_2_1_parents = file1_2_1_abs_path.parents
print(file1_2_1_parents)        # <PosixPath.parents>
print(len(file1_2_1_parents))   # 4
print(file1_2_1_parents[0])     # /workspace/dir1/dir1_2
print(file1_2_1_parents[1])     # /workspace/dir1
print(file1_2_1_parents[2])     # /workspace
print(file1_2_1_parents[3])     # /
```


## `PurePath.parent`

`parent` はファイルパスの指すファイルあるいはディレクトリのあるディレクトリのパスを保持しています．  
`os.path.dirname()` の機能にあたります．  

## `PurePath.name`

`name` はファイルパスの最後の区切り文字以降，つまりディレクトリ名あるいはファイル名を保持しています．  
`os.path.basename()` と同様の機能です．  

```python
from pathlib import Path


file1_1_abs_path = Path("/workspace/dir1/file1_1.html")
print(file1_1_abs_path.parent)  # /workspace/dir1
print(file1_1_abs_path.name)    # file1_1.html

file1_2_1_abs_path = Path("/workspace/dir1/dir1_2/file1_2_1.md")
print(file1_2_1_abs_path.parent)    # /workspace/dir1/dir1_2
print(file1_2_1_abs_path.name)      # file1_2_1.md
```

## `PurePath.suffix`

`suffix` はファイルパスが指すファイルの拡張子を保持しています．  
`os.path.splitext()` と似たような機能になります．  
`XXX.tar.gz` のように拡張子が複数のピリオドを含む場合は `path.suffixes` を使うようにします．  

```python
from pathlib import Path


file1_1_abs_path = Path("/workspace/dir1/file1_1.html")
print(file1_1_abs_path.suffix)      # .html

file1_2_2_abs_path = Path("/workspace/dir1/dir1_2/file1_2_2.tar.gz")
print(file1_2_2_abs_path.suffix)    # .gz
```

## `PurePath.suffixes`

`suffixes` はファイル名の最初のピリオド以降を list として返します．  
複数のピリオドが含まれる拡張子をもつファイルパスから拡張子を取り出したいときに便利です．  

```python
from pathlib import Path


file1_1_abs_path = Path("/workspace/dir1/file1_1.html")
print(file1_1_abs_path.suffixes)    # ['.html']

file1_2_2_abs_path = Path("/workspace/dir1/dir1_2/file1_2_2.tar.gz")
print(file1_2_2_abs_path.suffixes)  # ['.tar', '.gz']
```

## `PurePath.stem`

`stem` は拡張子を除いたファイル名を保持しています．  
最後のピリオド以降を除去するみたいで，複数のピリオドが含まれる拡張子をもつファイル名の場合は上手くいかないですね...  
その場合は `str.split(".")` で対処します．  

```python
file1_1_abs_path = Path("/workspace/dir1/file1_1.html")
print(file1_1_abs_path.stem)    # file1_1

file1_2_2_abs_path = Path("/workspace/dir1/dir1_2/file1_2_2.tar.gz")
print(file1_2_2_abs_path.stem)                      # file1_2_2.tar
print(str(file1_2_2_abs_path.stem).split(".")[0])   # file1_2_2
```

## `path.`


# ファイル I/O


# モジュール



# sys

インタプリタ (Python プログラムを実行しているアプリケーション) に関係するパラメータや関数がそろっているモジュールです．  

# datetime

# time