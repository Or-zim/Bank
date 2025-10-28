from sqlalchemy.orm import Session
from model import Transaction
from datetime import datetime
from sqlalchemy import select


def get_transaction(db: Session, acc_id):
    """вывод всех транзакций по id счета"""
    query = (select(Transaction).where(Transaction.account_id == acc_id))
    result = db.execute(query)
    result = result.scalars().all()
    if result:
        return result
    else:
        False



def create_transaction(db: Session, amount, description, account_id):
    """создание транцзакции"""
    db_transaction = Transaction(amount=amount, description=description, account_id=account_id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction