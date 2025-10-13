import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

def create_db_engine():
    load_dotenv()

    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DB')

    try:
        MYSQL_PORT = int(MYSQL_PORT) if MYSQL_PORT else 3306
    except ValueError:
        print("Ошибка: Некорректное значение порта в .env. Используется значение по умолчанию: 3306")
        MYSQL_PORT = 3306

    return create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}')

engine = create_db_engine() 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 


def get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

