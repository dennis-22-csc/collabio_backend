import os
from dotenv import load_dotenv
import mysql.connector
import uuid
from user_list import users_data
from project_list import projects_data
from message_list import messages_data
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get the values from environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

cursor = None
connection = None

def initialize_sql():
    global cursor
    global connection

    # Connect to MySQL
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()

def format_timestamp(timestamp):
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def create_db():
    try:
        initialize_sql()
        # Create the database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS collabio"
        cursor.execute(create_db_query)
        cursor.close()
        connection.close()
        return "Database created successfully."

    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def delete_database():
    try:
        initialize_sql()
        # Delete the database if it exists
        delete_db_query = "DROP DATABASE IF EXISTS collabio"
        cursor.execute(delete_db_query)
        cursor.close()
        connection.close()
        return "Database deleted successfully."

    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def create_tables():
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Create users table
        create_users_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            email VARCHAR(255) PRIMARY KEY,   
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            about TEXT NOT NULL,
            tags VARCHAR(255) NOT NULL,
            firebase_token VARCHAR(255),
            picture_uri VARCHAR(255) NOT NULL,
            firebase_id VARCHAR(255) NOT NULL
        )
        '''
        # Create projects table
        create_projects_table_query = '''
        CREATE TABLE IF NOT EXISTS projects (
            project_id CHAR(36) PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            timestamp DATETIME NOT NULL,
            description TEXT NOT NULL,
            tags VARCHAR(255) NOT NULL,
            poster_name VARCHAR(255) NOT NULL,
            poster_email VARCHAR(255) NOT NULL,
            FOREIGN KEY (poster_email) REFERENCES users(email)
        )
        '''
        # Create messages table
        create_messages_table_query = '''
        CREATE TABLE IF NOT EXISTS messages (
        message_id CHAR(36) PRIMARY KEY,
        sender_name VARCHAR(255) NOT NULL,
        sender_email VARCHAR(255) NOT NULL,
        receiver_name VARCHAR(255) NOT NULL,
        receiver_email VARCHAR(255) NOT NULL,
        message VARCHAR(255) NOT NULL,
        timestamp VARCHAR(255) NOT NULL,
        status VARCHAR(255) NOT NULL,
        FOREIGN KEY (sender_email) REFERENCES users(email),
        FOREIGN KEY (receiver_email) REFERENCES users(email)
        )
        '''

        cursor.execute(create_users_table_query)
        cursor.execute(create_projects_table_query)
        cursor.execute(create_messages_table_query)
        cursor.close()
        connection.close()
        return "Tables created successfully."

    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def delete_project_table():
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Delete project table if it exists
        delete_table_query = "DROP TABLE IF EXISTS projects"
        cursor.execute(delete_table_query)
        cursor.close()
        connection.close()
        return "Projects table deleted successfully."

    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def delete_user_table():
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Delete user table if it exists
        delete_table_query = "DROP TABLE IF EXISTS users"
        cursor.execute(delete_table_query)
        cursor.close()
        connection.close()
        return "Users table deleted successfully."

    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def delete_message_table():
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Delete messages table if it exists
        delete_table_query = "DROP TABLE IF EXISTS messages"
        cursor.execute(delete_table_query)
        cursor.close()
        connection.close()
        return "Messages table deleted successfully."

    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)


def insert_project(project):
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Insert the project data
        insert_query = '''
        INSERT INTO projects (project_id, title, timestamp, description, tags, poster_name, poster_email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            project["project_id"],
            project["title"],
            project["timestamp"],
            project["description"],
            ','.join(project["tags"]),
            project["poster_name"],
            project["poster_email"]
        )
        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return "Project inserted successfully."
    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

    
def insert_projects(projects):
    for project in projects:
        print(insert_project(project))    
    
