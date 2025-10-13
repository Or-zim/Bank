from sqlalchemy.orm import Session
from model import User
from datetime import datetime

def create_user(db: Session, first_name: str, last_name: str, password:str):
    """Создание нового пользователя"""
    db_user = User(first_name=first_name, last_name=last_name, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user