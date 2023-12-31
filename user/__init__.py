from pydantic import BaseModel
from fastapi import Form


# Класс валидации для регистрации
class UserRegisterModel(BaseModel):
    name: str = Form(...)
    email: str = Form(...)
    password: str = Form(...)


# Класс валидации для входа
class UseLoginModel(BaseModel):
    name: str = Form(...)
    password: str = Form(...)


