import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash


# Configuracion de la base de datos de los usuarios
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


def check_email(email):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM sistema_registro WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            cursor.close()
            close_connection(connection)
            return user
        else:
            return None
    except mysql.connector.Error as err:
        print("Error fetching user by email:", err)
        return None


# Funcion para guardar los mensajes del chatbot en la base de datos
def save_chat_message(connection, user_id, message, response):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO historial_chat (id, message, response) VALUES (%s, %s, %s)"
        data = (user_id, message, response)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print("Error saving chat message:", err)
        return False

def check_username_exists(username):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT id FROM sistema_registro WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            close_connection(connection)
            return result is not None
        except mysql.connector.Error as err:
            print("Error checking username:", err)
            close_connection(connection)
            return False
    else:
        return False  # Connection to database failed



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
        query = "SELECT * FROM historial_chat WHERE id = %s"
        data = (user_id,)
        cursor.execute(query, data)
        messages = cursor.fetchall()
        cursor.close()
        return messages
    except mysql.connector.Error as err:
        print("Error retrieving chat messages by user ID:", err)
        return []


# Funcion para guardar los mensajes del usuario
def save_chat_to_database(user_id, user_message, response):
    try:
        connection = connect_to_database(database='usuarios')
        if connection:
            save_chat_message(connection, user_id=user_id, message=user_message, response=response)
            close_connection(connection)
    except Exception as e:
        print("Error saving chat message:", e)


# Establecer una nueva conexion a la base de datos de os usuarios
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7>>HhNN6/fZ",
    database="usuarios"
)

def check_passkey(passkey):
    try:
        connection = connect_to_database()
        if connection.is_connected():
            with connection.cursor(dictionary=True) as cursor:
                query = "SELECT clave FROM passkey WHERE clave = %s"
                cursor.execute(query, (passkey,))
                result = cursor.fetchone()
                return result is not None
    except Error as e:
        print(f"Error while connecting to database: {e}")
        return False
    finally:
        if connection.is_connected():
            connection.close()


# Function to insert contacts of the support network into the database
def insert_contact(full_name_one, country_code_one, number_one, full_name_two, country_code_two, number_two, psychologist_name, psychologist_contact=None):
    cursor = db.cursor()
    if psychologist_contact:
        sql = "INSERT INTO redApoyo (full_name_one, country_code_one, number_one, full_name_two, country_code_two, number_two, psychologist_name, psychologist_contact) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (full_name_one, country_code_one, number_one, full_name_two, country_code_two, number_two, psychologist_name, psychologist_contact)
    else:
        sql = "INSERT INTO redApoyo (full_name_one, country_code_one, number_one, full_name_two, country_code_two, number_two, psychologist_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (full_name_one, country_code_one, number_one, full_name_two, country_code_two, number_two, psychologist_name)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()



# Se cierra la conexion con la base de datos
def close_db_connection():
    db.close()


# Configuracion de la base de datos de los profesionales
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


# Funcion para cerrar la conexion con la base de datos, profesionales
def close_profesionales_connection(connection):
    if connection:
        connection.close()



import mysql.connector


def get_patient_info_by_username(username):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM sistema_registro WHERE username = %s"
            cursor.execute(query, (username,))
            patient_info = cursor.fetchone()
            cursor.close()
            close_connection(connection)
            return patient_info
        except mysql.connector.Error as err:
            print("Error fetching patient info:", err)
            close_connection(connection)
            return None
    else:
        return None

def check_username(username):
    connection = connect_to_database('usuarios')
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT id FROM sistema_registro WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            close_connection(connection)
            if result:
                return True  # Username exists
            else:
                return False  # Username does not exist
        except mysql.connector.Error as err:
            print("Error checking username:", err)
            close_connection(connection)
            return False
    else:
        return False  # Connection to database failed


# Obtener la informacion del paciente de la base de datos
def get_patient_info_by_user_id(user_id):
    connection = connect_to_database('usuarios')
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM sistema_registro WHERE id = %s"
            cursor.execute(query, (user_id,))
            patient_info = cursor.fetchone()
            cursor.close()
            close_connection(connection)
            return patient_info
        except mysql.connector.Error as err:
            print("Error fetching patient info:", err)
            close_connection(connection)
            return None
    else:
        return None

def save_medical_history_entry(user_id, fecha, descripcion):
    connection = connect_to_database('sistema_registro')
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO expediente (user_id, fecha, descripcion) VALUES (%s, %s, %s)"
            data = (user_id, fecha, descripcion)
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            close_connection(connection)
            return True
        except mysql.connector.Error as err:
            print("Error saving medical history entry:", err)
            close_connection(connection)
            return False
    else:
        return False

