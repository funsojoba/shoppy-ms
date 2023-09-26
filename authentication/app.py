from flask import Flask, request, jsonify
import jwt
from decouple import config

app = Flask(__name__)

# Secret key for JWT (replace with a strong secret in production)
JWT_SECRET_KEY = config('JWT_SECRET_KEY')

# Sample user data (for demonstration purposes)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        token = jwt.encode({'username': username}, JWT_SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Authentication failed'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
