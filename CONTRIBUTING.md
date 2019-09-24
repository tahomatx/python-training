# machine-learning

## 開発環境の構築

### Githubからソースコードをクローン

ターミナルで次を実行。ホームディレクトリで行うと良い。

```sh
git clone https://github.com/ev-kenjiterai/python-training.git
```

実行すると`python-training`というフォルダが作られ、このファイルを含むコードがダウンロードされる。


### Visual Studio Codeへのフォルダの登録

このフォルダーをVisual Studio Codeに登録します。

1.   左側のフォルダが出ているところを右クリック
2.   **Add Folder to Workspace** をクリック
3.   出てきたダイアログ画面でこのフォルダを選択して開く


### GitKrakenへのレポジトリの登録

1.   一番左上のフォルダーアイコンをクリック
2.   「Open」をクリック
3.   「Open a Repository」をクリック
4.   出てきたダイアログ画面でこのフォルダを選択して開く



### virtualenvによる開発環境の準備

virtualenvの初期化

```sh
virtualenv --python python3 '.virtualenv'
```

virtualenv環境の開始(有効化、アクティベート)

```sh
source ./.virtualenv/bin/activate
```

virtualenv環境の終了

```sh
deactivate
```


### 依存関係のあるライブラリのインストール

pip を使ってライブラリをインストールするとき、インストールしたいライブラリを`requirements.txt`のように記述すると、次のコマンドでまとめてインストールできる。

```sh
pip install -r requirements.txt
```

いまのところ、scikit-learnをインストールする。


## Pythonコードの実行

いまのところ、1つのサンプルコードがある。virtualenvを有効化した状態で次のコマンドで実行できる。

```sh
python c5_scikit_learn/iris.py
```
