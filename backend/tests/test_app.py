import pytest
from app import app as flask_app
from flask_pymongo import MongoClient
import json


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, similar to setUp
    mongo = MongoClient('mongodb://localhost:27017/testDatabase')

    yield
    # Code that will run after your test, similar to tearDown
    mongo.db.users.delete_many({})


def test_create_user(client):
    # Arrange
    user = {
        'name': 'Test User',
        'email': 'testuser@example.com',
        'age': 30,
        'color': 'red'
    }
    # Act
    response = client.post('/users', data=json.dumps(user), content_type='application/json')

    # Assert
    assert response.status_code == 200
    assert b'Test User' in response.data


def test_get_users(client):
    # Arrange
    user = {
        'name': 'Test User',
        'email': 'testuser@example.com',
        'age': 30,
        'color': 'red'
    }
    client.post('/users', data=json.dumps(user), content_type='application/json')

    # Act
    response = client.get('/users')

    # Assert
    assert response.status_code == 200
    assert b'Test User' in response.data


def test_get_users_with_filter(client):
    # Arrange
    user1 = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'age': 25,
        'color': 'blue'
    }
    user2 = {
        'name': 'Jane Doe',
        'email': 'janedoe@example.com',
        'age': 28,
        'color': 'green'
    }
    client.post('/users', data=json.dumps(user1), content_type='application/json')
    client.post('/users', data=json.dumps(user2), content_type='application/json')

    # Act
    response = client.get('/users', query_string={'name': 'John Doe'})

    # Assert
    assert response.status_code == 200
    users = json.loads(response.data)
    assert len(users) == 1
    assert users[0]['name'] == 'John Doe'
