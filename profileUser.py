from db import get_connection

def get_user_data():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    select_query = "SELECT full_name, username FROM sistema_registro"
    cursor.execute(select_query, ())
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()
    return user_data
