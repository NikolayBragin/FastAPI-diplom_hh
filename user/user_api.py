from fastapi import APIRouter, Request, Form
from datetime import datetime

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from database.userservice import add_new_user_db, get_all_category_db, get_exact_product_db, get_exact_category_db
from user import UserRegisterModel, UseLoginModel

user_router = APIRouter(prefix='/user', tags=['Работа с пользователем'])
template = Jinja2Templates(directory='templates')

#
# # Регистрация пользователя ввод данных (name, email, password)
# @user_router.post('/register')
# async def register_user(name: str = Form(...), email: str = Form(...), password: str = Form(...)):
#     result = add_new_user_db(reg_date=datetime.now(), name=name, email=email, password=password)
#     print(result)
#     return RedirectResponse('/', status_code=302)
#
#
# # Регистрация пользователя страница
# @user_router.get('/register')
# async def register_user_get(request: Request):
#     return template.TemplateResponse('register.html', {'request': request})

# # логин пользователя ввод данных (name, password)
# @user_router.post('/login')
# async def login_user(name: str = Form(...), password: str = Form(...)):
#     result = login_user_db(name=name, password=password)
#     return RedirectResponse('/', status_code=302)
#
# # логин пользователя страница
# @user_router.get('/login')
# async def login_user_get(request: Request):
#     return RedirectResponse('login')
#
#
# # логаут пользователя страница
# @user_router.get('/logout')
# async def logout_user_get(request: Request):
#     return RedirectResponse('/')

# Запрос на вывод всех профессий
@user_router.get('/categorys')
async def all_category_info():
    categories = get_all_category_db()
    return {'status': 1, 'message': categories}

# Запрос на вывод всех сотрудников
@user_router.get('/product')
async def all_product_info():
    product = get_all_category_db()
    return {'status': 1, 'message': product}

# Запрос на получение определенного сотрудника
@user_router.get('/exact-product')
async def get_exact_product(product_id: int):
    exact_result = get_exact_product_db(product_id)
    if exact_result:
        return {'status': 1, 'message': exact_result}

# Запрос на получение определенной профессии
@user_router.get('/exact-category')
async def get_exact_category(product_category: str):
    exact_category = get_exact_category_db(product_category)
    if exact_category:
        return {'status': 1, 'message': exact_category}
