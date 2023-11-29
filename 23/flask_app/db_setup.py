# db_setup.py

from simple_math import db, User, Expression

# Create the database and the database tables
db.create_all()

# If you want to add a default user for testing, you can do so here
user = User(email='test@example.com')
user.set_password('testpassword')  # You should use a secure password in a real app

# Add the user to the session and commit it to the database
db.session.add(user)
db.session.commit()

print("Database and tables created.")
