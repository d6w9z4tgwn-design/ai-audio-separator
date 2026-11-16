# AI Audio Separator

楽曲ファイルからボーカル・ドラム・ベース・その他の音源を分離するデスクトップツールです。Demucsの処理を、コマンド操作が苦手な人でも使えるシンプルなGUIから実行できます。

## 主な機能

- 音声ファイルと保存先を選ぶだけでDemucsによる4ステム分離を実行
- 長時間の推論をバックグラウンドで処理し、画面の操作を維持
- CLIからの自動処理にも対応

## セットアップ
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## 使い方

`python app.py` でGUIを起動します。CLIでは `python app.py input.wav --output output` を実行します。

初回はモデルのダウンロードが発生します。Demucsの実行にはFFmpegと、環境に合うPyTorch/torchaudioが必要です。処理結果は指定フォルダにDemucs標準の構成で保存されます。

Python 3.10+ 推奨。実際の推論は環境ごとに確認してください。
