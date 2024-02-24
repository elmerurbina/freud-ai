import mysql.connector

# Base de datos de los usuarios, incluye sistema de autenticacion, perfiles y historial de mensajes
db_usuarios = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "usuarios",
}



def connect_to_database(database='usuarios'):
    try:
        connection = mysql.connector.connect(
            host=db_usuarios["host"],
            user=db_usuarios["user"],
            password=db_usuarios["password"],
            database=db_usuarios["database"]
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None


def close_connection(connection):
    if connection:
        connection.close()

def save_chat_message(connection, user_id, message, response):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO historial_chat (user_id, message, response) VALUES (%s, %s, %s)"
        data = (user_id, message, response)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print("Error saving chat message:", err)
        return False

def get_all_chat_messages(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM historial_chat"
        cursor.execute(query)
        messages = cursor.fetchall()
        cursor.close()
        return messages
    except mysql.connector.Error as err:
        print("Error retrieving chat messages:", err)
        return []

def get_chat_messages_by_user_id(connection, user_id):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM historial_chat WHERE user_id = %s"
        data = (user_id,)
        cursor.execute(query, data)
        messages = cursor.fetchall()
        cursor.close()
        return messages
    except mysql.connector.Error as err:
        print("Error retrieving chat messages by user ID:", err)
        return []


    # Base de datos del dataset
db_dataset = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "dataset",
}

def connect_database():
    try:
        connection = mysql.connector.connect(
            host=db_dataset["host"],
            user=db_dataset["user"],
            password=db_dataset["password"],
            database=db_dataset["database"]
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None

def fetch_data_from_information_table(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM information"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data
    except mysql.connector.Error as err:
        print("Error fetching data from information table:", err)
        return []




def get_db():
    return mysql.connector.connect(**db_usuarios)

def close_db(conn):
    conn.close()
