import firebase_admin
from firebase_admin import credentials, auth, exceptions, messaging

# Initialize the Admin SDK with your service account credentials
cred = credentials.Certificate('denniscode-24c88-firebase-adminsdk-h98h0-9082289f45.json')
firebase_admin.initialize_app(cred)

def send_verification_link(email):
    try:
        link = auth.generate_email_verification_link(email)
        print('Successfully generated verification link:', link)
    except exceptions.FirebaseError as e:
        print('Error:', e)

def delete_user(email):
    try:
        user = auth.get_user_by_email(email)
        auth.delete_user(user.uid)
        print('Successfully deleted user')
    except exceptions.FirebaseError as e:
        print('Error:', e)

def message_subscribers(title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        topic="news"
    )

    try:
        response = messaging.send(message)
        print("Message sent successfully")
    except exceptions.FirebaseError as e:
        print('Error:', e)

def message_device(registration_token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
              title=title,
              body=body,
        ),
        token=registration_token,
    )

    try:
        response = messaging.send(message)
        print('Successfully sent message.')
    except exceptions.FirebaseError as e:
        print('Error:', e)


TITLE = "Test"
BODY = "Hello, how is it going with the app?"
TOKEN = "f4OoeQLZQIyn302KBXEnP-:APA91bHRH7HB-bU2nrK83NKhznSsZ2MBz7rlPo3UhMbj2_S8naF1BnoGdXqQN4PSlpEOxMKzuEV2Bvrs-DmjCYlufu5WQuy2ekGfPLwboI0RORacZRcX1O33x99kOQe_-7Z-UdbaHu"

#message_subscribers(TITLE, BODY)
#message_device(TOKEN, TITLE, BODY)
