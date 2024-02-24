import mysql.connector

# Base de datos de los usuarios, incluye sistema de autenticacion y perfiles
db_usuarios = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "registro",
}

# Base de datos para guardar los chats y manejar el historial
db_chats = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "historial_chat",
}

def get_db():
    return mysql.connector.connect(**db_usuarios)

def close_db(conn):
    conn.close()

def save_chat_message(connection, user_id, message, response):
    try:
        # Create a cursor
        cursor = connection.cursor()
        # SQL query to insert a new chat message
        sql = "INSERT INTO messages (user_id, message, response) VALUES (%s, %s, %s)"
        # Execute the query
        cursor.execute(sql, (user_id, message, response))
        # Commit changes to the database
        connection.commit()

    except mysql.connector.Error as err:
        print()

# Function to retrieve all chat messages from the database
def get_all_chat_messages(connection):
    try:
        # Create a cursor
        cursor = connection.cursor(dictionary=True)
        # SQL query to select all chat messages
        sql = "SELECT * FROM messages"
        # Execute the query
        cursor.execute(sql)
        # Fetch all chat messages
        messages = cursor.fetchall()
        return messages
    except mysql.connector.Error as err:

        return []

# Function to close the database connection
def close_connection(connection):
    try:
        # Close the connection
        connection.close()

    except mysql.connector.Error as err:
      return