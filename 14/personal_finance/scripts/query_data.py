from sqlalchemy.orm import sessionmaker
from models.base import engine, Session
from models.user import User
from models.transaction import Transaction



Session = sessionmaker(bind=engine)

def get_transactions_by_user_name(name):
    session = Session()
    return session.query(Transaction).join(User).filter(User.name == name).all()
