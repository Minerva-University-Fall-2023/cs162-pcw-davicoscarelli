from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    userID = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    weight = Column(Float)
    height = Column(Float)
    fitness_goals = Column(String)

class Workouts(Base):
    __tablename__ = 'workouts'
    workoutID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('users.userID'))
    type = Column(String)
    duration = Column(Float)
    calories_burned = Column(Float)

class Nutrition(Base):
    __tablename__ = 'nutrition'
    logID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('users.userID'))
    food_item = Column(String)
    calories = Column(Float)
    carbs = Column(Float)
    proteins = Column(Float)
    fats = Column(Float)

class Sleep(Base):
    __tablename__ = 'sleep'
    sleepID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('users.userID'))
    duration = Column(Float)
    sleep_quality_score = Column(Float)
    interruptions = Column(Integer)

class Mental_Wellbeing(Base):
    __tablename__ = 'mental_wellbeing'
    entryID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('users.userID'))
    stress_level = Column(Integer)
    meditation_duration = Column(Float)

engine = create_engine('sqlite:///health_fitness_app.db')
Base.metadata.create_all(engine)
