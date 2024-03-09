from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from db import get_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Your existing code for fetching user by email from the database
def get_user_by_email(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (email,))
    user = cursor.fetchone()
    return user

# Handle Google Sign-In callback
@app.route('/google_login_callback', methods=['POST'])
def google_login_callback():
    # Implement Google Sign-In callback logic here
    # This route will handle the response from the Google Sign-In button click
    # You should verify the ID token with Google and perform necessary actions
    # For example, retrieve user information and create a session for the user
    # Once authenticated, redirect the user to the desired page
    # Example logic:
    # id_token = request.form['id_token']
    # Verify the ID token with Google
    # Authenticate the user and set session
    # Redirect to chat page or any other desired page
    return redirect(url_for('chat'))  # Example redirection to chat page

# Your existing login route for regular login
@app.route('/login_account', methods=['GET', 'POST'])
def login_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = get_user_by_email(email)
        if user and check_password_hash(user['contrasena'], password):
            # Login successful, set session
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            return redirect(url_for('chat'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
