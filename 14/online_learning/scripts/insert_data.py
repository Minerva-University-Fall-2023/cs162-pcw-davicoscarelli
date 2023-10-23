from sqlalchemy.orm import sessionmaker
from models.base import engine, Session
from models.user import User
from models.course import Course
from models.enrollment import Enrollment

Session = sessionmaker(bind=engine)

def insert_user(name):
    session = Session()
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    user_id = new_user.id
    return user_id

def insert_course(name):
    session = Session()
    new_course = Course(name=name)
    session.add(new_course)
    session.commit()
    course_id = new_course.id
    return course_id

def insert_enrollment(user_id, course_id):
    session = Session()
    new_enrollment = Enrollment(user_id=user_id, course_id=course_id)
    session.add(new_enrollment)
    session.commit()
