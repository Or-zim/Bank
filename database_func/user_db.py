from sqlalchemy.orm import Session
from sqlalchemy import select
from model import User
from datetime import datetime

def create_user(db: Session, first_name: str, last_name: str, password:str):
    """Создание нового пользователя"""
    db_user = User(first_name=first_name, last_name=last_name, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def logaut_user(db: Session, first_name: str, last_name: str, password:str):
    """Осуществляет вход пользователя по имени фамилии и паролю"""
    query = (select(User)
        .where(User.first_name == first_name)
        .where(User.last_name == last_name)
        .where(User.password == password)  
    )
    
    result = db.execute(query)
    result = result.scalars().first()
    return result
    


def get_user_data(db: Session, id):
    """Вывод информации по пользователе по id"""
    