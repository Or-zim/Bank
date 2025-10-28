import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from sqlalchemy.orm import Session
from console_func.user_func import get_user_data_console
from console_func.account_func import transfer_of_funds_console, create_account_console, get_accounts_console
from console_func.transaction_func import get_transaction_console




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





def enter_user(db: Session, user_id, first_name, last_name):
    """функция для описания функционала приложения аторизованного пользователя"""
    while True:
        print("\n----------MENU----------")
        print("1. Профиль")
        print("2. Перевод")
        print("3. История транзакций")
        print("4. Новый счет")
        print("5. Выход и аккаунта")
        choice = input('\nВыбирете действие: ')
        if choice == '1':
            print('\n-----------ПРОФИЛЬ----------')
            print(f'ИМЯ: {first_name}')
            print(f'ФАМИЛИЯ: {last_name}')
            get_accounts_console(db, user_id)
            continue
        elif choice == '2':
            transfer_of_funds_console(db, user_id)
            continue
        elif choice == '3':
            get_transaction_console(db, user_id)
            continue
        elif choice == '4':
            create_account_console(db, user_id)
            continue
        elif choice == '5':
            print("Выход из аккаунта.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")
