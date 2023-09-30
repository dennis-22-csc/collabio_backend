from flask import Flask, jsonify, request, render_template, redirect, url_for, send_from_directory, current_app
from database import insert_project, insert_user, update_user_data, get_projects, get_user_info, get_other_user_info, insert_message, get_received_messages_by_user_email, get_messages_by_user_email, delete_messages, get_users
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from util import find_matching_users, send_matching_project_email, send_message_email, delete_account_email, send_new_user_email
from manage_dropbox import upload_image, download_image, update_image
import eventlet
import redis
import json
import logging
import uuid

# Create Flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode='eventlet')
redis_server = redis.StrictRedis(host='localhost', db=0)

logging.basicConfig(
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Output log messages to the console
        logging.FileHandler('logfile.log')  # Output log messages to a file
    ]
)

@app.route('/')
def home():
    return redirect("https://dennis-22-csc.github.io/collabio/")

@app.route('/create-your-profile')
def create_profile():
    return redirect("https://play.google.com/store/apps/details?id=com.denniscode.collabio")

@app.route('/view-inbox')
def view_inbox():
    return redirect("https://play.google.com/store/apps/details?id=com.denniscode.collabio")

@app.route('/view-user-profile/<user_id>')
def other_user_view(user_id):
    return redirect("https://play.google.com/store/apps/details?id=com.denniscode.collabio")

@app.route('/view-matching-project/<project_id>')
def matching_project_view(project_id):
    return redirect("https://play.google.com/store/apps/details?id=com.denniscode.collabio")

@app.route('/.well-known/assetlinks.json')
def serve_assetlinks():
    return send_from_directory('.well-known', 'assetlinks.json')

@app.route('/projects', methods=['GET'])
def retrieve_projects():
    result = get_projects()
    
    if result is None:
        return jsonify({"error": "Projects not found"})
    elif isinstance(result, str):
        return jsonify({"error": result}) 
    return jsonify({"projects": result})

@app.route('/messages', methods=['POST'])
def get_messages():
    data = request.get_json()
    email = data.get('email')
    result = get_messages_by_user_email(email)

    if isinstance(result, str):
        return jsonify({"error": result})
    return jsonify({"messages": result})

@app.route('/get-user', methods=['POST'])
def get_user():
    data = request.get_json()
    email = data.get('email')
    result = get_user_info(email)

    if isinstance(result, str):
        return jsonify({"error": result})
    else:
        dropbox_result = download_image(result['picture_uri'])
        if dropbox_result is not None:
            result["picture_bytes"] = dropbox_result
            return jsonify({"user": result})
        else:
            return jsonify({"error": dropbox_result})

@app.route('/get-other-user', methods=['POST'])
def get_other_user():
    data = request.get_json()
    user_id = data.get('user_id')
    result = get_other_user_info(user_id)

    if result is None:
        return jsonify({"error": "User record not found"})
    elif isinstance(result, str):
        return jsonify({"error": result})
    else:
        dropbox_result = download_image(result['picture_uri'])
        if dropbox_result is not None:
            result["picture_bytes"] = dropbox_result
            return jsonify({"other_user": result})
        else:
            return jsonify({"error": "dropbox {}".format(dropbox_result)})

@app.route('/del-messages', methods=['POST'])
def delete_messages_handler():
    #data = request.get_json()
    #uuids = data.get('uuids')
    #results = delete_messages(uuids)
    
    #if len(results) > 0:
        #return jsonify({'results': results})
    #else:
    return jsonify({'message': 'Messages deleted'})
    #return jsonify({'null': 'null'})
        
    
@app.route('/project', methods=['POST'])
def create_new_project():
    project_data = request.get_json()
    project_id = str(uuid.uuid4())
    project_data["project_id"] = project_id
    result = insert_project(project_data)
    if result == "Project inserted successfully.":
        project_data_json = json.dumps(project_data)
        redis_server.publish(f'new_project', project_data_json)
    return jsonify(result)

@app.route('/create-user', methods=['POST'])
def create_new_user():
    user_data = request.get_json()
    image_result = upload_image(user_data['picture_bytes'])
    if image_result != "Error uploading image":
        user_data['picture_uri'] = image_result
        result = insert_user(user_data)
        return jsonify(result)
    else:
        return jsonify(image_result)

@app.route('/message', methods=['POST'])
def insert_new_message():
    message_data = request.get_json()
    message_data["status"] = "sent"
    result = insert_message(message_data)
    if result == "Message inserted successfully.":
        message_data_json = json.dumps(message_data)
        recipient_email = message_data.get('receiver_email')
        redis_server.publish(f'new_message:{recipient_email}', message_data_json)
        socketio.start_background_task(send_message_email, message_data.get('receiver_email'), message_data.get('receiver_name'), message_data.get('sender_name'))
    return jsonify(result)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    user_data = request.get_json()
    
    if "picture_bytes" in user_data:
        result = get_user_info(user_data['email'])
        if isinstance(result, str):
            return jsonify(result)
        else:
            image_updated = update_image(user_data['picture_bytes'], result['picture_uri'])
            if image_updated:
                return jsonify("Profile updated successfully")
            else:
                return jsonify("Failed to update profile")
    result = update_user_data(user_data)
    return jsonify(result)


@app.route('/del-account', methods=['GET', 'POST'])
def delete_account():
    if request.method == 'POST':
        email = request.form['email']
        result = get_user_info(email)
        if result is not None and not isinstance(result, str):
            socketio.start_background_task(delete_account_email, email, result.get('first_name'))
        return redirect(url_for('delete_account', success='true'))
    return render_template('delete_account.html')

def is_not_numeric(variable):
    return not isinstance(variable, (int, float, complex))

@socketio.on('connect')
def on_connect():
    try:
        user_email = request.args.get('email')
        if user_email:
            redis_pubsub = redis_server.pubsub()
            message_channel = f'new_message:{user_email}'
            project_channel = 'new_project'
            redis_pubsub.subscribe([message_channel, project_channel])
            socketio.start_background_task(listen_redis_messages, redis_pubsub, user_email)
    except Exception as e:
        logging.error('Error in on_connect:', str(e))

def listen_redis_messages(redis_pubsub, user_email):
    try:
        for message in redis_pubsub.listen():
            if message['type'] == 'message' and is_not_numeric(message['data']):
                channel = message['channel'].decode('utf-8')
                data = message['data'].decode('utf-8')
                message_channel = f'new_message:{user_email}'
                project_channel = 'new_project'
                if channel == message_channel:
                    socketio.emit('new_message', data) 
                elif channel == project_channel:
                    socketio.emit('new_project', data)
                    
    except Exception as e:
        logging.error('Error in listening:', str(e))

# Main function
if __name__ == '__main__': 
    socketio.run(app, 'host:0.0.0.0', port=5000)
