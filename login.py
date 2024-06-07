from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from db import connect_to_database
from register_user import get_user_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

login_manager = LoginManager()
login_manager.init_app(app)

# Define a User class
class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    # This function is required by Flask-Login. It loads a user given the ID.
    user = User()
    user.id = user_id
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        connection = connect_to_database()
        cursor = connection.cursor()

        try:
            # Check if the email and password match the records in the database
            query = "SELECT id FROM sistema_registro WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user_id = cursor.fetchone()

            # Consume all results (even if only one expected)
            cursor.fetchall()

            if user_id:
                # Create a User object and login the user
                user = User()
                user.id = user_id[0]
                login_user(user)

                # Save user ID in session
                session['user_id'] = user_id[0]

                # Redirect to chat.html upon successful login
                return redirect(url_for('chat'))
            else:
                error = 'Credenciales incorrectas. Por favor, inténtelo de nuevo.'
                return render_template('login.html', error=error)
        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('user_id', None)  # Elimina el ID de usuario de la sesion
    return redirect(url_for('login'))

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')


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