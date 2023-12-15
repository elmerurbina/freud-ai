from flask import Flask, render_template, request, url_for, abort, flash
from datetime import datetime, timedelta
from flask_mail import Message, Mail
import jwt
from db import get_db_connection
from flask import Blueprint


app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'your_secret_key_here'


# Configuracion del Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'elmerurbina570@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ui+5~d~=Kx'
mail = Mail(app)

# Base de datos del sistema de autenticacion
conn = get_db_connection()

class User:
    def __init__(self, id, email):
        self.id = id
        self.email = email

# Se carga la informacion del usuario de la base de datos, usando la informacion del correo
def get_user_by_email(email):
 with get_db_connection() as conn, conn.cursor() as cursor:

    query = "SELECT user_id FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    if result:
        return User(result[0], email)
    return None

# Se genera un Token, para facilitar el proceso de recuperacion de la contrasenia
def generate_password_reset_token(user):
    expires = datetime.utcnow() + timedelta(hours=24)
    token = jwt.encode({'user_id': user.id, 'expires': expires}, app.config['SECRET_KEY'], algorithm='HS256')
    return token.decode('utf-8')

# Se valida el Token generado
def validate_password_reset_token(token):
 with get_db_connection() as conn, conn.cursor() as cursor:
    try:
        payload = jwt.encode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = payload['user_id']
        expires = payload['expires']
        if datetime.utcnow() > expires:
            return None
        query = "SELECT email FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result:
            return User(user_id, result[0])
        return None
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None





password_recovery_blueprint = Blueprint('password_recovering', __name__)
@app.route('/recover', methods=['GET', 'POST'])
def password_recovery():
    if request.method == 'GET':
        return render_template('recover_account.html')
    elif request.method == 'POST':
        email = request.form['email']

        user = get_user_by_email(email)
        if user is None:
            flash('Email not found')
            return render_template('recover_account.html')

        token = generate_password_reset_token(user)

# Se le envia un correo al usuario con las instrucciones
        msg = Message('Password Reset', sender='elmerurbina570@gmail.com', recipients=[user.email])
        msg.body = 'To reset your password, please click on the following link:\n\n' + url_for('reset_password', token=token, _external=True)

        mail.send(msg)

        flash('Password reset email sent. Check your email for instructions.')
        return ("The instruction to reset your password have been sent to your email")

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = validate_password_reset_token(token)
    if user is None:
        abort(404)

    if request.method == 'GET':
        return render_template('reset_password.html', token=token)
    elif request.method == 'POST':

        flash('Password reset instructions sent to your email')


       # return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
