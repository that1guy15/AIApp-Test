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
