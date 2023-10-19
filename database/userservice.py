from database.models import User, Category, Product
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

# Вывести все профессии
def get_all_category_db():
    db = next(get_db())
    all_category = db.query(Category).all()
    return all_category

# Вывести всех сотрудников
def get_all_product_db():
    db = next(get_db())
    all_product = db.query(Product).all()
    return all_product

# Получить информацию определенного сотрудника
def get_exact_product_db(product_id):
    db = next(get_db())
    # Запрос в базу данных на получение определенного сотрудника по его id
    exact_product = db.query(Product).filter_by(product_id=product_id).first()
    return exact_product

# Получить информацию определенной профессии
def get_exact_category_db(product_category):
    db = next(get_db())
    # Запрос в базу данных на получение профессии по id
    exact_category = db.query(Product).filter_by(product_category=product_category).all()
    return exact_category