def get_projects():
    projects = []
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Retrieve all projects
        select_query = '''
        SELECT p.project_id, p.title, p.timestamp, p.description, p.tags, p.poster_name, p.poster_email,  u.about
        FROM projects AS p
        INNER JOIN users AS u ON p.poster_email = u.email
        '''
        cursor.execute(select_query)
        results = cursor.fetchall()
        
        for row in results:
            project = {
                'project_id': row[0],
                'title': row[1],
                'timestamp': format_timestamp(row[2]),
                'description': row[3],
                'tags': row[4].split(','),
                'poster_name': row[5],
                'poster_email': row[6],
                'poster_about': row[7]
            }
            projects.append(project)

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
         return "Error occurred: " + str(error)
    return projects

def insert_user(user):
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Insert the user data
        insert_query = '''
        INSERT INTO users (email, first_name, last_name, about, tags, picture_uri, firebase_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          first_name = VALUES(first_name),
          last_name = VALUES(last_name),
          about = VALUES(about),
          tags = VALUES(tags),
          picture_uri = VALUES(picture_uri),
          firebase_id = VALUES(firebase_id)
        '''
        values = (
            user["email"],
            user["first_name"],
            user["last_name"],
            user["about"],
            ','.join(user["tags"]),
            user["picture_uri"],
            user["user_id"],
        )
        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return "User inserted successfully."
    except mysql.connector.Error as error:
            return "Error occurred: " + str(error)

        
def insert_users(users):
    for user in users:
        print(insert_user(user))

def get_user_info(email):
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Fetch user data
        select_query = '''
        SELECT first_name, last_name, about, tags, picture_uri, firebase_id FROM users
        WHERE email = %s
        '''
        cursor.execute(select_query, (email,))
        result = cursor.fetchone()
        if result is None:
            return "No user is found"
        user_info = {
            'first_name': result[0],
            'last_name': result[1],
            'about': result[2],
            'tags': result[3].split(','),
            'picture_uri': result[4],
            'firebase_id': result[5],
            'email': email,
        }
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)
    return user_info

def get_other_user_info(user_id):
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Fetch user data
        select_query = '''
        SELECT email, first_name, last_name, about, tags, picture_uri FROM users
        WHERE firebase_id = %s
        '''
        cursor.execute(select_query, (user_id,))
        result = cursor.fetchone()
        if result is None:
            return "No user is found"
        user_info = {
            'email': result[0],
            'first_name': result[1],
            'last_name': result[2],
            'about': result[3],
            'tags': result[4].split(','),
            'picture_uri': result[5],
        }
        cursor.close()
        connection.close()

        if not user_info:
            return None
    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)
    return user_info

