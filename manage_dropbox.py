import os
import dropbox
from dropbox.exceptions import ApiError, AuthError
import requests
import base64
import logging
import json
import time
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Output log messages to the console
        logging.FileHandler('logfile.log')  # Output log messages to a file
    ]
)

# Load environment variables from .env file
load_dotenv()

APP_KEY = os.getenv('DROPBOX_APP_KEY')
APP_SECRET = os.getenv('DROPBOX_APP_SECRET')
AUTHORIZATION_CODE = os.getenv('DROPBOX_AUTHORIZATION_CODE')
REFRESH_TOKEN = os.getenv('DROPBOX_REFRESH_TOKEN')

def load_token_data():
    with open('token_data.json', 'r') as file:
        return json.load(file)

def save_new_token(new_access_token):
    new_creation_time = time.time()

    token_data = {
        "access_token": new_access_token,
        "creation_time": new_creation_time,
        "expiration_duration": 14400
    }

    with open('token_data.json', 'w') as file:
        json.dump(token_data, file)

def is_token_expired(token_data):
    current_time = time.time()
    creation_time = token_data['creation_time']
    expiration_duration = token_data['expiration_duration']

    return current_time - creation_time >= expiration_duration

def get_refresh_token(app_key, app_secret, authorization_code):
    refresh_url = "https://api.dropbox.com/oauth2/token"
    refresh_data = {
        "code": authorization_code,
        "grant_type": "authorization_code",
        "client_id": app_key,
        "client_secret": app_secret
    }

    try:
        response = requests.post(refresh_url, data=refresh_data)
        response_json = response.json()
        if "refresh_token" in response_json:
            refresh_token = response_json["refresh_token"]
            return refresh_token
    except requests.exceptions.RequestException as e:
        logging.error(f"Error getting refresh token. {e}")

def request_new_access_token(refresh_token, client_id, client_secret):
    refresh_url = 'https://api.dropboxapi.com/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
    }

    try:
        response = requests.post(refresh_url, headers=headers, data=data)
        if response.status_code == 200:
            response_data = response.json()
            new_access_token = response_data['access_token']
            save_new_token(new_access_token)
        else:
            logging.error(f"Error getting access token. {response.content}")
    except ApiError as e:
         logging.error(f"Error getting access token. {e}")

def upload_image(image_bytes_string):
    timestamp = int(time.time())
    file_name = f"image_{timestamp}.jpg"
    remote_image_path = '/collabio/profile_pictures' + '/' + file_name
    
    try:
        ACCESS_TOKEN_DATA = {}
        ACCESS_TOKEN_DATA = load_token_data()
        if is_token_expired(ACCESS_TOKEN_DATA):
            request_new_access_token(REFRESH_TOKEN, APP_KEY, APP_SECRET)
            ACCESS_TOKEN_DATA = load_token_data()
        ACCESS_TOKEN = ACCESS_TOKEN_DATA['access_token']
        dbx = dropbox.Dropbox(ACCESS_TOKEN)
        image_bytes = base64.b64decode(image_bytes_string)
        upload_result = dbx.files_upload(image_bytes, remote_image_path, mode=dropbox.files.WriteMode('overwrite'))
        return upload_result.id.replace("id:", "")
    except ApiError as e:
        logging.error(f"Error uploading image. {e}")

def update_image(image_bytes_string, image_id):
    try:
        ACCESS_TOKEN_DATA = {}
        ACCESS_TOKEN_DATA = load_token_data()
        if is_token_expired(ACCESS_TOKEN_DATA):
            request_new_access_token(REFRESH_TOKEN, APP_KEY, APP_SECRET)
            ACCESS_TOKEN_DATA = load_token_data()
        ACCESS_TOKEN = ACCESS_TOKEN_DATA['access_token']

        upload_url = f"https://content.dropboxapi.com/2/files/upload"

        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Dropbox-API-Arg": f'{{"path": "id:{image_id}", "mode": "overwrite"}}',
            "Content-Type": "application/octet-stream"
        }

        image_bytes = base64.b64decode(image_bytes_string)
        response = requests.post(upload_url, headers=headers, data=image_bytes)

        if response.status_code == 200:
            return True
        else:
            logging.error("Error updating file content. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        logging.error("Error making request:", e)

def download_image(image_id):
    try:
        ACCESS_TOKEN_DATA = {}
        ACCESS_TOKEN_DATA = load_token_data()
        if is_token_expired(ACCESS_TOKEN_DATA):
            request_new_access_token(REFRESH_TOKEN, APP_KEY, APP_SECRET)
            ACCESS_TOKEN_DATA = load_token_data()
        ACCESS_TOKEN = ACCESS_TOKEN_DATA['access_token']
        
        download_url = "https://content.dropboxapi.com/2/files/download"

        download_headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Dropbox-API-Arg": f'{{"path": "id:{image_id}"}}'
        }

        response = requests.post(download_url, headers=download_headers) 
        if response.status_code == 200:
            image_bytes = response.content
            image_bytes_string = base64.b64encode(image_bytes).decode('utf-8')
            return image_bytes_string
        else:
            logging.error(f"Error downloading image. {response.content}")

    except ApiError as e:
        logging.error(f"Error downloading image. {e}")

#filename = 'file_bytes.txt'

#with open(filename, 'r') as file:
    #file_content = file.read()
    #result = upload_image(file_content)
    #print(result)
#image_url = 'https://ucarecdn.com/a59c6d79-1baf-412f-bf78-c7d7a7e31712/image14.jpg'
#response = requests.get(image_url)

#if response.status_code == 200:
    #image_bytes = response.content
    #upload = upload_image(image_bytes)
    #print(upload)
    #download = download_image(upload)
    #print(download)

#update = update_image("xxxyaa", "_N_k1dTDfY4AAAAAAAAAGg")
#print(update)
