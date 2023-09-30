import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.event
def message(data):
    print('I received a message!')

@sio.on('custom_response')
def on_custom_response(data):
    print('Received custom_response:', data)

if __name__ == '__main__':
    
    sio.connect('http://collabio.denniscode.tech')

    sio.emit('custom_event', {'key': 'value'})

    sio.wait()
