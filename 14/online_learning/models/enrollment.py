from sqlalchemy import Column, Integer, ForeignKey
from .base import Base

from .user import User
from .course import Course
from sqlalchemy.orm import relationship

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    user = relationship(User)
    course = relationship(Course)
