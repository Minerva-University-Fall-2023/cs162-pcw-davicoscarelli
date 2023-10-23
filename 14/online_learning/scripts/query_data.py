from sqlalchemy.orm import sessionmaker
from models.base import engine, Session
from models.user import User
from models.course import Course
from models.enrollment import Enrollment

Session = sessionmaker(bind=engine)

def get_courses_by_user_name(name):
    session = Session()
    return session.query(Course).join(Enrollment).join(User).filter(User.name == name).all()
