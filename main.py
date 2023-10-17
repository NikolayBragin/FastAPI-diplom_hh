from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from database import Base, engine

from user.user_api import user_router


# Создать базу данных
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

## Если хотим выводить html странички
template = Jinja2Templates(directory='templates')
## Если хотим выводить html странички

# роут для главной страницы
@app.get('/')
async def home(request: Request):
    return template.TemplateResponse('index.html', {'request': request})

# роут для логина
@app.get('/login')
async def login(request: Request):
    return template.TemplateResponse('login.html', {'request': request})

# роут для логаута
@app.get('/logout')
async def logout(request: Request):
    return template.TemplateResponse('logout.html', {'request': request})

# роут для страницы about
@app.get('/about')
async def about(request: Request):
    return template.TemplateResponse('about.html', {'request': request})

# роут для страницы contacts
@app.get('/contacts')
async def contacts(request: Request):
    return template.TemplateResponse('contacts.html', {'request': request})

# роут для страницы news_home
@app.get('/news_home')
async def news_home(request: Request):
    return template.TemplateResponse('news_home.html', {'request': request})



# Регистрация компонентов
app.include_router(user_router)
