from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
comments = []

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("guestbook.html", {"request": request, "comments": comments})

# 課題5: "/add" へのPOSTリクエストを処理するエンドポイントを作成してください。
# フォームから "username" と "comment_text" を受け取り、
# commentsリストに追加した後、トップページ("/")にリダイレクトしてください。

# --- POSTリクエストを処理するコードをここに書いてください ---


# --- ここまで ---
# このファイルが直接実行されたときにUvicornサーバーを起動するための記述
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
