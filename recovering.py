from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import re
from db import *

from itsdangerous import URLSafeSerializer

app = Flask(__name__)

SECRET_KEY = 'your_secret_key'
app.config.from_object('config')

mail = Mail(app)

@app.route('/reset_password/<token>')
def reset_password(token):
    # Verify the token (assuming token is the same as the email)
    email = token  # For simplicity, token is the email in this example
    if not is_valid_email(email):
        return render_template('invalid_token.html')

    # Check if the user exists in the database
    query = f"SELECT * FROM sistema_registro WHERE email = '{email}'"
    result = db.execute(query)
    user = result.fetchone()
    if not user:
        flash('User does not exist', 'error')  # Flash an error message
        return render_template('error.html') # Redirect to login page or any other page

    # Render the reset password form if the user exists
    return render_template('reset_password.html', token=token)

def is_valid_email(email):
    # Regular expression pattern to validate email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def generate_unique_token(email):
    # Create a URLSafeSerializer instance with the secret key
    serializer = URLSafeSerializer(SECRET_KEY)
    # Generate a unique token based on the email
    return serializer.dumps(email)

def send_password_reset_email(email, reset_link):
    msg = Message('Password Reset', recipients=[email])
    msg.body = f"Ir al siguiente link para recuperar sus credenciales: {reset_link}"
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
