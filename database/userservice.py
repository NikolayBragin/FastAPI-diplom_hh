from database.models import User
from database import get_db

# Регистрация пользователя (name, email, password, reg_date)
def add_new_user_db(name, email, password, reg_date):
    db = next(get_db())
    new_user = User(user_name=name, user_email=email, user_password=password, reg_date=reg_date)
    db.add(new_user)
    db.commit()
    return "Пользователь успешно зарегестрирован"

# Логин пользователя
def login_user_db(name, password):
    db = next(get_db())
    new_user = User(user_name=name, user_password=password)
    db.add(new_user)
    db.commit()
    return "Пользователь успешно зашел"







