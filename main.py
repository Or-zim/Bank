from sqlalchemy.orm import Session
from model import Base, User, Account, Transaction
from database_func.user_db import *
from config import get_db, create_db_engine, enter_user
from sqlalchemy import create_engine
from console_func.user_func import add_user_console, logaut_user_console 




def create_database():  # Добавлена функция create_database
    engine = create_db_engine()
    Base.metadata.create_all(engine)
    print('Успешное подключение')


def main():
    """Основная функция приложения."""

    create_database()  # Создаем базу данных, если ее нет
    db: Session = next(get_db())  # Получаем сессию базы данных

    while True:
        print("\nВыберите действие:")
        print("1. Вход")
        print("2. Регистрация")
        print("0. Выход из приложения")
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            user = logaut_user_console(db)
            if user:
                enter_user(db=db, user_id=user.id, first_name=user.first_name, last_name=user.last_name)
                continue
            else:
                continue
        elif choice == "2":
            add_user_console(db)
            continue
        elif choice == "0":
            print("Выход из приложения.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

    db.close() 

if __name__ == "__main__":
    main()










