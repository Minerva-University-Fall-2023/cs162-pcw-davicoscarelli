from sqlalchemy import Column, Integer, String
from .base import Base

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
