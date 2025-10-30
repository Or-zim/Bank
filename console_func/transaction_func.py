from sqlalchemy.orm import Session
from database_func.transaction_db import *
from database_func.account_db import get_accounts


def get_transaction_console(db: Session, user_id):
    """вывод всех транзакцый по номеру счета в косоле"""
    try:
        print("-----ИСТОРИЯ ТРАНЗАКЦИЙ-----")
        POINT = 0
        dict_acc = {}
        accounts = get_accounts(db, user_id)
        if accounts:
            print('0. ПОСМОТРЕТЬ ИСТОРИЮ ВСЕХ ТРАНЗАКЦИЙ')
            for acc in accounts:
                POINT = POINT + 1
                dict_acc[POINT] = acc
                print(f'{POINT} | НАЗВАНИЕ: {acc.title} | НОМЕР СЧЕТА: {acc.account_number} | БАЛАНС: {acc.balance}')
            while True:
                choice = int(input('Выберите историю какого счета вы хотите посмотреть(напиши цифру указанную рядом с номером): '))
                if choice not in dict_acc.keys() and choice != 0:
                    print('НЕВЕРНЫЙ ВЫБОР СЧЕТА, ПОВТОРИТЕ ПОПЫТКУ!')
                    continue
                elif choice == 0:
                    transactions = []
                    for acc in accounts:
                        if acc:
                            if get_transaction(db, acc.id):
                                transactions.extend(get_transaction(db, acc.id))
                    print('ИСТОРИЯ ВСЕХ ТРАНЗАКЦИЙ')
                    if transactions:
                        for trans in transactions:
                            print(f'ДАТА: {trans.transaction_date} | СУММА: {trans.amount} | ОПИСАНИЕ: {trans.description}')
                        break
                    else:
                        print("ИСТОРИЯ ТРАНЗАКЦИЙ ПУСТА!")
                        break
                else:
                    owner_acc = dict_acc[choice].id
                    transactions = get_transaction(db, owner_acc)
                    if transactions:
                        print(f'ИСТОРИЯ ТРАНЗАКЦИЙ СЧЕТА: {dict_acc[choice].title}')
                        for trans in transactions:
                            print(f'ДАТА: {trans.transaction_date} | СУММА: {trans.amount} | ОПИСАНИЕ: {trans.description}')
                    else:
                        print('Этот счет не имеет транзакций!')
                    break
        else:
            print('У вас нету активных счетов!')
            return
    except Exception as e:
        print(f'ОШИБКА ПРИ ПРОСМОТРЕ ТРАНЗАКЦИЙ: {e}')
        return

