from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "username": "Suzuki", "email": "suzuki@example.com"},
    {"id": 2, "username": "Sato", "email": "sato@example.com"}
]

@app.get("/")
def read_root():
    return {"message": "API is running"}

# 課題3: "/api/users" へのGETリクエストで、上記のusersリストを返すエンドポイントを作成してください。

# --- ここにコードを書いてください ---


# --- ここまで ---