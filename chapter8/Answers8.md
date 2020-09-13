# Chapter 8 練習問題解答例


## Q 1

Path オブジェクトの glob メソッドか glob モジュールの glob メソッドを使います．  

次のコードは Path オブジェクトを使う実装例です．  
指定のディレクトリ以下のすべてのファイルパスを取得するには，glob メソッドに再帰的を意味する `**` と任意の文字列を表す `*` のワイルドカードを使います．  

```python
from pathlib import Path
from pprint import pprint


src = Path(__file__).parent.resolve()  # 相対パスを絶対パスにする
txts = []
# glob メソッドは拡張子 .txt のすべてのファイルの Path オブジェクトを生成する generator オブジェクトを返す
for p in src.glob("**/*.txt"):
    txts.append(str(p))  # str(<Path オブジェクト>) でファイルパスの文字列を取得
# (Extra) txts = [str(p) for p in path.glob("**/*.txt")]
pprint(txts)
"""
['/workspaces/dir2/dir2_1/file2_1_1.txt',
 '/workspaces/dir2/dir2_1/dir2_1_1/file2_1_1_01.txt',
 '/workspaces/dir2/dir2_1/dir2_1_1/file2_1_1_02.txt',
 '/workspaces/dir2/dir2_1/dir2_1_1/file2_1_1_03.txt',
 '/workspaces/dir2/dir2_1/dir2_1_2/file2_1_2_02.txt']
"""
```

次のコードは glob.glob メソッドを使う実装例です．  

```python
from pprint import pprint
import os
import glob


src = os.path.abspath(os.path.dirname(__file__))
txts = glob.glob(os.path.join(src, "**", "*.txt"), recursive=True)
pprint(txts)
"""
['/workspaces/dir2/dir2_1/file2_1_1.txt',
 '/workspaces/dir2/dir2_1/dir2_1_1/file2_1_1_01.txt',
 '/workspaces/dir2/dir2_1/dir2_1_1/file2_1_1_02.txt',
 '/workspaces/dir2/dir2_1/dir2_1_1/file2_1_1_03.txt',
 '/workspaces/dir2/dir2_1/dir2_1_2/file2_1_2_02.txt']
"""
```


## Q 2

Path オブジェクトを使った場合は次のようになります．  

```python
from pathlib import Path
from pprint import pprint


packages = {}
src = Path(__file__).parent / "../dir2_2/requirements.txt"
with open(src, "r") as f:
    for line in f:
        name, version = line.strip().split("==")
        packages[name] = version

pprint(packages)
"""
{'autopep8': '1.5.4',
 'flake8': '3.8.3',
 'mccabe': '0.6.1',
 'pycodestyle': '2.6.0',
 'pyflakes': '2.2.0',
 'toml': '0.10.1'}
"""
```

os.path モジュールを使った場合は次のようになります．  

```python
import os
from pprint import pprint


packages = {}
src = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dir2_2", "requirements.txt")
with open(src, "r") as f:
    for line in f:
        name, version = line.strip().split("==")
        packages[name] = version

pprint(packages)
"""
{'autopep8': '1.5.4',
 'flake8': '3.8.3',
 'mccabe': '0.6.1',
 'pycodestyle': '2.6.0',
 'pyflakes': '2.2.0',
 'toml': '0.10.1'}
"""
```


## Q 3

次のコードは Path オブジェクトを使う例です．  
file2_2_1.json から読み出したオブジェクト `prices` は list であることに注意しましょう．  
それを dict `price_dct` に直して商品名から価格を取得しやすくします．  

```python
from pathlib import Path
import json


json_path = Path(__file__).parent / "../dir2_2/file2_2_1.json"
txt_path = Path(__file__).parent / "../dir2_2/file2_2_2.txt"

with open(json_path, "r") as f:
    prices = json.load(f)

with open(txt_path, "r") as f:
    items = f.readlines()

price_dct = {}
for p in prices:
    price_dct[p["item_name"]] = p["unit_price"]
# (Extra) price_dct = {p["item_name"]: p["unit_price"] for p in prices}

total_price = 0
for item in items:
    total_price += price_dct.get(item.strip(), 0)   # get() をつかったほうが安全

print(total_price)
```

os.path モジュールを使った場合のコードは次のようになります．  

```python
import os
import json


dir2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(dir2_path, "dir2_2", "file2_2_1.json")
txt_path = os.path.join(dir2_path, "dir2_2", "file2_2_2.txt")

with open(json_path, "r") as f:
    prices = json.load(f)

with open(txt_path, "r") as f:
    items = f.readlines()

price_dct = {}
for p in prices:
    price_dct[p["item_name"]] = p["unit_price"]
# (Extra) price_dct = {p["item_name"]: p["unit_price"] for p in prices}

total_price = 0
for item in items:
    total_price += price_dct.get(item.strip(), 0)

print(total_price)
```


## Q 4

Path オブジェクトを使用した場合のコードは次のとおりです．  
Path オブジェクトの iterdir メソッドを使って dir1_2_1 直下のファイルの Path オブジェクトをすべて取得し，それぞれの Path オブジェクトからファイルの内容を読み出して images に格納します．  
その後 sort メソッドでファイル名順にソートします．  

```python
from pathlib import Path
from pprint import pprint


images = []
src_dir = Path(__file__).parent / "../dir2_2/dir2_2_1"
for p in src_dir.iterdir():
    with open(p, "r") as f:
        for line in f:
            images.append(line.strip())

images.sort()
pprint(images)
```

dir2_2_1 直下に `.txt` 以外のファイルがある可能性を考慮して万全を期すには glob メソッドを使って `.txt` のファイルの Path オブジェクトのみを取得すると良いです．  

