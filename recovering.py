from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Message
from werkzeug.security import generate_password_hash
import os
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

# Database configuration
db_path = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db():
    return sqlite3.connect(db_path)

def close_db(conn):
    conn.close()

# Mockup password reset tokens
password_reset_tokens = {}

# Function to send password reset email
def send_password_reset_email(user):
    token = os.urandom(24).hex()
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    password_reset_tokens[user['id']] = {'token': token, 'expiration_time': expiration_time}

    reset_link = url_for('reset_password', token=token, _external=True)

    # Replace the email sending logic with your actual email sending code
    msg = Message('Password Reset Request', recipients=[user['email']])
    msg.body = f"Click the following link to reset your password: {reset_link}"
    # mail.send(msg)

# Reset Password route
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user_id = None
    for uid, reset_info in password_reset_tokens.items():
        if reset_info['token'] == token and datetime.utcnow() < reset_info['expiration_time']:
            user_id = uid
            break

    if user_id is None:
        flash('Invalid or expired token. Please request a new password reset.', 'error')
        return redirect(url_for('login'))

    # Update user's password in the database
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Passwords do not match.', 'error')
        else:
            hashed_password = generate_password_hash(new_password)
            cursor.execute("UPDATE usuarios SET contrasena = ? WHERE id = ?", (hashed_password, user_id))
            db.commit()
            flash('Password reset successful! You can now log in with your new password.', 'success')
            del password_reset_tokens[user_id]  # Remove token after successful reset
            close_db(db)
            return redirect(url_for('login'))

    close_db(db)
    return render_template('reset_password.html')

# Your other routes and code...

if __name__ == '__main__':
    app.run(debug=True)
