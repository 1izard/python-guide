# python-tutorial

練習問題付き Python 入門  


# 推奨環境

- Python 3.6 以上  
- OS はたぶんなんでも OK  
- エディタは VSCode 推奨  

本稿のコードの多くのは Python 3.8.5 を Docker コンテナ上で実行して動作確認していますが，プラットフォームごとに差異がありそうなところは Windows，MacOS 上でも動作確認しています．  


# 対象読者

プログラミング初心者，Python 初学者 / 初級者  


# 本稿のゴール

Python の基本文法を学習しながら，最終的にコマンドラインツール (Terminal や Powershell などで使うツール) を実装できるようにします．  
そのため Python の実行はコマンドラインでの実行を前提とします．  
エディタとして何を使っていいかわからない方の中で，とりあえず Python の文法だけ勉強できればいい方は Google Colab ( https://colab.research.google.com/notebooks/intro.ipynb )，コマンドラインツールまで実装したい方は VSCode ( https://code.visualstudio.com/ ) をおすすめしますが，本稿での説明は VSCode を前提として進めます．  

# Index

[Chapter 0 準備](chapter0/Chapter0.md)  
[Chapter 1 基本データ型](chapter01/Chapter1.md)  
[Chapter 2 文字列](chapter02/Chapter2.md)  
[Chapter 3 基本構文](chapter03/Chapter3.md)  
[Chapter 4 基本データ構造](chapter04/Chapter4.md)  
[Chapter 5 関数](chapter05/Chapter5.md)  
[Chapter 6 組込み関数](chapter06/Chapter6.md)  
[Chapter 7 クラス](chapter07/Chapter7.md)  
[Chapter 8 ファイル操作](chapter08/Chpater8.md)  
[Chapter 9 システム/例外処理/モジュール](chapter09/Chapter9.md)  
[Chapter 10 コマンドラインツールを作ってみよう](chapter10/Chapter10.md)


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


# 読み方

## サンプルコード

本文中のサンプルコードを分割して説明を挟むようなことはせず，すべてコピペしてすぐ使えるようにしています．  


## ディレクトリ構成

各 chapter のディレクトリに `workspaces` という作業用ディレクトリを用意しています．  
練習用に自動的にディレクトリやファイルを作成するプログラムも用意してあるので，本リポジトリをクローンあるいはダウンロードすることで練習する環境を手軽に作ることができます．  


## Extra

文中の `(Extra)` とある部分ではちょっと難しい発展的な内容を扱っています．  
プログラミング初心者の方や Python 初学者の方は余裕がなければスキップして OK です．  

