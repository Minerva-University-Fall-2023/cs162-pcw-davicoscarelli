from create_tables import Users, Workouts, Nutrition, Sleep, Mental_Wellbeing, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc

Session = sessionmaker(bind=engine)
session = Session()

def nutrition_sleep_correlation(user_id):
    """
    Explanation:
    Calculates the correlation between a user's nutrition (specifically carb intake) and sleep quality.
    
    Input:
    user_id (int): The ID of the user for whom the correlation is to be calculated.
    
    Output:
    float: A value representing the correlation between average carb intake and average sleep quality score.
    The output is a ratio of average carb intake to average sleep quality score. 
    A higher value might indicate that increased carb intake negatively affects sleep quality, while a lower value might suggest the opposite.
    
    Strengths:
    By understanding how nutrition affects sleep, users can make informed decisions about their diet to improve sleep quality.
    """
    avg_carb_intake = session.query(func.avg(Nutrition.carbs)).filter(Nutrition.userID == user_id).scalar()
    avg_sleep_score = session.query(func.avg(Sleep.sleep_quality_score)).filter(Sleep.userID == user_id).scalar()
    correlation = avg_carb_intake / avg_sleep_score if avg_sleep_score else 0
    return correlation

def nutrition_workouts_correlation(user_id):
    """
    Explanation:
    Determines how a user's nutrition, specifically carb intake, affects their workout performance.
    
    Input:
    user_id (int): The ID of the user for whom the analysis is to be done.
    
    Output:
    list of tuples: Each tuple contains the carb intake and average calories burned during workouts.
    A higher carb intake with more calories burned indicates a positive impact of nutrition on workouts.
    
    Strengths:
    Users can understand the importance of nutrition in their workout performance and adjust their diet for optimal results.
    """
    return session.query(
        Nutrition.carbs,
        func.avg(Workouts.calories_burned).label('avg_calories_burned')
    ).join(Workouts, Nutrition.userID == Workouts.userID).filter(Nutrition.userID == user_id).group_by(Nutrition.carbs).all()

def sleep_vs_mental_wellbeing(user_id):
    """
    Explanation:
    Analyzes the correlation between sleep duration and stress levels to understand the impact of sleep on mental well-being.
    
    Input:
    user_id (int): The ID of the user for whom the correlation is to be analyzed.
    
    Output:
    list of tuples: Each tuple contains sleep duration and average stress level.
    The output provides insights into how sleep duration affects stress levels. 
    Longer sleep with lower stress indicates a positive impact of sleep on mental well-being.
    
    Strengths:
    By understanding the importance of sleep duration on mental health, users can prioritize their sleep routines for better mental well-being.
    """
    return session.query(
        Sleep.duration,
        func.avg(Mental_Wellbeing.stress_level).label('avg_stress_level')
    ).join(Mental_Wellbeing, Sleep.userID == Mental_Wellbeing.userID).filter(Sleep.userID == user_id).group_by(Sleep.duration).all()

def dynamic_recommendations(user_id):
    """
    Explanation:
    Provides dynamic recommendations based on a user's sleep score.
    
    Input:
    user_id (int): The ID of the user for whom the recommendations are to be generated.
    
    Output:
    list of strings: Each string is a recommendation for the user.
    The recommendations are based on the user's average sleep score. 
    If the score is below a certain threshold, the user receives specific advice to improve their sleep.
    The outputs can be expanded to have different recommendations for different thresholds.
    
    Strengths:
    Personalized recommendations can guide users to make changes that directly benefit their health.
    """
    poor_sleep_score = 50  # Threshold for poor sleep
    avg_sleep_score = session.query(func.avg(Sleep.sleep_quality_score)).filter(Sleep.userID == user_id).scalar()
    recommendations = []

    if avg_sleep_score < poor_sleep_score:
        recommendations.append("Consider increasing protein intake for better sleep.")
        recommendations.append("Try low-intensity workouts like Yoga or Meditation to improve sleep quality.")
    
    return recommendations



def personalized_workout_recommendations(user_id):
    """
    Explanation:
    Recommends popular workout types based on a user's fitness goals by analyzing the preferences of users with similar goals.
    
    Input:
    user_id (int): The ID of the user for whom the recommendations are to be generated.
    
    Output:
    list of tuples: Each tuple contains the workout type and its count, indicating how many users with similar fitness goals prefer that workout.
    The list is ordered by preference. It shows which workouts are most preferred by users with specific fitness goals, helping the user to align their workouts with their goals.
    
    Strengths:
    Personalized recommendations can motivate users to try new workouts and achieve their fitness goals more effectively.
    """
    user_goal = session.query(Users.fitness_goals).filter(Users.userID == user_id).scalar()
    return session.query(
        Workouts.type,
        func.count(Workouts.type).label('count')
    ).join(Users, Workouts.userID == Users.userID).filter(Users.fitness_goals == user_goal).group_by(Workouts.type).order_by(desc('count')).all()
 

def mental_workout_correlation():
    """
    Explanation:
    Finds the correlation between mental well-being and workout intensity.
    
    Output:
    list of tuples: Each tuple contains the workout type, average workout duration, and average stress level.
    The output provides insights into how different workouts correlate with stress levels.
    A higher average duration with a lower stress level indicates a positive impact of that workout on mental well-being.
    
    Strengths:
    Users can understand how their mental well-being affects their workout performance and vice versa.
    """
    return session.query(
        Workouts.type,
        func.avg(Workouts.duration).label('avg_duration'),
        func.avg(Mental_Wellbeing.stress_level).label('avg_stress_level')
    ).join(Mental_Wellbeing, Workouts.userID == Mental_Wellbeing.userID).group_by(Workouts.type).all()

def fitness_goal_workout_preference():
    """
    Explanation:
    Determines the preferred workout type for users with specific fitness goals.
    
    Output:
    list of tuples: Each tuple contains the fitness goal, workout type, and count of users with that goal preferring the workout.
    The list is ordered by preference. It shows which workouts are most preferred by users with specific fitness goals.
    
    Strengths:
    By understanding user preferences, the app can provide better workout recommendations aligned with user goals.
    """
    return session.query(
        Users.fitness_goals,
        Workouts.type,
        func.count(Workouts.type).label('count')
    ).join(Workouts, Users.userID == Workouts.userID).group_by(Users.fitness_goals, Workouts.type).order_by(desc('count')).all()




# Sample usage
user_id = 1

# User Centered
print(f"Nutrition-Sleep Correlation for User {user_id}: {nutrition_sleep_correlation(user_id)}\n\n")
print(f"Dynamic Recommendations for User {user_id}: {dynamic_recommendations(user_id)}\n\n")
print(f"Nutrition Impact on Workouts for User {user_id}: {nutrition_workouts_correlation(user_id)}\n\n")
print(f"Sleep Duration vs. Mental Well-being for User {user_id}: {sleep_vs_mental_wellbeing(user_id)}\n\n")
print(f"Personalized Workout Recommendations for User {user_id}: {personalized_workout_recommendations(user_id)}\n\n")

# Global Analysis
print(f"Mental-Workout Correlation: {mental_workout_correlation()}\n\n")
print(f"Fitness Goal-Workout Preference: {fitness_goal_workout_preference()}\n\n")



session.close()
