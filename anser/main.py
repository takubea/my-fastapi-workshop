from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# "templates"フォルダをテンプレート置き場として指定
templates = Jinja2Templates(directory="templates")

# データベースの代わりに、Pythonのリストでコメントを保存（サーバー再起動でリセットされます）
comments = []

@app.get("/")
def read_root(request: Request):
    """
    トップページを表示します。
    GETリクエストを受け取り、保存されているコメントリストと共に掲示板ページを返します。
    """
    return templates.TemplateResponse("guestbook.html", {"request": request, "comments": comments})

@app.post("/add")
def add_comment(username: str = Form(), comment_text: str = Form()):
    """
    新しいコメントを追加します。
    POSTリクエストでフォームデータを受け取り、コメントリストに追加後、トップページにリダイレクトします。
    """
    new_comment = {"username": username, "text": comment_text}
    comments.append(new_comment)
    
    # コメント追加後、PRG(Post-Redirect-Get)パターンでリダイレクト
    return RedirectResponse(url="/", status_code=303)

# このファイルが直接実行されたときにUvicornサーバーを起動するための記述
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)