from flask import Flask, render_template, request, redirect, url_for, flash
import jwt


from db import get_db_connection

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'your_secret_key_here'


# Conección con la base de datos
conn = get_db_connection()


class User:
    def __init__(self, id, email):
        self.id = id  # el user_id es generado en la base de datos
        self.email = email

def get_user_by_id(user_id):
    with get_db_connection() as conn, conn.cursor() as cursor:
        query = "SELECT email FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result:
            return User(user_id, result[0])
        return None

def validate_password_reset_token(token):
    with get_db_connection() as conn, conn.cursor() as cursor:
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = payload['user_id']
            query = "SELECT email FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            if result:
                user = User(user_id, result[0])
                if user is None or user.id != user_id:
                    flash('Invalid or expired token')
                    return redirect(url_for('login'))
                return user
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass  # Token validation failed

    flash('Invalid or expired token')
    return redirect('Invalid token')



@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    with get_db_connection() as conn, conn.cursor() as cursor:
        user = validate_password_reset_token(token)
        if user is None:
            return

        if request.method == 'GET':
            return render_template('reset_password.html', token=token)
        elif request.method == 'POST':
            new_password = request.form['new_password']

            # Encriptamos la nueva contrasenia


            # Se actualiza la información de la contrasenia en la base de datos
            query = "UPDATE users SET password = %s WHERE user_id = %s"
           # cursor.execute(query, (encrypted_password, user.id))
            conn.commit()

            flash('Password reset successful')

        #    return redirect(url_for('login'))  # Se redirige el usuario a la pagina de login

if __name__ == '__main__':
    app.run(debug=True)
