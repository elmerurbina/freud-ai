from flask import Blueprint, render_template, redirect, url_for, request
import mysql.connector
register_user_app = Blueprint('register_user_app', __name__)

# Your database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "7>>HhNN6/fZ",
    "database": "registro",
}

@register_user_app.route('/register', methods=['POST'])
def register_user():
    # Extract user data from the form
    full_name = request.form.get('full_name')
    username = request.form.get('user')
    email = request.form.get('email')
    birthdate = request.form.get('date')
    password = request.form.get('password')

    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert user data into the 'users' table
        insert_query = "INSERT INTO users (full_name, username, email, birthdate, password_hash) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (full_name, username, email, birthdate, password))
        connection.commit()

        # Close the database connection
        cursor.close()
        connection.close()

        # Redirect to the chat route upon successful registration
        return redirect(url_for('chat'))

    except Exception as e:
        # Handle registration failure (e.g., duplicate username or email)
        print(e)
        return render_template('registration_failed.html')
