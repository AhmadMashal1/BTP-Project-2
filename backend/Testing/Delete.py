import unittest
import http.client
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.conn = http.client.HTTPConnection("localhost", 8000)
        self.valid_token = self.obtain_valid_token()

    def tearDown(self):
        self.conn.close()

    def obtain_valid_token(self):
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

        return data['token']

    # TESTING to delete a reservation
    def test_delete_reservation(self):
        # Replace '6616d03e6b6baae1f731b040' with the actual reservation ID
        reservation_id = '6616d03e6b6baae1f731b040'
        
        headers = {'Authorization': f'Bearer {self.valid_token}'}
        self.conn.request("DELETE", f"/reservations/{reservation_id}", headers=headers)

        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)

        data = json.loads(response.read())
        self.assertEqual(data, {'message': 'Reservation deleted successfully'})
        print('Reservation deleted')


if __name__ == '__main__':
    unittest.main()
