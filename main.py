from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from database import Base, engine
from database.userservice import get_all_category_db, get_all_product_db, get_exact_product_db, get_exact_category_db

from user.user_api import user_router


# Создать базу данных
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

## Если хотим выводить html странички
template = Jinja2Templates(directory='templates')
## Если хотим выводить html странички

# Регистрация компонентов
app.include_router(user_router)

# роут для главной страницы
@app.get('/')
async def home(request: Request):
    category = get_all_category_db()
    product = get_all_product_db()
    return template.TemplateResponse('index.html', {'request': request, 'category': category, 'product': product})


# роут для страницы about
@app.get('/about')
async def about(request: Request):
    category = get_all_category_db()
    product = get_all_product_db()
    return template.TemplateResponse('about.html', {'request': request, 'category': category, 'product': product})


# роут для страницы contacts
@app.get('/contacts')
async def contacts(request: Request):
    category = get_all_category_db()
    product = get_all_product_db()
    return template.TemplateResponse('contacts.html', {'request': request, 'category': category, 'product': product})


# роут для страницы news_home
@app.get('/news_home')
async def news_home(request: Request):
    category = get_all_category_db()
    product = get_all_product_db()
    return template.TemplateResponse('news_home.html', {'request': request, 'category': category, 'product': product})

# роут для страницы персонал
@app.get('/product/{product_id}')
async def exact_product(request: Request, product_id: int):
    product_info = get_exact_product_db(product_id=product_id)
    return template.TemplateResponse('exact_product.html', {'request': request, 'product': product_info})


# роут для страницы профессии
@app.get('/category/{category_name}')
async def exact_category(request: Request, category_name: str):
    category_info = get_exact_category_db(product_category=category_name)
    return template.TemplateResponse('exact_category.html', {'request': request, 'products': category_info})

# роут для логина??????????????
@app.get('/login')
async def login(request: Request):
    return template.TemplateResponse('login.html', {'request': request})


# роут для логаута??????????????
@app.get('/logout')
async def logout(request: Request):
    return template.TemplateResponse('index.html', {'request': request})


# роут для страницы register????????????
@app.get('/register')
async def register(request: Request):
    return template.TemplateResponse('register.html', {'request': request})





