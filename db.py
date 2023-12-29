import mysql.connector

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