def save_prescription(user_id, fecha, medicamento):
    connection = connect_to_database('sistema_registro')
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO recetas (user_id, fecha, medicamento) VALUES (%s, %s, %s)"
            data = (user_id, fecha, medicamento)
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            close_connection(connection)
            return True
        except mysql.connector.Error as err:
            print("Error saving prescription entry:", err)
            close_connection(connection)
            return False
    else:
        return False

def save_diagnostic_test(user_id, fecha, prueba, resultado):
    connection = connect_to_database('sistema_registro')
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO pruebas_diagnosticas (user_id, fecha, prueba, resultado) VALUES (%s, %s, %s, %s)"
            data = (user_id, fecha, prueba, resultado)
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            close_connection(connection)
            return True
        except mysql.connector.Error as err:
            print("Error saving diagnostic test entry:", err)
            close_connection(connection)
            return False
    else:
        return False


# Function to generate a password hash
def generate_password(password):
    return generate_password_hash(password)

# Function to check if a password matches its hash
def check_password(password, password_hash):
    return check_password_hash(password_hash, password)


def add_user(nombre, email, password):
    hashed_password = generate_password_hash(password, method='sha256')
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO autenticacion (nombre, email, password) VALUES (%s, %s, %s)',
                           (nombre, email, hashed_password))
            connection.commit()
            cursor.close()
            close_connection(connection)
            return True
        except mysql.connector.Error as err:
            print("Error adding user:", err)
            close_connection(connection)
            return False

# Funcion para obtener un usuario por correo electronico
def get_user_by_email(email):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM autenticacion WHERE email = %s', (email,))
            user = cursor.fetchone()
            cursor.close()
            close_connection(connection)
            return user
        except mysql.connector.Error as err:
            print("Error fetching user by email:", err)
            close_connection(connection)
            return None

# Funcion para verificar las credenciales del usuario
def verify_user(email, password):
    user = get_user_by_email(email)
    if user and check_password_hash(user['password'], password):
        return user
    return None


# Funcion para guardar el perfil de los profesionales en la base de datos
def save_profesional(connection, form, file_path):
    try:
        cursor = connection.cursor()
        if file_path: # Si existe una foto de perfil
            cursor.execute("""
                INSERT INTO perfil (nombre, licencia, ubicacion, contacto, keywords, descripcion, photo)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (form.nombre.data, form.licencia.data, form.direccion.data, form.contacto.data, form.keywords.data, form.descripcion.data, file_path))
        else: # Si no hay foto de perfil
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


# Revisar si la licencia proporcionada existe en la base de datos
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


# Funcion para eliminar perfil del psicologo
def delete_professional(connection, profile_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM perfil WHERE id = %s", (profile_id,))
        connection.commit()
        cursor.close()
        return True
    except Error as e:
        print(f"Error deleting professional: {e}")
        return False


# Funcion para obtener la informacion del perfil del psicologo de la base de datos
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


# Funcion para actualizar perfil del psicologo
def update_professional(connection, profile_id, nombre, ubicacion, contacto, licencia, estudios_academicos, keywords, descripcion, foto_data):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE perfil 
            SET nombre = %s, ubicacion = %s, contacto = %s, licencia = %s, estudios_academicos = %s, keywords = %s, descripcion = %s, photo = %s
            WHERE id = %s
        """, (nombre, ubicacion, contacto, licencia, estudios_academicos, keywords, descripcion, foto_data, profile_id))
        connection.commit()
        cursor.close()
        return True
    except Error as e:
        print(f"Error updating professional: {e}")
        return False


# Base de datos del dataset
def fetch_data_from_information_table():
    try:
        # Establecer la coneccion con la base de datos
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='7>>HhNN6/fZ',
            database='dataset'
        )



        cursor = connection.cursor()

        # Buscar datos en la table informacion
        query = "SELECT * FROM information"


        cursor.execute(query)

        # Traer todas las columnas de la tabla informacion
        rows = cursor.fetchall()

        # Cerrar la conexion
        cursor.close()
        connection.close()


       # Mostrar la informacion obtenida
        return rows

    except mysql.connector.Error as error:
        print("Error fetching data from information table:", error)
        return None



# Configuracion de la base de datos de la aseguradora
aseguradora = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "aseguradora",
}

# Funcion para conectar a la base de datos de la aseguradora
def connect(database='aseguradora'):
    try:
        connection = mysql.connector.connect(
            host=aseguradora["host"],
            user=aseguradora["user"],
            password=aseguradora["password"],
            database=database
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None


# Funcion para cerrar la conexion con la base de datos
def close(connection):
    if connection:
        connection.close()


def valid_code(codigo):
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT codigo_ejecutivo FROM codigo_ejecutivo WHERE codigo_ejecutivo = %s"
            cursor.execute(query, (codigo,))
            result = cursor.fetchone()
            cursor.close()
            close(connection)
            return result is not None
        except mysql.connector.Error as err:
            print("Error checking codigo ejecutivo:", err)
            close(connection)
            return False
    else:
        return False
