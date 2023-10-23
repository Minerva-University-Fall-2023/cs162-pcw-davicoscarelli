from sqlalchemy.orm import sessionmaker
from models.base import engine, Session
from models.user import User
from models.transaction import Transaction

Session = sessionmaker(bind=engine)

def insert_user(name):
    session = Session()
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    user_id = new_user.id
    return user_id

def insert_transaction(user_id, amount, description):
    session = Session()
    new_transaction = Transaction(user_id=user_id, amount=amount, description=description)
    session.add(new_transaction)
    session.commit()
