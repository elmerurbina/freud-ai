from flask import Flask, render_template, redirect, url_for
from register_user import register_user_app
from flask_dance.contrib.google import make_google_blueprint, google
from flask import request, jsonify



app = Flask(__name__)

app.config.from_pyfile('config.py')  # Cargar las configuraciones del archivo config.py
app.register_blueprint(register_user_app, url_prefix='/register')


# Google OAuth blueprint
google_bp = make_google_blueprint(

    redirect_to="login_callback"
)
app.register_blueprint(google_bp, url_prefix="/login")


# Ruta del index
@app.route('/freud')
def home():
    return render_template('index.html')


@app.route('/support')
def redApoyo():
    return render_template('redApoyo.html')

@app.route('/historial')
def historial():
    return render_template('historial.html')



# Editar perfil del profesional
@app.route('/perfil_profesional')
def edit_profile():
    return render_template('editarPerfilProfesional.html')




# Mostrar el perfil del profesional
@app.route('/perfil')
def mi_perfil():
    return render_template('perfil.html')





# Funcion para configurar las notificaciones
@app.route('/notificaciones')
def  notificaciones():
    return render_template('notificaciones.html')




# Ruta que permite el acceso al panel del psicologo y por ende a la interfaz de estos
@app.route('/verExpediente')  # Corrected the route path
def verExpediente():
    return render_template('verExpediente.html')


@app.route('/expediente')
def expediente():
    return render_template('expediente.html')


# Acceso a las funciones de inicio de sesion
@app.route('/login_account', methods=['GET', 'POST'])
def login_account():
    return render_template('login.html')

# Route for handling Google Sign-In callback
@app.route("/google_login_callback")
def login_callback():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text

    # Use resp.json() to get user information
    # Implement your logic to handle user login or registration here

    return redirect(url_for("chat"))  # Redirect to chat interface after successful login

# Route for handling Google login
@app.route("/google_login", methods=['POST'])
def google_login():
    id_token = request.form['id_token']

    # Verify the ID token with Google
    # You can use libraries like google-auth or pyjwt to verify the token
    # Example verification logic should be added here

    # If the token is valid, proceed with the login process
    # You can get user information from the ID token
    # For example, idinfo['email'], idinfo['name'], etc.
    # Implement your logic to handle the user login or registration here

    return jsonify({'status': 'success'})





# Acceso al registro del usuario
@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    return render_template('register.html')

@app.route('/agregar_perfil')
def agregar_perfil():
    return render_template('agregar.html')




# Permitir al usuario recuperar y actualizar sus credenciales
@app.route('/password_recovery')
def  password_recovery():
    return render_template('recover_account.html')




# Permite el acceso y la funcionalidad a la interfaz para actualizar credenciales
@app.route('/reset_password')
def  reset_password():
    return render_template('reset_password.html')



# Esta es la parte encargada de mostrarle al usuario todos los profesionales registrados en la pataforma
@app.route('/profesionales')
def  profesionales():
    return render_template('profesionales.html')



# Esta es la ruta que maneja la parte del chatbot
@app.route('/chat')
def chat():
    return render_template('chat.html')


# Procesa los mensajes del usuario
@app.route('/process_message', methods=['POST'])
def process_message():
    user_message = request.json.get('message', '')

    # Procesa los mensajes del usuario y genera una respuesta
    response = get_chatbot_response(user_message)

    return jsonify({'response': response})

# Muestra las respuestas del chatbot
def get_chatbot_response(user_input):
    # Estas son algunas respuestas pre-programadas a los saludos mas comunes
    if 'hola' in user_input.lower():
        return '¡Hola! ¿En qué puedo ayudarte hoy?'
    elif 'estoy ansioso' in user_input.lower():
        return 'Entiendo. ¿Puedes contarme más sobre lo que te preocupa?'
    else:
        return 'Lo siento, no entiendo. ¿Puedes reformular tu pregunta?'



if __name__ == '__main__':
    app.run(debug=True)