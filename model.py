from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from typing import List
from datetime import datetime


class Base(DeclarativeBase):
    pass



class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(256), nullable=False)
    last_name: Mapped[str] = mapped_column(String(256), nullable=False)
    password: Mapped[str] = mapped_column(String(12), nullable=False)
    date_joined: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    accounts: Mapped[List["Account"]] = relationship(back_populates="user")
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.first_name!r}, last_name={self.last_name!r})"
    

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    account_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    balance: Mapped[float] = mapped_column(Float, default=0.0)
    date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="accounts")
    
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="account")
    
    def __repr__(self):
        return f"Account(id={self.id!r}, account_number={self.account_number!r}, balance={self.balance!r})"



class Transaction(Base):
    __tablename__ = 'transactions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    transaction_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    description: Mapped[str] = mapped_column(String(256), nullable=False)
    
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    account: Mapped["Account"] = relationship(back_populates="transactions")
    def __repr__(self):
        return f"Transaction(id={self.id!r}, amount={self.amount!r}, transaction_date={self.transaction_date!r}, description={self.description!r}, account_id={self.account_id})"