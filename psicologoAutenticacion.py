from flask import Flask, render_template, request, redirect, url_for, flash, session
from db import add_user, get_user_by_email, verify_user
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route('/psicologoAutenticacion')
def psicologoAutenticacion():
    return render_template('psicologoAutenticacion.html')


@app.route('/ingresar', methods=['POST', 'GET'])
def ingresar():
    email = request.form['login-email']
    password = request.form['login-password']

    user = verify_user(email, password)

    if user:
        session['user_id'] = user['id']
        session['user_name'] = user['nombre']
        return redirect(url_for('dashboard'))
    else:
        flash('Correo electrónico o contraseña incorrectos', 'login_error')
        return render_template('psicologoAutenticacion.html', login_error_message='Correo electrónico o contraseña incorrectos')


@app.route('/registrar', methods=['POST', 'GET'])
def registrar():
    nombre = request.form['register-name']
    email = request.form['register-email']
    password = request.form['register-password']
    confirm_password = request.form['register-confirm-password']

    if password != confirm_password:
        flash('Las contraseñas no coinciden', 'register_error')
        return render_template('psicologoAutenticacion.html', register_error_message='Las contraseñas no coinciden')

    if add_user(nombre, email, password):
        flash('Registro exitoso, ahora puedes iniciar sesión', 'register_success')
    else:
        flash('El correo electrónico ya está registrado', 'register_error')

    return render_template('psicologoAutenticacion.html', register_error_message='El correo electrónico ya está registrado')



if __name__ == '__main__':
    app.run(debug=True)
