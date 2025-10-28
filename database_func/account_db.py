from sqlalchemy.orm import Session
from model import Account
from datetime import datetime
from sqlalchemy import select, update



def create_account(db: Session, title: str, number: str, user_id: int):

    account = Account(title=title, account_number=number, user_id=user_id)

    db.add(account)
    db.commit()
    db.refresh(account)
    return account





def transfer_of_funds(db: Session, number, value):
    """Перевод средств между счетами"""
    query = (update(Account).where(Account.account_number==number).values(balance=Account.balance + value))
    result = db.execute(query)
    db.commit()
    if result.rowcount > 0:
        return True
    else:
        return False

def get_accounts(db: Session, user_id: int):
    """вывод всех счетов пользователя по его id"""
    query = (select(Account).where(Account.user_id==user_id))
    result = db.execute(query)
    result = result.scalars().all()
    if result:
        return result
    else:
        return False



def check_account(db: Session, number):
    """вывод аккаунта по номеру счета"""
    query = (select(Account).where(Account.account_number==number))
    result = db.execute(query)
    result = result.scalars().first()
    if result:
        return result
    else:
        return False

def get_balance(db: Session, number):
    """вывод баланса по номеру счета"""
    query = (select(Account.balance).where(Account.account_number==number))
    result = db.execute(query)
    result = result.scalars().first()
    if result:
        return result
    else:
        return False

