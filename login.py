from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from db import get_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

def get_user_by_email(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (email,))
    user = cursor.fetchone()
    return user

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
