from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

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