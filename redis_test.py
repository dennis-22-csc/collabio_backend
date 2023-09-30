import socketio
from flask_socketio import SocketIO, emit
from flask import Flask
import logging
import redis
import eventlet
import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the log level (e.g., DEBUG, INFO, WARNING, ERROR)

# Create a file handler
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.DEBUG)  # Set the log level for this handler

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


# Create a Flask SocketIO app
app = Flask(__name__)
socketio = SocketIO(app)
redis_server = redis.StrictRedis(host='localhost', port=6379, db=0)


@socketio.on('connect')
def on_connect():
    try:
        logger.debug('Client connected')
        # Subscribe to the Redis channel
        redis_pubsub = redis_server.pubsub()
        redis_pubsub.subscribe('new_message')
        logger.debug("subscribed")
        for message in redis_pubsub.listen():
             if message['type'] == 'message':
                logger.debug('Received message from Redis:', message['data'].decode('utf-8'))
    except Exception as e:
        logger.error('Error in on_connect:', str(e))

@socketio.on('custom_event')
def handle_custom_event(data):
    logger.debug('Received custom_event:', data)
    redis_server.publish('new_message', json.dumps(data))
    emit('custom_response', {'me': 'you'}, broadcast=True)

def event_stream():
    pubsub = redis_server.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe('new_message')
    logger.debug("subscribed")
    for message in pubsub.listen():
        logger.debug(message['new_message'])

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    #redis_thread = eventlet.spawn(event_stream)
