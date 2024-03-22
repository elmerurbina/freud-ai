from flask import render_template, redirect, url_for, request, Flask
from db import connect_to_database, close_connection


app = Flask(__name__)

@app.route('/register_user', methods=['POST'])
def register_user():
    # Extract user data from the form
    full_name = request.form.get('full_name')
    username = request.form.get('user')
    email = request.form.get('email')
    birthdate = request.form.get('date')
    password = request.form.get('password')

    try:
        # Connect to the usuarios database
        connection = connect_to_database()

        # Insert user data into the 'sistema_registro' table
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO sistema_registro (full_name, username, email, birthdate, password_hash) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (full_name, username, email, birthdate, password))
            connection.commit()
            cursor.close()
            close_connection(connection)

            # Redirect to the chat route upon successful registration
            return redirect(url_for('chat'))
        else:
            return render_template('registration_failed.html')

    except Exception as e:
        # Handle registration failure
        print(e)
        return render_template('registration_failed.html')