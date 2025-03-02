# GPU が不要な場合は、標準の Python ベースイメージを使います
FROM python:3.11-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存パッケージリストをコピーしてインストール
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# アプリケーションコードのコピー
COPY . .

# API サーバーの起動（FastAPI アプリケーションを uvicorn で起動）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
