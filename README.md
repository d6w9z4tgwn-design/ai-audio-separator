# ai-audio-separator

DemucsをGUIから実行して音源分離。

Tkinter frontend for Demucs source separation.

## Setup / 起動
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## Usage / 使用例
`python app.py` (GUI) or `python app.py input.wav --output output`. Model download, FFmpeg and compatible PyTorch/torchaudio may be required. Inference not verified.

Python 3.10+ recommended. AI-generated development assistance was used.
