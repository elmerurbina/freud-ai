import mysql.connector
from _datetime import datetime




# Base de datos del sistema de autenticacion
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "registro",
}

def get_db():
    return mysql.connector.connect(**db_config)

def close_db(conn):
    conn.close()



#Base de datos del dataset
b_config = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "dataset",
}

def connect_to_database():
    try:
        conn = mysql.connector.connect(**b_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

def fetch_data_from_information_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM information")
        table_data = cursor.fetchall()
        cursor.close()
        return table_data
    except mysql.connector.Error as err:
        print(f"Error fetching data from the 'information' table: {err}")
        return []


# base de datos para guardar los chats del usuario
chats_db_config = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "chats",
}

def get_chats_db_connection():
    try:
        conn = mysql.connector.connect(**chats_db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to the 'chats' database: {err}")
        return None

def close_chats_db_connection(conn):
    conn.close()

def insert_chat_message(user_id, message_text):
        conn = get_chats_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                #encrypted_user_input = encrypt_message(user_input, encryption_key)
               # encrypted_bot_response = encrypt_message(bot_response, encryption_key)


                query = "INSERT INTO mensajes (user_id, message_text, timestamp) VALUES (%s, %s, %s)"
                cursor.execute(query, (user_id, message_text, timestamp))
                conn.commit()
                cursor.close()
                close_chats_db_connection(conn)
                return True  # Si el mensaje se guarda correctamente
            except mysql.connector.Error as err:
                print(f"Error inserting chat message: {err}")
                close_chats_db_connection(conn)
        return False  # Si el mensaje no puede guardar


    # Funcion para mostrar los chats al usuario autorizado
def get_user_chat_history(user_id):
        conn = get_chats_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM mensajes WHERE user_id = %s ORDER BY timestamp"
                cursor.execute(query, (user_id,))
                chat_history = cursor.fetchall()
                cursor.close()
                close_chats_db_connection(conn)
                return chat_history
            except mysql.connector.Error as err:
                print(f"Error fetching chat history: {err}")
                close_chats_db_connection(conn)
        return []



# Base de datos del registro
registro_db_config = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "profesionales",
}

def get_registro_db_connection():
    return mysql.connector.connect(**registro_db_config)

def close_registro_db_connection(conn):
    conn.close()

def insert_profile_data(nombre, licencia, ubicacion, contacto, descripcion, file_path):
    conn = get_registro_db_connection()
    if conn:
        try:
            cursor = conn.cursor()


            query = "INSERT INTO registro (nombre, licencia, ubicacion, contacto, descripcion, profile_picture) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (nombre, licencia, ubicacion, contacto, descripcion, file_path)
            cursor.execute(query, values)

            conn.commit()
            cursor.close()
            close_registro_db_connection(conn)

            print(f"Profile data for {nombre} Datos guardados exitosamente")
            return True
        except mysql.connector.Error as err:
            print(f"Ocurrio un error al intentar guardar los datos {err}")
    return False
