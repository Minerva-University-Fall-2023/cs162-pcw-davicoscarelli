from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    """
    Represents a user in the health and fitness tracking app.
    """
    __tablename__ = 'users'
    userID = Column(Integer, primary_key=True)  # Unique identifier for the user
    name = Column(String)  # Name of the user
    age = Column(Integer)  # Age of the user
    gender = Column(String)  # Gender of the user
    weight = Column(Float)  # Weight of the user in kilograms
    height = Column(Float)  # Height of the user in centimeters
    fitness_goals = Column(String)  # User's fitness goals description

class Workouts(Base):
    """
    Represents a workout session of a user.
    """
    __tablename__ = 'workouts'
    workoutID = Column(Integer, primary_key=True)  # Unique identifier for the workout
    userID = Column(Integer, ForeignKey('users.userID'))  # Reference to the user
    type = Column(String)  # Type of workout (e.g., cardio, strength)
    duration = Column(Float)  # Duration of the workout in minutes
    calories_burned = Column(Float)  # Calories burned during the workout

class Nutrition(Base):
    """
    Represents a nutrition log entry for a user.
    """
    __tablename__ = 'nutrition'
    logID = Column(Integer, primary_key=True)  # Unique identifier for the nutrition log
    userID = Column(Integer, ForeignKey('users.userID'))  # Reference to the user
    food_item = Column(String)  # Name of the food item consumed
    calories = Column(Float)  # Calories in the food item
    carbs = Column(Float)  # Carbohydrates in the food item in grams
    proteins = Column(Float)  # Proteins in the food item in grams
    fats = Column(Float)  # Fats in the food item in grams

class Sleep(Base):
    """
    Represents a sleep log entry for a user.
    """
    __tablename__ = 'sleep'
    sleepID = Column(Integer, primary_key=True)  # Unique identifier for the sleep log
    userID = Column(Integer, ForeignKey('users.userID'))  # Reference to the user
    duration = Column(Float)  # Duration of sleep in hours
    sleep_quality_score = Column(Float)  # Quality score of the sleep (e.g., out of 10)
    interruptions = Column(Integer)  # Number of times the user woke up during sleep

class Mental_Wellbeing(Base):
    """
    Represents a mental wellbeing log entry for a user.
    """
    __tablename__ = 'mental_wellbeing'
    entryID = Column(Integer, primary_key=True)  # Unique identifier for the mental wellbeing log
    userID = Column(Integer, ForeignKey('users.userID'))  # Reference to the user
    stress_level = Column(Integer)  # User's stress level (e.g., out of 10)
    meditation_duration = Column(Float)  # Duration of meditation in minutes

# Create an SQLite database engine
engine = create_engine('sqlite:///health_fitness_app.db')

# Create all tables in the database
Base.metadata.create_all(engine)
