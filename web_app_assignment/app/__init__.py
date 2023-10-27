from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from .models import User

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)



from app import routes
from .models import User

