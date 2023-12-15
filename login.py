from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import get_db_connection
from flask import Blueprint
app = Flask(__name__, static_url_path='/static')


# Integración de la base de datos
conn = get_db_connection()


login_blueprint = Blueprint('Login', __name__)
@app.route('/login', methods=['GET', 'POST'])
def login_account():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')



        with get_db_connection() as conn, conn.cursor() as cursor:
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email))
            user = cursor.fetchone()

            if user:
                session['user_id'] = user[0]

                # Se redirige al usuario a la página del chatbot
                return redirect(url_for('chatbot'))

            flash("Try again")

    # Se redirige al usuario a la pagina de login
    return render_template('login.html')

@app.route('/bot')
def bot():
    user_id = session.get('user_id')

    # Identifica si el usuario está autorizado
    if user_id is not None:
        return render_template('ChatBot.html')
    else:
        # Si las credenciales no son las correctas, se le regresa a la página de login
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
