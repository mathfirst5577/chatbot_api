from fastapi import FastAPI
from pydantic import BaseModel

# vectorstore と chain_with_context は、あらかじめセットアップ済みの変数として用意されている前提です
app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_api(request: QueryRequest):
    query = request.question

    # FAISS を使って類似ドキュメントを検索する（事前に作成された vectorstore を利用）
    retrieved_docs = vectorstore.similarity_search(query, k=4)
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    # chain_with_context を使って回答を生成する
    answer = chain_with_context.run({"question": query, "context": context})
    return {"question": query, "answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
