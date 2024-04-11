"""
BTP405 – Project 02

I declare that this assignment is my own work in accordance with Seneca Academic Policy. No part of this
assignment has been copied manually or electronically from any other source (including web sites) or
distributed to other students.

Name: Ahmad Mashal 
Student ID: 149015224 
Date: 2024-04-10
"""



import http.server
import json
from urllib.parse import urlparse
import bcrypt
import jwt
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('.env')

def connect_to_mongodb():
    try:
        mongodb_uri = os.getenv('MONGODB_URI')
        db_name = os.getenv('DB_NAME')
        client = MongoClient(mongodb_uri)
        db = client[db_name]
        print("Connecting to MongoDB was successful.")
        return db
    except Exception as e:
        print(f"Failed to connect to MongoDB. Error: {e}")
        return None

db = connect_to_mongodb()

sessions = {}
user_counter = 0
reservation_counter = 0

def create_tables():
    print("Tables created successfully")

def serialize_reservation(reservation):
    serialized_reservation = {
        'id': str(reservation['_id']),
        'user_id': reservation['user_id'],
        'date': reservation['date'],
        'time': reservation['time'],
        'party_size': reservation['party_size']
    }
    return serialized_reservation

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'content-type, Authorization')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def generate_token(self, user_id):
        token = jwt.encode({'user_id': user_id}, '123', algorithm='HS256')
        return token
    
    def do_GET(self):
        token = self.headers.get('Authorization')
        if not token:
            self._set_headers(401)
            self.wfile.write(json.dumps({'message': 'No token provided'}).encode())
            return

        token = token.replace('Bearer ', '')

        user_id = sessions.get(token)
        if not user_id:
            self._set_headers(401)
            self.wfile.write(json.dumps({'message': 'Invalid token'}).encode())
            return

        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/reservations':
            try:
                reservations = list(db.reservations.find({'user_id': user_id}))
                serialized_reservations = [serialize_reservation(reservation) for reservation in reservations]
                self._set_headers(200)
                self.wfile.write(json.dumps(serialized_reservations).encode())
            except Exception as e:
                print(f"Error retrieving reservations from database: {e}")
                self._set_headers(500)
                self.wfile.write(json.dumps({'message': 'Internal server error'}).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/register':
            global user_counter
            user_counter += 1

            try:
                existing_user = db.users.find_one({'$or': [{'username': data['username']}, {'email': data['email']}]})
                if existing_user:
                    raise ValueError('Username or email already exists')

                hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

                db.users.insert_one({'user_id': user_counter, 'username': data['username'], 'email': data['email'], 'password_hash': hashed_password})
            except Exception as e:
                print(f"Error saving user data to database: {e}")

            self._set_headers(201)
            self.wfile.write(json.dumps({'message': 'User registered successfully'}).encode())

        elif path == '/login':
            try:
                user = db.users.find_one({'username': data['username']})
                if not user:
                    raise ValueError('User not found')

                if bcrypt.checkpw(data['password'].encode('utf-8'), user['password_hash']):
                    token = self.generate_token(user['user_id'])
                    sessions[token] = user['user_id']

                    self._set_headers(200)
                    self.wfile.write(json.dumps({'message': 'Login successful', 'token': token, 'user_id': user['user_id']}).encode())
                else:
                    raise ValueError('Incorrect password')
            except Exception as e:
                print(f"Error logging in: {e}")
                self._set_headers(401)
                self.wfile.write(json.dumps({'message': 'Login failed'}).encode())

        elif path == '/reservations':
            try:
                global reservation_counter
                reservation_counter += 1
                
                db.reservations.insert_one({'id': reservation_counter, 'date': data['date'], 'time': data['time'], 'party_size': data['party_size']})
            except Exception as e:
                print(f"Error saving reservation to database: {e}")

            self._set_headers(201)
            self.wfile.write(json.dumps({'message': 'Reservation made successfully'}).encode())

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        data = json.loads(put_data)

        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path.startswith('/reservations'):
            try:
                reservation_id = path.split('/')[-1]
                db.reservations.update_one({'id': int(reservation_id)}, {'$set': {'date': data['date'], 'time': data['time'], 'party_size': data['party_size']}})
            except Exception as e:
                print(f"Error updating reservation in database: {e}")

            self._set_headers(200)
            self.wfile.write(json.dumps({'message': 'Reservation updated successfully'}).encode())
    
    def do_DELETE(self):
        token = self.headers.get('Authorization')
        if not token:
            self._set_headers(401)
            self.wfile.write(json.dumps({'message': 'No token provided'}).encode())
            return

        token = token.replace('Bearer ', '')

        user_id = sessions.get(token)
        if not user_id:
            self._set_headers(401)
            self.wfile.write(json.dumps({'message': 'Invalid token'}).encode())
            return

        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path.startswith('/reservations/'):
            reservation_id = path.split('/')[-1]

            try:
                db.reservations.delete_one({'id': int(reservation_id), 'user_id': user_id})

                self._set_headers(200)
                self.wfile.write(json.dumps({'message': 'Reservation deleted successfully'}).encode())
            except Exception as e:
                print(f"Error deleting reservation from database: {e}")
                self._set_headers(500)
                self.wfile.write(json.dumps({'message': 'Internal server error'}).encode())

def run(server_class=http.server.HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
