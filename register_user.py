from flask import Flask, render_template, request, redirect, url_for
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

if __name__ == '__main__':
    app.run(debug=True)
