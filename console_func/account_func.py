from sqlalchemy.orm import Session
from database_func.account_db import *
from database_func.transaction_db import create_transaction
import random
import string

def generate_account_number(length: int = 20) -> str:
    """Генерирует случайный номер счета из цифр"""
    digits = string.digits
    return ''.join(random.choices(digits, k=length))


def create_account_console(db: Session, user_id):
    """создание нового счета из косоли"""
    try:
        while True:
            acc_number = generate_account_number(20)
            check = check_account(db, number=acc_number)
            if check:
                continue
            else:
                title = input('Введите название вашего счета: ')
                print(f'Вы уверены что хотите создать новый счет с названием: {title}')
                choice = input('ДА: 1\nНЕТ: 2\n')
                if choice == '1':
                    create_account(db, title, acc_number, user_id)
                    print('Счет успешно создан!')
                else:
                    print('Создание отменено!')
                break
    except Exception as e:
        print(f'Ошибка при создании счета: {e}')
                
                
def transfer_of_funds_console(db: Session, user_id):
    """Перевод средств между счетами"""
    try:
        print("-----ПЕРЕВОД ПО НОМЕРУ СЧЕТА-----")
        POINT = 0
        dict_acc = {}
        accounts = get_accounts(db, user_id)
        if accounts:
            for acc in accounts:
                POINT = POINT + 1
                dict_acc[POINT] = acc
                print(f'{POINT} | НАЗВАНИЕ: {acc.title} | НОМЕР СЧЕТА: {acc.account_number} | БАЛАНС: {acc.balance}')
            while True:
                change = int(input('Выберите с какого счета будет осуществлен перевод(напиши цифру указанную рядом с номером): '))
                if change not in dict_acc.keys():
                    print('НЕВЕРНЫЙ ВЫБОР СЧЕТА, ПОВТОРИТЕ ПОПЫТКУ!')
                    continue
                else:
                    owner_acc = dict_acc[change].account_number
                    print('Счет успешно выбран!')
                    break
            account_number = input('Введите номер счета получателя: ')
            value = int(input('Введите сумму перевода: '))
            balance = get_balance(db, owner_acc) # в аргументе передается номер счета отправителя чтобы проверить его на доступность средств для перевода
            if value > balance:
                print('Недостаточно средств для совершения перевода. Пополните баланс!')
                return
            else:
                if check_account(db, account_number):
                    transfer_of_funds(db, owner_acc, -value)#вычетание суммы
                    transfer_of_funds(db, account_number, value)#прибавление 
                    description = 'перевод'
                    account_id = check_account(db, owner_acc)
                    create_transaction(db, value, description, account_id.id)
                    print('Перевод прошел успешно!')
                    print(f'НОМЕР СЧЕТА ПОЛУЧАТЕЛЯ: {account_number}')
                    return 
                else:
                    print('ОПЕРАЦИЯ ОТМЕНЕННА, ПОЛЬЗОВАТЕЛЯ С ТАКИМ СЧЕТОМ НЕ СУЩЕСТВУЕТ!')
                    return
        else:
            print('У вас нету активных счетов!')
            return
    except Exception as e:
        print(f'ОШИБКА ПРИ ПЕРЕВОДЕ: {e}')
        return

def get_accounts_console(db: Session, user_id): 
    """вывод всех счетов в консоле"""
    accounts = get_accounts(db, user_id)
    print("-----Ваши счета!-----")
    if accounts:
        for i in accounts:
            print(f"НАЗВАНИЕ: {i.title} | НОМЕР: {i.account_number} | БАЛАНС: {i.balance}")
    else:
        print('У вас нету активных счетов!')
    print('---------------------')
    return
