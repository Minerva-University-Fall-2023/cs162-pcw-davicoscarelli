from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base
from .user import User
from sqlalchemy.orm import relationship



class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Integer)
    description = Column(String)
    user = relationship(User)
