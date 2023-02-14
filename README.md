![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/poi-ai/keibaAI)
![Lines of code](https://img.shields.io/tokei/lines/github/poi-ai/keibaAI)
![Elapsed date](https://img.shields.io/date/1673284347?label=first%20commit)
![GitHub latest commit](https://img.shields.io/github/last-commit/poi-ai/keibaAI)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/poi-ai/keibaAI)<br>
[![Twitter](https://github.com/poi-ai/img/blob/main/twitter.png)](https://twitter.com/intent/tweet?text=poi-ai/keibaAI&url=https://github.com/poi-ai/keibaAI)
[![はてなブックマーク](https://github.com/poi-ai/img/blob/main/hatebu.png)](https://b.hatena.ne.jp/entry/s/github.com/poi-ai/keibaAI)
[![Facebook](https://github.com/poi-ai/img/blob/main/facebook.png)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/poi-ai/keibaAI)

|項目|
| :--- |
| 1. [概要](#anchor1) |
| 2. [開発環境](#anchor2)|
| 3. [初期設定](#anchor3)|
| 4. [実行](#anchor4)|

<!--
| 5. [](#anchor5)| -->

<a id="anchor1"></a>
## 1. 概要
競馬AIを開発するプロジェクトです。旧リポジトリ→[keibaAI_disable](https://github.com/poi-ai/keibaAI_disable)

本リポジトリでは、データスクレイピングからクレンジング、モデル構築、予測まで一通りのソースコードを管理予定です。

学習データは容量の都合上本リポジトリでは扱わず、Google Driveなどで管理を行なっております。
(ある程度完成に近づいたらprivateに変更予定です。)

~~各PGの説明等、詳細は[Wiki](https://github.com/poi-ai/keibaAI/wiki)に記載予定です。~~

<a id="anchor2"></a>
## 2. 開発環境

### 動作確認バージョン
Python >= 3.9.13<br>
pip >= 22.3.1<br>
MySQL >= 8.0.31

### 使用外部ライブラリ
`requirements.txt`に記載

### 動作確認OS
* Windows 10 (Python 3.10.2)
* CentOS 7 (Python 3.9.13)

<a id="anchor3"></a>
## 3. 初期設定
### clone

#### HTTPS
```
$ git clone https://github.com/poi-ai/keibaAI.git
```

#### SSH
```
$ git clone git@github.com:poi-ai/keibaAI.git
```

### pipのアップデート
```
$ python -m pip install pip==22.3.1
```

### 外部ライブラリのインストール
```
$ pip install -r requirements.txt
```

### 共通ディレクトリをモジュールパスに追加

#### Windows

##### 画面から設定
検索ボックスでenvと入力→「システム環境変数の編集」→「環境変数(N)」→「PYTHONPATH」の変数値に`<ローカルリポジトリのパス>\src\common;<ローカルリポジトリのパス>\config`を追加

##### プロンプトから設定

管理者としてコマンドプロンプトを起動(Ctrl + Shiftを押しながらコマンドプロンプトを起動)し、下記コマンドを実行

```
$ echo %PYTHONPATH%
```

`%PYTHONPATH%`と出力されたら、

```
$ setx /m PYTHONPATH "<ローカルリポジトリのパス>\src\common;<ローカルリポジトリのパス>\config"
```

何かしらのパスが出力されたら、

```
$ setx /m PYTHONPATH "%PYTHONPATH%;<ローカルリポジトリのパス>\src\common;<ローカルリポジトリのパス>\config"
```

を実行する

#### Linux
profileファイルの編集操作を行う下記コマンドを実行

```
$ sudo vi ~/.bash_profile
```

ファイルの末尾に下記を追加

```
PYTHONPATH=$PYTHONPATH:<ローカルリポジトリのパス>/src/common:<ローカルリポジトリのパス>/config
export PYTHONPATH
```

下記コマンド実行で追加した内容を反映させる

```
$ source ~/.profile
```

<a id="anchor4"></a>
## 4. 実行

* `/config/config.py.sample`をコピーし、同階層に`config.py`という名前で保存
* `config.py`へ起動させるシステムや設定値の記載
* `/config/dbconfig.py.sample`をコピーし、同階層に`dbconfig.py`という名前で保存
* `dbconfig.py`へデータベースの接続設定の記載

上記設定を行った後に、

```
$ cd <ローカルリポジトリのパス>
$ python main.py
```

で実行できる
