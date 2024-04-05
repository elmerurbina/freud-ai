import mysql.connector
from mysql.connector import Error


# Database configurations
db_usuarios = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "usuarios",
}

# Function to connect to the database
def connect_to_database(database='usuarios'):
    try:
        connection = mysql.connector.connect(
            host=db_usuarios["host"],
            user=db_usuarios["user"],
            password=db_usuarios["password"],
            database=database
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None

# Function to close connection with the database
def close_connection(connection):
    if connection:
        connection.close()

# Function to save chat messages in the database
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

# Function to retrieve all chat messages from the database
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

# Function to retrieve chat messages by user ID from the database
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

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7>>HhNN6/fZ",
    database="usuarios"
)

# Function to insert contact into redApoyo table
def insert_contact(contact_one, contact_two, psychologist_email):
    cursor = db.cursor()
    sql = "INSERT INTO redApoyo (contact_one, contact_two, psychologist_email) VALUES (%s, %s, %s)"
    val = (contact_one, contact_two, psychologist_email)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

# Close MySQL database connection
def close_db_connection():
    db.close()

# Database configurations for profesionales database
db_profesionales = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "profesionales",
}

# Function to connect to the profesionales database
def connect_to_profesionales_database():
    try:
        connection = mysql.connector.connect(
            host=db_profesionales["host"],
            user=db_profesionales["user"],
            password=db_profesionales["password"],
            database=db_profesionales["database"]
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None

# Function to close connection with the profesionales database
def close_profesionales_connection(connection):
    if connection:
        connection.close()

def save_profesional(connection, form, file_path):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO perfil (nombre, licencia, ubicacion, contacto, keywords, descripcion, photo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (form.nombre.data, form.licencia.data, form.direccion.data, form.contacto.data, form.keywords.data, form.descripcion.data, file_path))
        connection.commit()
        cursor.close()
        return True
    except Error as e:
        print(f"Error saving professional: {e}")
        return False

# Function to fetch all professional data from the database
def get_profesionales_data(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM perfil")
        professionals = cursor.fetchall()
        cursor.close()
        return professionals
    except Error as e:
        print(f"Error fetching professionals data: {e}")
        return []