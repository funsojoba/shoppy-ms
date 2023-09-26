from flask import Flask, jsonify
from kafka import KafkaConsumer

app = Flask(__name__)

# Kafka consumer setup
consumer = KafkaConsumer('notification_topic',
                         bootstrap_servers='kafka:9092',
                         auto_offset_reset='earliest',
                         group_id='cart_service')

notifications = {}

@app.route('/cart/<user_id>')
def get_cart(user_id):
    if user_id in notifications:
        return jsonify({'cart': notifications[user_id]})
    else:
        return jsonify({'cart': []})

# Listen for notification messages from Kafka
for message in consumer:
    user_id = int(message.key)
    notification = message.value.decode()
    
    if user_id not in notifications:
        notifications[user_id] = []
    
    notifications[user_id].append(notification)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
