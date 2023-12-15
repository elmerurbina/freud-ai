from flask import Flask, render_template

app = Flask(__name__)

@app.route('/freud')
def home():
    return render_template('index.html')

@app.route('/verExpediente')  # Corrected the route path
def verExpediente():
    return render_template('verExpediente.html')


@app.route('/register_user')  # Corrected the route path
def register_user():
    return render_template('register.html')


@app.route('/login_account')  # Corrected the route path
def login_account():
    return render_template('login.html')


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
def  chat():
    return render_template('ChatBot.html')


if __name__ == '__main__':
    app.run(debug=True)
