from flask import Flask, render_template, request
import os
from flask_wtf import CSRFProtect
from db import get_db



app = Flask(__name__)
app.config.from_pyfile('config.py')  # Load configurations from config.py

csrf = CSRFProtect(app)

@app.route('/freud')
def home():
    return render_template('index.html')

@app.route('/verExpediente')  # Corrected the route path
def verExpediente():
    return render_template('verExpediente.html')


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    # Fetch user details from the database based on the username
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT nombre, correo FROM usuarios WHERE correo = %s", (username,))
    user_data = cursor.fetchone()

    # Check if the user exists
    if user_data:
        if request.method == 'POST':
            # Handle profile update
            new_email = request.form.get('email')
            cursor.execute("UPDATE usuarios SET correo = %s WHERE nombre = %s", (new_email, user_data['nombre']))
            db.commit()

            # Handle profile picture upload
            if 'profile_picture' in request.files:
                profile_picture = request.files['profile_picture']
                if profile_picture.filename != '':
                    upload_folder = 'static/uploads'
                    if not os.path.exists(upload_folder):
                        os.makedirs(upload_folder)
                    profile_picture.save(os.path.join(upload_folder, profile_picture.filename))

                    # Update the database with the path to the uploaded profile picture
                    cursor.execute("UPDATE usuarios SET foto_perfil = %s WHERE nombre = %s", (os.path.join(upload_folder, profile_picture.filename), user_data['nombre']))
                    db.commit()

        return render_template('profile.html', username=user_data['nombre'])
    else:
        return render_template('error.html', message='User not found')



@app.route('/login_account', methods=['GET', 'POST'])
def login_account():
    return render_template('login.html')



@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    return render_template('register.html')

@app.route('/agregar_perfil')
def agregar_perfil():
    return render_template('agregar.html')



@app.route('/password_recovery')
def  password_recovery():
    return render_template('recover_account.html')



@app.route('/reset_password')
def  reset_password():
    return render_template('reset_password.html')


@app.route('/profesionales')
def  profesionales():
    return render_template('profesionales.html')


@app.route('/chat')
def chat():
    return render_template('ChatBot.html')


if __name__ == '__main__':
    app.run(debug=True)