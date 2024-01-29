# Python + pyenv + poetry + venv + Docker + MySQLによるCIL TODOリスト
***
### 環境構築
***
1. DevContainerでappフォルダ内をロードする
2. コンテナに接続できたら下記コマンドを順に実行
    1. poetry.tomlを生成
    `poetry config virtualenvs.in-project true --local`
    2. poetryが使用するpythonインタープリタを設定
    `poetry env use /home/vscode/.pyenv/shims/python`
    3. 依存関係をインストール
    `poetry install`
3. VSCode拡張機能やPythonインタープリタのパスを正常に読み込ませるためにVSCodeをリロードする
4. 絶対インポートをできるよう、ターミナルで下記コマンドを実行し、PYTHONPATHを設定する
    `export PYTHONPATH="/app/cli-todo/src:$PYTHONPATH"`
    `export PYTHONPATH="/app/cli-todo/tests:$PYTHONPATH"`
