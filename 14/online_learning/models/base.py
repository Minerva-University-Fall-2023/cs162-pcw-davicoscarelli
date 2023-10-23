from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Replace this with your actual database URL
DATABASE_URL = "sqlite:///test.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
