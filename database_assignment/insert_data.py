from create_tables import Users, Workouts, Nutrition, Sleep, Mental_Wellbeing, engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

# Predefined lists for workouts, food items and personal goals.
workout_types = ['Running', 'Swimming', 'Cycling', 'Yoga', 'Gym','Walking']
food_items = [('Pizza', 300, 40, 12, 10), ('Burger', 250, 30, 15, 12), ('Salad', 150, 20, 5, 2)]
fitness_goals_list = [
    "Lose 10 pounds in 3 months",
    "Increase bench press weight by 20 pounds",
    "Run a marathon in under 4 hours",
    "Achieve a toned body for summer",
    "Increase flexibility and core strength",
    "Complete a triathlon",
    "Reduce body fat percentage to 15%",
    "Build muscle mass in arms and legs",
    "Improve cardiovascular endurance",
    "Maintain a consistent workout routine",
    "Achieve a balanced diet",
    "Reduce sugar intake",
    "Increase stamina for long hikes",
    "Participate in a bodybuilding competition",
    "Improve mental well-being through exercise",
    "Engage in regular yoga and meditation",
    "Achieve a V-shape torso",
    "Improve posture and reduce back pain",
    "Increase daily step count to 10,000",
    "Engage in team sports regularly"
]

# Generate random user profiles
for _ in range(100):
    user = Users(
        name=fake.name(),
        age=fake.random_int(min=18, max=90),
        gender=fake.random_element(elements=('M', 'F')),
        weight=round(random.uniform(50, 150), 2),
        height=round(random.uniform(150, 200), 2),
        fitness_goals=random.choice(fitness_goals_list)
    )
    session.add(user)


# Randomly assign workouts and food items to users
for user in session.query(Users).all():
    for _ in range(10):
        workout = Workouts(userID=user.userID, type=random.choice(workout_types), duration=random.uniform(0.5, 2), calories_burned=random.uniform(100, 500))
        session.add(workout)

        food = random.choice(food_items)
        nutrition = Nutrition(userID=user.userID, food_item=food[0], calories=food[1], carbs=food[2], proteins=food[3], fats=food[4])
        session.add(nutrition)

        sleep = Sleep(userID=user.userID, duration=random.uniform(4, 12), sleep_quality_score=random.uniform(0, 100), interruptions=random.randint(0, 5))
        session.add(sleep)

        mental_wellbeing = Mental_Wellbeing(userID=user.userID, stress_level=random.randint(0, 100), meditation_duration=random.uniform(0, 1))
        session.add(mental_wellbeing)

session.commit()