def get_users():
    try:
        initialize_sql()
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        users = []

        for row in cursor.fetchall():
            user = {
                "email": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "about": row[3],
                "tags": row[4].split(','),
                "firebase_token": row[5],
                "picture_uri": row[6],
                "firebase_id": row[7],
            }
            users.append(user)

        cursor.close()
        connection.close()
        return users
    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def delete_user_by_email(email):
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Delete the user by email
        delete_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_query, (email,))
        connection.commit()

        cursor.close()
        connection.close()
        return "User deleted successfully."
    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def insert_message(message):
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Insert the message
        insert_query = '''
        INSERT INTO messages (message_id, sender_name, sender_email, receiver_name, receiver_email, message, timestamp, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (
            message['message_id'],
            message["sender_name"],
            message["sender_email"],
            message["receiver_name"],
            message["receiver_email"],
            message["message"],
            message["timestamp"],
            message["status"]
        )
        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return "Message inserted successfully."
    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def insert_messages(messages):
        for message in messages:
            print(insert_message(message))
        
def get_messages_by_user_email(email):
    messages = []
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        select_query = f'''
        SELECT 
            message_id,
            sender_name,
            sender_email,
            receiver_name,
            receiver_email,
            message,
            timestamp,
            status
        FROM messages
        WHERE '{email}' IN (sender_email, receiver_email)
        '''
        cursor.execute(select_query)
        results = cursor.fetchall()

        for row in results:
            message = {
                'message_id': row[0],
                'sender_name': row[1],
                'sender_email': row[2],
                'receiver_name': row[3],
                'receiver_email': row[4],
                'message': row[5],
                'timestamp': row[6],
                'status': row[7]
            }
            messages.append(message)
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        # Handle the error if needed
        return "Error occurred: " + str(error)

    return messages

def get_received_messages_by_user_email(email):
    messages = []
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        select_query = f'''
        SELECT 
            message_id,
            sender_name,
            sender_email,
            receiver_name,
            receiver_email,
            message,
            timestamp,
            status
        FROM messages
        WHERE receiver_email = '{email}'
        '''
        cursor.execute(select_query)
        results = cursor.fetchall()

        for row in results:
            message = {
                'message_id': row[0],
                'sender_name': row[1],
                'sender_email': row[2],
                'receiver_name': row[3],
                'receiver_email': row[4],
                'message': row[5],
                'timestamp': row[6],
                'status': row[7]
            }
            messages.append(message)
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        # Handle the error if needed
        return "Error occurred: " + str(error)

    return messages

def delete_message_by_uuid(message_uuid):
    try:
        initialize_sql()
        # Use the database
        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        # Delete the message with the given UUID
        delete_query = '''
        DELETE FROM messages WHERE message_id = %s
        '''
        values = (str(message_uuid),)
        cursor.execute(delete_query, values)
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        connection.close()

        return message_uuid 
    
    except mysql.connector.Error as error:
        return "Error occurred: " + str(error)

def delete_messages(uuids):
    results = {}
    for uuid in uuids:
        result = delete_message_by_uuid(uuid)
        if result != uuid:
            results[uuid] = result
    return results

def update_user_data(user):
    try:
        
        initialize_sql()

        use_db_query = "USE collabio"
        cursor.execute(use_db_query)

        if "first_name" in user:
            column = "first_name"
            data = user["first_name"]
            email = user["email"]

            query = f"UPDATE users SET {column} = %s WHERE email = %s"
            values = (data, email)

            cursor.execute(query, values)
        elif "last_name" in user:
            column = "last_name"
            data = user["last_name"]
            email = user["email"]

            query = f"UPDATE users SET {column} = %s WHERE email = %s"
            values = (data, email)

            cursor.execute(query, values)
        elif "about" in user:
            column = "about"
            data = user["about"]
            email = user["email"]

            query = f"UPDATE users SET {column} = %s WHERE email = %s"
            values = (data, email)

            cursor.execute(query, values)
        elif "tags" in user:
            column = "tags"
            data = ','.join(user["tags"])
            email = user["email"]

            query = f"UPDATE users SET {column} = %s WHERE email = %s"
            values = (data, email)

            cursor.execute(query, values)
        elif "firebase_token" in user:
            column = "firebase_token"
            data = user["firebase_token"]
            email = user["email"]

            query = f"UPDATE users SET {column} = %s WHERE email = %s"
            values = (data, email)

            cursor.execute(query, values)
        elif "picture_uri" in user:
            column = "picture_uri"
            data = user["picture_uri"]
            email = user["email"]

            query = f"UPDATE users SET {column} = %s WHERE email = %s"
            values = (data, email)

            cursor.execute(query, values)
        else:
            return "Invalid entry"

        connection.commit()
        cursor.close()
        connection.close()

        return "Profile updated successfully"

    except mysql.connector.Error as e:
        return "Error occurred while updating profile" + str(e)

# Main function
def main():
    #print(create_db())
    #print(create_tables())
    #insert_users(users_data)
    #insert_projects(projects_data)
    #insert_messages(messages_data)
    #print(update_user_data({"email": "denniskoko@gmail.com", "firebase_token": ""}))
    #print(get_projects())
    #print(get_messages_by_user_email("dennisthebusinessguru@gmail.com"))
    #print(get_user_info("dennisthebusinessguru@gmail.com"))
    #print(get_users())
    #print(delete_project_table())
    #print(delete_message_table())
    #print(delete_user_table())
    #print(delete_database())
    #print(delete_user_by_email("dennisthebusinessguru@gmail.com"))
    #print(delete_user_by_email("dennisakpotaire@gmail.com"))
    #connection.close())
    print("Connection closed successfully")

if __name__ == "__main__":
    main()
