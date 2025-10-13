from sqlalchemy.orm import Session
from model import Base, User, Account, Transaction
from services.user_service import * 
from config import get_db, create_db_engine
from sqlalchemy import create_engine

def add_user_from_console(db: Session):
    """Добавляет пользователя, получая данные из консоли."""
    first_name = input("Введите имя пользователя: ")
    last_name = input("Введите фамилию пользователя: ")
    password = input("Введите пароль пользователя: ")

    if not first_name or not last_name or not password:
        print("Ошибка: Необходимо ввести все данные пользователя.")
        return

    try:
        new_user = create_user(db, first_name, last_name, password)
        print(f"Пользователь {new_user.first_name} {new_user.last_name} успешно добавлен с ID: {new_user.id}")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")


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
        print("1. Добавить пользователя")
        print("2. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            add_user_from_console(db)
        elif choice == "2":
            print("Выход из приложения.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

    db.close() # Закрываем сессию

if __name__ == "__main__":
    main()










