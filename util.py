import os
import logging
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the values from environment variables
smtp_username = os.getenv('FROM_USERNAME')
smtp_password = os.getenv('FROM_PASSWORD')
from_addr = os.getenv('FROM_AADRESS')

logging.basicConfig(
    level=logging.ERROR,  # Set the logging level to ERROR or higher
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Output log messages to the console
        logging.FileHandler('logfile.log')  # Output log messages to a file
    ]
)

def categorize_project_type(keywords):
    if 'android' in keywords:
        return 'android'
    elif 'ios' in keywords:
        return 'ios'
    elif any(tag in keywords for tag in ['web', 'website']):
        return 'web'
    else:
        return 'other'

def create_keywords(project_title, project_tags):
    title_keywords = project_title.lower().split()
    tag_keywords = [tag.lower() for tag in project_tags]
    tags_split = [tag.split() for tag in tag_keywords]
    tags_flat = [word for tag in tags_split for word in tag]

    return title_keywords + tags_flat

def find_matching_users(users, project_title, project_tags):
    keywords = create_keywords(project_title, project_tags)
    project_category = categorize_project_type(keywords)

    matching_users = []
    for user in users:
        user_tags = [tag.lower() for tag in user['tags']]
        user_tags_split = [tag.split() for tag in user_tags]
        user_tags_flat = [word for tag in user_tags_split for word in tag]

        if project_category == 'web' and ('web' in user_tags_flat or 'website' in user_tags_flat):
            matching_users.append({'name': user['first_name'], 'email': user['email']})
        elif project_category in user_tags_flat:
            matching_users.append({'name': user['first_name'], 'email': user['email']})

    return matching_users

def send_matching_project_email(receiver_email, receiver_name, project_id):
    try:
        url = 'https://collabio.denniscode.tech/view-matching-project/{}'.format(project_id)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        from_name = 'Collabio'
        
        email_body = f"Hi {receiver_name},\n\n"
        email_body += f"A project you might be interested in has just been posted!\n"
        email_body += f"Check it out using the below link:\n\n"
        email_body += url + "\n\n"
        email_body += f"Best regards,\n"
        email_body += f"The Collabio Team"

        message = MIMEText(email_body)
        message['Subject'] = 'Relevant Project'
        message['From'] = formataddr((from_name, from_addr))
        message['To'] = receiver_email

        # Send the email
        smtp_connection.sendmail(message['From'], [message['To']], message.as_string())

        # Disconnect from the server
        smtp_connection.quit()
    except smtplib.SMTPException as error:
        logging.error("Error occurred: " + str(error))

def send_new_user_email(receiver_email, receiver_name, new_user_id):
    try:
        url = 'https://collabio.denniscode.tech/view-user-profile/{}'.format(new_user_id)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        from_name = 'Collabio'
        email_body = f"Hi {receiver_name},\n\n"
        email_body += f"A new user has joined Collabio!\n"
        email_body += f"Check them out using the below link:\n\n"
        email_body += url + "\n\n"
        email_body += f"Best regards,\n"
        email_body += f"The Collabio Team"

        message = MIMEText(email_body)
        message['Subject'] = 'New User Notification'
        message['From'] = formataddr((from_name, from_addr))
        message['To'] = receiver_email

        # Send the email
        smtp_connection.sendmail(message['From'], [message['To']], message.as_string())
         # Disconnect from the server
        smtp_connection.quit()
    except smtplib.SMTPException as error:
        logging.error("Error occurred: " + str(error))

def send_message_email(receiver_email, receiver_name, sender_name):
    try:
        url = 'https://collabio.denniscode.tech/view-inbox'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        from_name = 'Collabio'

        email_body = f"Hi {receiver_name},\n\n"
        email_body += f"{sender_name} sent you a message!\n"
        email_body += f"Check it out using the below link:\n\n"
        email_body += url + "\n\n"
        email_body += f"Best regards,\n"
        email_body += f"The Collabio Team"

        message = MIMEText(email_body)
        message['Subject'] = 'Message Notification'
        message['From'] = formataddr((from_name, from_addr))
        message['To'] = receiver_email

        # Send the email
        smtp_connection.sendmail(message['From'], [message['To']], message.as_string())
        # Disconnect from the server
        smtp_connection.quit()
    except smtplib.SMTPException as error:
        logging.error("Error occurred: " + str(error))


def delete_account_email(receiver_email, receiver_name):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        from_name = 'Collabio'

        email_body = f"Hi {receiver_name},\n\n"
        email_body += f"We received a delete account request from you.\n"
        email_body += f"Please confirm by replying to this email.\n\n"
        email_body += f"Best regards,\n"
        email_body += f"The Collabio Team"
        
        message = MIMEText(email_body)
        message['Subject'] = 'Delete Account Request'
        message['From'] = formataddr((from_name, from_addr))
        message['To'] = receiver_email

        # Send the email
        smtp_connection.sendmail(message['From'], [message['To']], message.as_string())
        # Disconnect from the server
        smtp_connection.quit()
    except smtplib.SMTPException as error:
        logging.error("Error occurred: " + str(error))

if __name__ == "__main__":
    print(send_matching_project_email("dennisakpotaire@gmail.com", "Dennis", "12wed"))
    users = [{'email': 'alimatsadiat@gmail.com', 'first_name': 'Alimat', 'last_name': 'Sadiat', 'about': 'A frontend developer', 'tags': ['Web Development', 'UI Design', 'Flutter', 'UX Design', 'CSS', 'Javascript', 'HTML']}, {'email': 'dennisakpotaire@gmail.com', 'first_name': 'Dennis', 'last_name': 'Koko', 'about': 'An android engineer', 'tags': ['Android Development', 'E-commerce', 'Flutter', 'WooCommerce']}, {'email': 'kunleajayi@gmail.com', 'first_name': 'Kunle', 'last_name': 'Ajayi', 'about': 'A web designer', 'tags': ['Web Design', 'UI Design', 'Flutter', 'UX Design']}, {'email': 'olasmith@gmail.com', 'first_name': 'Ola', 'last_name': 'Smith', 'about': 'A web developer', 'tags': ['Web Development', 'E-commerce', 'Word Press', 'WooCommerce']}, {'email': 'racheloniga@gmail.com', 'first_name': 'Rachel', 'last_name': 'Oniga', 'about': 'A blockchain developer', 'tags': ['Blockchain Development', 'E-commerce', 'Web3', 'AI']}]

    project_title = "Build a Social Networking Platform"
    project_tags = ['Android Development', 'Social Networking', 'Frontend', 'Backend']

    keywords = create_keywords(project_title, project_tags)
    print(keywords)
    print(categorize_project_type(keywords))
    matching_users = find_matching_users(users, project_title, project_tags)
    print("Matching users:", matching_users)

