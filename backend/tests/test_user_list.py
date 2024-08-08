import unittest
from app import app, mongo

class UserListTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Clean up test users
        mongo.db.users.delete_many({})

    def test_get_users_with_filters(self):
        # Create test users
        mongo.db.users.insert_many([
            {'name': 'John', 'email': 'john@example.com', 'age': 30, 'color': 'red'},
            {'name': 'Jane', 'email': 'jane@example.com', 'age': 25, 'color': 'blue'}
        ])
        
        # Test filtering by name
        response = self.app.get('/users', query_string={'name': 'John'})
        self.assertEqual(response.status_code, 200)
        users = response.get_json()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['name'], 'John')
        
        # Test filtering by age
        response = self.app.get('/users', query_string={'age': 25})
        self.assertEqual(response.status_code, 200)
        users = response.get_json()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['age'], 25)

if __name__ == '__main__':
    unittest.main()
