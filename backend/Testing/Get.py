import unittest
import http.client
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.conn = http.client.HTTPConnection("localhost", 8000)

    def tearDown(self):
        self.conn.close()

    # TESTING to get all reservations for an account
    def test_get_reservations(self):
        # Perform login to obtain a valid token
        user_data = {
            'username': 'newuser',  # Replace with valid username
            'password': 'password123'  # Replace with valid password
        }
        headers = {'Content-Type': 'application/json'}
        self.conn.request("POST", "/login", body=json.dumps(user_data), headers=headers)

        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)

        data = json.loads(response.read())
        self.assertEqual(data['message'], 'Login successful')
        self.assertIsNotNone(data['token'])

        valid_token = data['token']

        # Use the obtained token to retrieve reservations
        headers = {'Authorization': f'Bearer {valid_token}'}
        self.conn.request("GET", "/reservations", headers=headers)

        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)

        data = json.loads(response.read())
        self.assertIsInstance(data, list)
        print(data)


if __name__ == '__main__':
    unittest.main()
