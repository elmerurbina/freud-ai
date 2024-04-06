from flask import Flask, render_template, request, redirect, url_for, session
from db import connect_to_database
import os

app = Flask(__name__)

# Function to handle user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['nombre']
        username = request.form['user']
        email = request.form['email']
        password = request.form['password']
        date_of_birth = request.form['date']

        # Server-side validation to ensure all fields are filled
        if not all([full_name, username, email, password, date_of_birth]):
            return render_template('register.html', error_message='All fields are required.')

        # Connect to the database
        connection = connect_to_database()
        cursor = connection.cursor()

        # Insert user data into the database
        query = "INSERT INTO sistema_registro (full_name, username, email, password, date_of_birth) VALUES (%s, %s, %s, %s, %s)"
        values = (full_name, username, email, password, date_of_birth)
        cursor.execute(query, values)
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Redirect to chat.html upon successful registration
        return redirect(url_for('chat'))

    return render_template('register.html')

# Function to render chat.html
@app.route('/chat')
def chat():
    return render_template('chat.html')

def get_user_data(user_id):
    # Connect to the database
    connection = connect_to_database()
    cursor = connection.cursor()

    # Retrieve user data from the database
    query = "SELECT username, full_name, photo FROM sistema_registro WHERE id = %s"
    cursor.execute(query, (user_id,))
    user_data = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return user_data

# Route to display user profile
@app.route('/userProfile')
def userProfile():
    # Retrieve the user ID from the session
    user_id = session.get('user_id')

    if user_id:
        # Retrieve user data from the database using the user ID
        user_data = get_user_data(user_id)
        if user_data:
            # Extract user information
            username = user_data[0]
            full_name = user_data[1]
            photo_path = user_data[2]  # Assuming photo is stored as a file path in the database

            return render_template('perfilUsuario.html', username=username, full_name=full_name, photo_path=photo_path)
        else:
            return "User not found"
    else:
        return "No se encontro el ID del usuario"
if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
