from fastapi import APIRouter, Request, Form
from datetime import datetime

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from database.userservice import add_new_user_db
from user import UserRegisterModel

user_router = APIRouter(prefix='/user', tags=['Работа с пользователем'])
template = Jinja2Templates(directory='templates')


# Регистрация пользователя ввод данных (name, email, password)
@user_router.post('/register')
async def register_user(name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    result = add_new_user_db(reg_date=datetime.now(), name=name, email=email, password=password)
    return RedirectResponse('/', status_code=302)


# Регистрация пользователя страница
@user_router.get('/register')
async def register_user_get(request: Request):
    return template.TemplateResponse('register.html', {'request': request})



# логин пользователя страница
@user_router.get('/login')
async def login_user_get(request: Request):
    return template.TemplateResponse('login.html', {'request': request})



