from sqlalchemy import Integer, DateTime, Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from database import Base

# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)

    reg_date = Column(DateTime)

# Таблица профессий
class Category(Base):
    __tablename__ = 'categorys'
    category_id = Column(Integer, autoincrement=True, primary_key=True)
    category_name = Column(String)

# Таблица персонала
class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, autoincrement=True, primary_key=True)
    product_name = Column(String)
    product_category = Column(Integer, ForeignKey('categorys.category_id'))
    product_des = Column(String)
    product_price = Column(Float)
    product_photo = Column(String)
    product_amount = Column(Integer)
    product_city = Column(String)

    profession_fk = relationship(Category, lazy='subquery')


# Таблица найма
class Cart(Base):
    __tablename__ = 'carts'
    carts_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user_product = Column(Integer, ForeignKey('products.product_id'))
    user_product_count = Column(Integer)

    user_fk = relationship(User, lazy='subquery')
    personal_fk = relationship(Product, lazy='subquery')
