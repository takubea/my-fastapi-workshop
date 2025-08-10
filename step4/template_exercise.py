from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users_data = [
    {"id": 1, "username": "Suzuki", "email": "suzuki@example.com"},
    {"id": 2, "username": "Sato", "email": "sato@example.com"}
]

@app.get("/users-page")
def show_users_page(request: Request):
    # 課題4: users.htmlテンプレートを返し、users_dataを渡してください。
    # ヒント: return templates.TemplateResponse("ファイル名", {"request": request, "渡すデータ名": データ})
    
    # --- Pythonのコードをここに書いてください ---
    pass # この行は消してください
    # --- ここまで ---