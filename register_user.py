from flask import Flask, render_template, request, redirect, url_for
from db import get_connection
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

        # Check if a file is uploaded
        if 'foto' in request.files:
            photo = request.files['foto']
            if photo.filename != '':
                # Save the photo to a temporary location
                photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
                photo.save(photo_path)
        else:
            photo_path = None

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        # Insert user data into the database
        query = "INSERT INTO sistema_registro (full_name, username, email, password, date_of_birth, photo) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (full_name, username, email, password, date_of_birth, photo_path)
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
    app.config['UPLOAD_FOLDER'] = 'uploads'  # Define the folder where uploaded files will be saved
    app.run(debug=True)