```python
from pathlib import Path
from pprint import pprint


images = []
src_dir = Path("../dir1_2/dir1_2_1")
for p in src_dir.glob("*.txt"):
    with open(p, "r") as f:
        for line in f:
            images.append(line.strip())

images.sort()
pprint(images)
```

os.path モジュールを使うコードは次のようになります．  

```python
from pprint import pprint
import os
import glob


images = []
dir2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pattern = os.path.join(dir2_path, "dir2_2", "dir2_2_1", "*.txt")
for p in glob.glob(pattern):
    with open(p, "r") as f:
        for line in f:
            images.append(line.strip())

images.sort()
pprint(images)
```


## Q 5

```python
packages = {
    "autopep8": "1.5.4",
    "flake8": "3.8.3",
    "mccabe": "0.6.1",
    "pycodestyle": "2.6.0",
    "pyflakes": "2.2.0",
    "toml": "0.10.1",
}

with open("requirements.txt", "w") as f:
    for k, v in packages.items():
        f.write(f"{k}=={v}\n")
    # (Extra) f.writelines([f"{k}=={v}\n" for k, v in packages.items()])
```


## Q 6

Path オブジェクトを使う実装例は次のとおりです．  

```python
from pathlib import Path
import json


class Weather:
    def __init__(self, date, weather, max_temp, min_temp):
        self.date = date
        self.weather = weather
        self.max_temp = max_temp
        self.min_temp = min_temp


weathers = [
    Weather("2020-08-02", "sunny", 31.5, 22.6),
    Weather("2020-08-03", "sunny", 32.3, 22.3),
    Weather("2020-08-04", "sunny", 33.1, 24.5),
    Weather("2020-08-05", "sunny", 34.2, 25.7),
    Weather("2020-08-06", "sunny", 33.1, 25.5),
    Weather("2020-08-07", "cloudy", 35.4, 26),
    Weather("2020-08-08", "cloudy", 32.3, 26),
]

dcts = []
for weather in weathers:
    dcts.append(weather.__dict__)


dst = Path(__file__).parent / "../file2_3.json"
with open(dst, "w") as f:
    json.dump(dcts, f)
```

os.path モジュールを使った実装例は次のとおりです．  

```python
import os
import json


class Weather:
    def __init__(self, date, weather, max_temp, min_temp):
        self.date = date
        self.weather = weather
        self.max_temp = max_temp
        self.min_temp = min_temp


weathers = [
    Weather("2020-08-02", "sunny", 31.5, 22.6),
    Weather("2020-08-03", "sunny", 32.3, 22.3),
    Weather("2020-08-04", "sunny", 33.1, 24.5),
    Weather("2020-08-05", "sunny", 34.2, 25.7),
    Weather("2020-08-06", "sunny", 33.1, 25.5),
    Weather("2020-08-07", "cloudy", 35.4, 26),
    Weather("2020-08-08", "cloudy", 32.3, 26),
]

dcts = []
for weather in weathers:
    dcts.append(weather.__dict__)


dst = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "file1_3.json")
with open(dst, "w") as f:
    json.dump(dcts, f)
```


## Q 7

Paht オブジェクトを使った場合は次のようになります．  

```python
from pathlib import Path
import shutil


top = Path(__file__).parent / "../dir2_3"
src = top / "dir2_3_1"
dst = top / "dir2_3_2"

shutil.copytree(str(src), str(dst))
```

os.path モジュールを使ったコードは次のようになります．  

```python
import os
import shutil


top = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dir2_3")
src = os.path.join(top, "dir2_3_1")
dst = os.path.join(top, "dir2_3_2")

shutil.copytree(src, dst)
```


## Q 8

Path モジュールを使ったコードは次のようになります．  

```python
from pathlib import Path

src = Path(__file__).parent / "../dir2_4"
for i, p in enumerate(src.iterdir(), 1):
    p.rename(p.with_name(f"data{i:02d}.png"))
    # あるいは p.rename(p / f"data{i:02d}.png")
```

os.path モジュールを使う場合は glob.glob メソッドを使うのが簡単です．  

```python
import os
import glob


top = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dir2_4")
for i, p in enumerate(glob.glob(os.path.join(top, "*")), 1):
    os.rename(p, os.path.join(top, f"data{i:02d}.png"))
```


## Q 9

Path オブジェクトを使用すると次のように書けます．  

```python
from pathlib import Path
import shutil


top = Path(__file__).parent / "../dir2_5"
dst = Path(__file__).parent / "../dir2_5/work"

with open(dst / "wanted.txt", "r") as f:
    for line in f:
        src = top / line.strip()
        shutil.copy2(str(src), str(dst))
```

os.path モジュールの場合は次のようになります．  

```python
import os
import shutil


top = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dir2_5")
dst = os.path.join(top, "work")

with open(os.path.join(dst, "wanted.txt"), "r") as f:
    for line in f:
        src = os.path.join(top, line.strip())
        shutil.copy2(src, dst)
```


## Q 10

Path オブジェクトを使うと次のようになります．  


```python
from pathlib import Path
import json
import shutil


top = Path(__file__).parent / "../dir2_6"
src_dir = top / "work"
with open(src_dir / "dist.json", "r") as f:
    dist = json.load(f)
    for k, v in dist.items():
        src = src_dir / k
        dst = top / v
        shutil.copy2(str(src), str(dst))
```

os.path モジュールを使うと次のようになります．  

```python
import os
import json
import shutil


top = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dir2_6")
src_dir = os.path.join(top, "work")
with open(os.path.join(src_dir, "dist.json"), "r") as f:
    dist = json.load(f)
    for k, v in dist.items():
        src = os.path.join(src_dir, k)
        dst = os.path.join(top, v)
        shutil.copy2(src, dst)
```

