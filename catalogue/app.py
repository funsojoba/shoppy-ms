from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Sample catalog data
catalog_data = [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 5.99},
    {"id": 3, "name": "Product C", "price": 15.99},
]

AUTH_SERVICE_URL = 'http://authentication:5000/login'  # Use the service name as the hostname

@app.route('/products')
def get_products():
    # Authenticate the request
    auth_data = {'username': 'user1', 'password': 'password1'}  # Replace with user input or token
    response = requests.post(AUTH_SERVICE_URL, json=auth_data)
    
    if response.status_code == 200:
        # Authentication successful, return catalog data
        return jsonify(catalog_data)
    else:
        return jsonify({'error': 'Authentication failed'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
