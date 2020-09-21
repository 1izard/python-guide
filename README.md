# python-tutorial

練習問題付き Python 入門  


# 推奨環境

- Python 3.6 以上  
- OS はたぶんなんでも OK  
- エディタは VSCode 推奨  

本稿のコードの多くのは Python 3.8.5 を Docker コンテナ上で実行して動作確認していますが，プラットフォームごとに差異がありそうなところは Windows，MacOS 上でも一応動作確認しています．  


# 対象読者

プログラミング初心者，Python 初学者 / 初級者  


# 本稿のゴール

Python の基本文法を学習しながら，最終的にコンソール上で動く学習用ツールを実装できるようにします．  
そのため Python の実行はコマンドラインでの実行を前提とします．  
エディタとして何を使っていいかわからない方の中で，とりあえず Python の文法だけ勉強できればいい方は Google Colab ( https://colab.research.google.com/notebooks/intro.ipynb )，ツールまで実装したい方は VSCode ( https://code.visualstudio.com/ ) をおすすめしますが，本稿での説明は VSCode を前提として進めます．  

# Index

## [Chapter 0 準備](chapter00/Chapter0.md)  
- [Python のインストール](chapter00/Chapter0.md#Python-のインストール)
- [リポジトリのクローン / ダウンロード](chapter00/Chapter0.md#リポジトリのクローン--ダウンロード)
- [VSCode のインストール](chapter00/Chapter0.md#VSCode-のインストール)
- [最初のプログラム](chapter00/Chapter0.md#最初のプログラム)
- [Python Extension のインストール](chapter00/Chapter0.md#Python-Extension-のインストール)
- [Linter, Formatter の設定](chapter00/Chapter0.md#linter-formatter-の設定)


## [Chapter 1 基本データ型](chapter01/Chapter1.md)  
- [組込みデータ型 (Built-in Data Type)](chapter01/Chapter1.md#組込みデータ型-built-in-data-type)
- [変数 (Variables) (仮)](chapter01/Chapter1.md#変数-variables-仮)
- [数値](chapter01/Chapter1.md#数値)
- [文字列](chapter01/Chapter1.md#文字列)
- [None](chapter01/Chapter1.md#None)
- [変換](chapter01/Chapter1.md#変換)
- [練習問題 1](chapter01/Chapter1.md#練習問題)
- [練習問題 1 回答例](chapter01/Answers1.md)


## [Chapter 2 文字列](chapter02/Chapter2.md)  
- [定義](chapter02/Chapter2.md#定義)
- [インデックス](chapter02/Chapter2.md#インデックス)
- [文字列長](chapter02/Chapter2.md#文字列長)
- [オフセット](chapter02/Chapter2.md#オフセット)
- [スライス](chapter02/Chapter2.md#スライス)
- [str 型で使用できる主なメソッド](chapter02/Chapter2.md#str-型で使用できる主なメソッド)
- [変数](chapter02/Chapter2.md#変数)
- [練習問題 2](chapter02/Chapter2.md#練習問題)
- [練習問題 2 解答例](chapter02/Answers2.md)


## [Chapter 3 基本構文](chapter03/Chapter3.md)  
- [if 文](chapter03/Chapter3.md#if-文)
- [while 文](chapter03/Chapter3.md#while-文)
- [スコープ](chapter03/Chapter3.md#スコープ)
- [練習問題 3](chapter03/Chapter3.md#練習問題)
- [練習問題 3 解答例](chapter03/Answers3.md)


## [Chapter 4 基本データ構造](chapter04/Chapter4.md)  
- [list](chapter04/Chapter4.md#list)
- [tuple (タプル)](chapter04/Chapter4.md#tuple-タプル)
- [dict (辞書)](chapter04/Chapter4.md#dict-辞書)
- [for 文](chapter04/Chapter4.md#for-文)
- [練習問題 4](chapter04/Chapter4.md#練習問題)
- [練習問題 4 解答例](chapter04/Answers4.md)


## [Chapter 5 関数](chapter05/Chapter5.md)  
- [定義](chapter05/Chapter5.md#定義)
- [実引数 (Argument)](chapter05/Chapter5.md#実引数-argument)
- [仮引数 (Parameter)](chapter05/Chapter5.md#仮引数-parameter)
- [バリデーション (Validation)](chapter05/Chapter5.md#バリデーション-validation)
- [再帰関数](chapter05/Chapter5.md#再帰関数)
- [関数オブジェクト](chapter05/Chapter5.md#関数オブジェクト)
- [ラムダ関数 (Lambda Function)](chapter05/Chapter5.md#ラムダ関数-lambda-function)
- [クロージャ (Closure)](chapter05/Chapter5.md#クロージャ-closure)
- [Generator 関数](chapter05/Chapter5.md#generator-関数)
- [Type Hint](chapter05/Chapter5.md#type-hint)
- [スコープ](chapter05/Chapter5.md#スコープ)
- [練習問題 5](chapter05/Chapter5.md#練習問題)
- [練習問題 5 解答例](chapter05/Answers5.md)


## [Chapter 6 組込み関数](chapter06/Chapter6.md)  
- [abs()](chapter06/Chapter6.md#abs)
- [all()](chapter06/Chapter6.md#all)
- [any()](chapter06/Chapter6.md#any)
- [min()](chapter06/Chapter6.md#min)
- [max()](chapter06/Chapter6.md#max)
- [sum()](chapter06/Chapter6.md#sum)
- [filter()](chapter06/Chapter6.md#filter)
- [map()](chapter06/Chapter6.md#map)
- [sorted()](chapter06/Chapter6.md#sorted)
- [zip()](chapter06/Chapter6.md#zip)
- [type()](chapter06/Chapter6.md#type)
- [isinstance()](chapter06/Chapter6.md#isinstance)
- [練習問題 6](chapter06/Chapter6.md#練習問題)
- [練習問題 6 解答例](chapter06/Answers6.md)


## [Chapter 7 クラス](chapter07/Chapter7.md)  
- [コンストラクタ (Constructor)](chapter07/Chapter7.md#コンストラクタ-constructor)
- [インスタンス属性](chapter07/Chapter7.md#インスタンス属性)
- [インスタンスメソッド](chapter07/Chapter7.md#インスタンスメソッド)
- [アクセシビリティ](chapter07/Chapter7.md#アクセシビリティ)
- [プロパティ (Property)](chapter07/Chapter7.md#プロパティ-property)
- [クラス属性](chapter07/Chapter7.md#クラス属性)
- [クラスメソッド](chapter07/Chapter7.md#クラスメソッド)
- [スタティックメソッド](chapter07/Chapter7.md#スタティックメソッド)
- [継承 (inheritance)](chapter07/Chapter7.md#継承-inheritance)
- [Enum クラス](chapter07/Chapter7.md#enum-クラス)
- [namedtuple](chapter07/Chapter7.md#namedtuple)
- [特殊メソッド (Spacial Method)](chapter07/Chapter7.md#特殊メソッド-special-method)
- [練習問題 7](chapter07/Chapter7.md#練習問題)
- [練習問題 7 解答例](chapter07/Answers7.md)


## [Chapter 8 ファイル操作](chapter08/Chapter8.md)  
- [ファイルパス](chapter08/Chapter8.md#ファイルパス)
- [Path](chatper08/Chapter8.md#path)
- [os](chapter08/Chapter8.md#os)
- [glob.glob()](chapter08/Chapter8.md#glob.glob)
- [shutil](chapter08/Chapter8.md#shutil)
- [ファイル I/O](chapter08/Chapter8.md#ファイル-IO)
- [JSON](chapter08/Chapter8.md#json)
- [練習問題 8](chapter08/Chapter8.md#練習問題)
- [練習問題 8 解答例](chapter08/Answers8.md)


## [Chapter 9 システム/例外処理/モジュール](chapter09/Chapter9.md)  
- [sys](chapter09/Chapter9.md#sys)
- [time](chapter09/Chapter9.md#time)
- [datetime](chapter09/Chapter9.md#datetime)
- [例外処理](chapter09/Chapter9.md#例外処理)
- [モジュール](chapter09/Chapter9.md#モジュール)
- [練習問題 9](chapter09/Chapter9.md#練習問題)
- [練習問題 9 解答例](chapter09/Answers9.md)


## [Chapter 10 コマンドラインツールを作ってみよう](chapter10/Chapter10.md)
- [Rare Candy チュートリアル](chapter10/Chapter10.md#rare-candy-チュートリアル)
- [実装](chapter10/Chapter10.md#実装)


# Topics

基本的な文法のほかに，以下について解説に力を入れています．  

- Python において変数は箱ではなくラベルである
- list の deep copy と shallow copy の違い
- 内包表記の使用例
- クロージャの実用的な使い方
- 組込み関数の実用的な使い方
- プロパティ
- UserList，UserDict の継承
- `__str__` をはじめとする特殊メソッド
- Pathlib，os.path，shutil でのファイル操作
- 実装方法を探りながらツール作り


# 読み方

## サンプルコード

本文中のサンプルコードを分割して説明を挟むようなことはせず，すべてコピペしてすぐ使えるようにしています．  


## ディレクトリ構成

各 chapter のディレクトリに `workspaces` という作業用ディレクトリを用意しています．  
練習用に自動的にディレクトリやファイルを作成するプログラムも用意してあるので，本リポジトリをクローンあるいはダウンロードすることで練習する環境を手軽に作ることができます．  
詳しくは [Chapter 0 準備](chapter0/Chapter0.md) を参照してください．  


## Extra

文中の `(Extra)` とある部分ではちょっと難しい発展的な内容を扱っています．  
プログラミング初心者の方や Python 初学者の方は余裕がなければスキップして OK です．  

