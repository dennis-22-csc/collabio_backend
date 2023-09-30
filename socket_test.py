import socketio
import requests 
from datetime import datetime, timedelta

# Generate timestamp and interval
now = datetime.now()
interval = timedelta(minutes=60)


socketio_url = 'http://collabio.denniscode.tech'
user_email = 'denniskoko@gmail.com'
sio = socketio.Client()
socketio_url_with_query = f'{socketio_url}?email={user_email}'

def send_new_message(message):
    url = f"{socketio_url}/message"
    response = requests.post(url, json=message)
    return response.json()

def create_new_project(project):
    url = f"{socketio_url}/project"
    response = requests.post(url, json=project)
    return response.json()

@sio.event
def connect():
    print("Connected to Socket.IO server")

@sio.event
def disconnect():
    print("Disconnected from Socket.IO server")

@sio.on('new_message')
def on_new_message(data):
    print("Received new message:", data)

@sio.on('new_project')
def on_new_project(data):
    print("Received new project:", data)

if __name__ == "__main__":
    sio.connect(socketio_url_with_query)

    message = {
    "sender_name": "Kunle",
    "sender_email": "kunleajayi@gmail.com",
    "receiver_name": "Rachel",
    "receiver_email": "racheloniga@gmail.com",
    "message": "Hi Rachel, I'm good.",
    "timestamp": "2023-07-18 12:35:20"
    }

    project = {
    'title': 'Build an e-commerce website',
    'timestamp': (now - interval * 3).strftime('%Y-%m-%d %H:%M:%S'),
    'description': '''
      I am looking for a web developer to collaborate with me to build an e-commerce website using Shopify or WooCommerce.
      - The website will have a modern and responsive design.
      - It will include features such as product listings, shopping cart, and secure payment integration.

      The project will include the following tasks:
      - Building the user interface
      - Developing the front-end and back-end functionality
      - Integrating the website with a payment gateway
      - Testing the website and ensuring a smooth user experience

      The target audience for the website is customers who want to purchase products online.

      If you are interested in this project, please send me your portfolio and a brief description of your experience with e-commerce website development.
      ''',
    'tags': ['Web Development', 'E-commerce', 'Shopify', 'WooCommerce'],
    "poster_name": "Dennis",
    'poster_email': 'denniskoko@gmail.com'
  }
    message_response = send_new_message(message)
    print("Message response:", message_response)

    project_response = create_new_project(project)
    print("Project response:", project_response)

    sio.wait()
    #sio.disconnect()