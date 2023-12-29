from flask import Flask, render_template, redirect, url_for, request, flash
from register_user import register_logic
from flask_wtf import CSRFProtect



app = Flask(__name__)
app.config.from_pyfile('config.py')  # Load configurations from config.py

csrf = CSRFProtect(app)

@app.route('/freud')
def home():
    return render_template('index.html')

@app.route('/verExpediente')  # Corrected the route path
def verExpediente():
    return render_template('verExpediente.html')




@app.route('/login_account')
def login_account():
    return render_template('login.html')



@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        affiliation = request.form['affiliation']
        role = request.form['role']
        pais = request.form['pais']
        departamento = request.form['departamento']
        municipio = request.form['municipio']

        result = register_logic(name, email, password, repeat_password, affiliation, role, pais, departamento, municipio)

        if result.get('success'):
            flash('Registration successful!', 'success')
            return redirect(url_for('chat'))  # Redirect to the chat route upon successful registration
        else:
            flash(result.get('error'), 'error')

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


@app.route('/profesionals')
def  profesionals():
    return render_template('profesionales.html')


@app.route('/chat')
def chat():
    return render_template('ChatBot.html')


if __name__ == '__main__':
    app.run(debug=True)
