from kafka import KafkaProducer
from flask import Flask, jsonify, request

app = Flask(__name__)

# Kafka producer setup
producer = KafkaProducer(bootstrap_servers='kafka:9092')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')
    
    # Send a notification message to Kafka
    producer.send('notification_topic', key=str(user_id).encode(), value=str(message).encode())
    
    return jsonify({'message': 'Notification sent'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
