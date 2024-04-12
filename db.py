import mysql.connector
from mysql.connector import Error


# Configuraciones de las base de datos
db_usuarios = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "usuarios",
}

# Funcion para conectar a la base de datos de los usuarios
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

# Funcion para cerrar la conexion con la bae de datos de los usuarios
def close_connection(connection):
    if connection:
        connection.close()

# Funcion para guardar los mensajes del chatbot en la base de datos
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

# Funcion para mostrar los mensajes de la base de datos
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

# Funcion para extraer los mensajes de la base de datos haciendo uso del ID del usuario
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

# Establecer la conexion a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7>>HhNN6/fZ",
    database="usuarios"
)

# Funcion para guardar los contactos de la red de apoyo en la base de datos
def insert_contact(contact_one, contact_two, psychologist_email):
    cursor = db.cursor()
    sql = "INSERT INTO redApoyo (contact_one, contact_two, psychologist_email) VALUES (%s, %s, %s)"
    val = (contact_one, contact_two, psychologist_email)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

# Se cierra la conexion con la base de datos
def close_db_connection():
    db.close()

# Configuraciones para la base de datos de los profesionales
db_profesionales = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "profesionales",
}

# Funcion para conectarse con la base de datos de los profesionales
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

# Funcion para cerrar la conexion con la base de datos
def close_profesionales_connection(connection):
    if connection:
        connection.close()

# Funcion para guardar el perfil de los profesionales en la base de datos
# Funcion para guardar el perfil de los profesionales en la base de datos
def save_profesional(connection, form, file_path):
    try:
        cursor = connection.cursor()
        if file_path:
            cursor.execute("""
                INSERT INTO perfil (nombre, licencia, ubicacion, contacto, keywords, descripcion, photo)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (form.nombre.data, form.licencia.data, form.direccion.data, form.contacto.data, form.keywords.data, form.descripcion.data, file_path))
        else:
            cursor.execute("""
                INSERT INTO perfil (nombre, licencia, ubicacion, contacto, keywords, descripcion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (form.nombre.data, form.licencia.data, form.direccion.data, form.contacto.data, form.keywords.data, form.descripcion.data))
        connection.commit()
        cursor.close()
        return True
    except Error as e:
        print(f"Error saving professional: {e}")
        return False

def get_profesional_by_licencia(connection, licencia):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM perfil WHERE licencia = %s", (licencia,))
        profesional = cursor.fetchone()
        cursor.close()
        return profesional
    except Error as e:
        print(f"Error fetching professional by licencia: {e}")
        return None

# Funcion para obtener la informacion de la base de datos
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


# Base de datos del dataset
def fetch_data_from_information_table():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='7>>HhNN6/fZ',
            database='dataset'
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to fetch data from the information table
        query = "SELECT * FROM information"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the fetched data
        return rows

    except mysql.connector.Error as error:
        print("Error fetching data from information table:", error)
        return None
