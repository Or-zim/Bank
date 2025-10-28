from sqlalchemy.orm import Session
from database_func.user_db import create_user, logaut_user
import unicodedata
RUS_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def add_user_console(db: Session):
    """Добавляет пользователя, получая данные из консоли."""

    try:
        while True:
            first_name = input("Введите имя пользователя (миниму 2 символа русского алфавита): ").lower()
            first_name = first_name.strip()
            first_name = unicodedata.normalize('NFC', first_name)

            if len(first_name) < 2:
                print('Имя должно состоять минимум из двух символов!')
                continue

            if all(ch in RUS_LOWER for ch in first_name):
                break
            else:
                print('Имя должно состоять из букв русского алфавита!')
                continue
            
        
    except Exception as e:
        print(f'Ошибка при вводе имени: {e}')

    try:
        while True:
            last_name = input("Введите фамилию пользователя: ").lower()
            last_name = last_name.strip()
            last_name = unicodedata.normalize('NFC', last_name)

            
            if len(last_name) < 2:
                print('Фамилия должна должно состоять минимум из двух символов!')
                continue

            if all(ch in RUS_LOWER for ch in last_name):
                break
            else:
                print('Фамилия должно состоять из букв!')
                continue
    except Exception as e:
        print(f"Ошибка при вводе фамили: {e}")
        
    try:
        while True:
            password = input("Введите пароль пользователя: ")
            if len(password) != 12:
                print("Пороль должен состоять строго из 12 симоволов!")
                continue
            else: 
                break
            
    except Exception as e:
        print(f"Ошибка при вводе пароля: {e}")

    try:
        new_user = create_user(db, first_name, last_name, password)
        print(f"Пользователь {new_user.first_name} {new_user.last_name} успешно добавлен с ID: {new_user.id}")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")

def logaut_user_console(db: Session):
    """вход пользователя в аккаунт в консоле"""
    
    try:
        first_name = input('Введите ваше имя: ').strip()
        last_name = input('Введите вашу фамилию: ').strip()
        password = input('Введите пароль: ').strip()
        print('Совершить вход пользователя с данными:')
        print(f'Имя: {first_name}')
        print(f'Фамилия: {last_name}')
        print(f'Пароль {password}')
        choice = input('Да: 1                Нет: 2\n')
        try:
            if choice == '1':
                user = logaut_user(db, first_name.lower(), last_name.lower(), password)
                if user:
                    print('Вы успешно вошли в аккаунт!')
                    return user
                else:
                    print('Пользователя с такими данными не существует!')
                    return
            elif choice == '2':
                print('Отмена входа!')
                return 
            else:
                print('Введите 1 или 2 для выбора действия!')
                return
        except Exception as e:
            print('Данные введены не корректно!')
    except Exception as e:
        print(f"Ошибка при попытке входа{e}")

def get_user_data_console(db: Session):
    """вывод данных пользователя в консоле"""
    