from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import connect_to_database, check_email
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'path_to_upload_folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to handle user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle form data
        full_name = request.form['nombre']
        username = request.form['user']
        email = request.form['email']
        password = request.form['password']
        date_of_birth = request.form['date']

        if check_email(email):
            flash('Este correo ya existe en la base de datos, por favor inicia sesión', 'error')
            return redirect(url_for('login'))

        # Handle file upload
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                filename = secure_filename(photo.filename)
                photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                photo.save(photo_path)
            else:
                photo_path = None
        else:
            photo_path = None

        # Save user data to the database, including the photo path
        # Connect to the database
        connection = connect_to_database()
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
        return redirect(url_for('login'))

    return render_template('register.html')


# Function to retrieve user data from the database
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
    user_id = session.get('id')

    if user_id:
        # Retrieve user data from the database using the user ID
        user_data = get_user_data(user_id)
        if user_data:
            # Extract user information
            username = user_data[0]
            full_name = user_data[1]
            photo_path = user_data[2]

            # Set a default value for photo_path if it's None
            photo_path = photo_path or ''

            return render_template('perfilUsuario.html', username=username, full_name=full_name, photo_path=photo_path)
        else:
            return "User not found"
    else:
        return "No se encontro el ID del usuario"
if __name__ == '__main__':
    app.run(debug=True)
