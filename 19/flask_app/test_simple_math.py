# test_simple_math.py

import pytest
from simple_math import app, db, User, Expression

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_register(client):
    response = client.post('/register', data={'email': 'test@example.com', 'password': 'securepassword'})
    assert b'Registered successfully!' in response.data

def test_login(client, user_factory):
    user = user_factory()
    response = client.post('/login', data={'email': user.email, 'password': 'mypassword'})
    assert b'Dashboard' in response.data

def test_logout(client, authenticated_user):
    response = client.get('/logout', follow_redirects=True)
    assert b'Login' in response.data

def test_expression_evaluation(client, authenticated_user):
    response = client.post('/dashboard', data={'expression': '3 + 4'}, follow_redirects=True)
    assert b'3 + 4 = 7' in response.data

def test_user_history(client, authenticated_user):
    client.post('/dashboard', data={'expression': '5 * 5'})
    response = client.get('/dashboard')
    assert b'5 * 5 = 25' in response.data

@pytest.fixture
def user_factory(db):
    def create_user(email='test@example.com', password='mypassword'):
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    return create_user

@pytest.fixture
def authenticated_user(client, user_factory):
    user = user_factory()
    client.post('/login', data={'email': user.email, 'password': 'mypassword'})
    return user
