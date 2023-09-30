import os
import json
import cloudinary
import cloudinary.uploader
import cloudinary.exceptions
import requests
import base64
import logging
import uuid
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

APP_KEY = os.getenv('CLOUDINARY_APP_KEY')
APP_SECRET = os.getenv('CLOUDINARY_APP_SECRET')
CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
cloudinary.config(
  cloud_name = CLOUD_NAME,
  api_key = APP_KEY,
  api_secret = APP_SECRET
)


def upload_image(image_bytes_string, image_id):
    remote_image_path = '/collabio/profile_pictures/'

    try:
        image_bytes = base64.b64decode(image_bytes_string)
        uploaded_image = cloudinary.uploader.upload(
        image_bytes,
        folder=remote_image_path,
        public_id=image_id
    )

        print("Uploaded Image URL:", uploaded_image["secure_url"])
    except cloudinary.exceptions.Error as e:
        logging.error(f"Error uploading image. {e}")


def download_image(image_id):
    try:
        #cloudinary_url = f"https://res.cloudinary.com/dor92kmrn/image/upload/{image_id}.jpg"
        cloudinary_url = f"https://res.cloudinary.com/dor92kmrn/image/upload/v1693248179/collabio/profile_pictures/image_1693248179.jpg/{image_id}.jpg"

        response = requests.get(cloudinary_url)
        if response.status_code == 200:
            image_bytes = response.content
            image_bytes_string = base64.b64encode(image_bytes).decode('utf-8')
            return image_bytes_string
        else:
            logging.error(f"Error downloading image. {response.content}")
    except cloudinary.exceptions.Error as e:
        logging.error(f"Error downloading image. {e}")

def delete_image(image_id):
    deletion_response = cloudinary.uploader.destroy(
        image_id,
        invalidate=True
    )

    print(deletion_response)
#image_url = 'https://ucarecdn.com/a59c6d79-1baf-412f-bf78-c7d7a7e31712/image14.jpg'
#response = requests.get(image_url)

#if response.status_code == 200:
    #image_bytes = response.content
    #image_bytes_string = base64.b64encode(image_bytes).decode('utf-8')
    #image_id = str(uuid.uuid4())
    #upload = upload_image(image_bytes_string, image_id)
    #print(upload)

print(download_image('99f6e7bb-b895-493e-b5ae-07ac0ee88d34'))

#print(delete_image('99f6e7bb-b895-493e-b5ae-07ac0ee88d34'))
