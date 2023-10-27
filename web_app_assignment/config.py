import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'kanban.db')

SECRET_KEY = 'kewfkjfnwoefo3iubfw9ebfj'

