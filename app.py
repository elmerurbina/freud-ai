from register_user import register, userProfile
from flask import request, jsonify
from db import *
from agregar import agregar_perfil, profesionales
from chat import get_chatbot_response, save_chat_to_database, chat
from login import *
from googleSinIn import *
from redApoyo import *
from custom import *
from frases import show_notification, send_notification, random_phrase
from recovering import *




app = Flask(__name__)

app.config.from_pyfile('config.py')  # Cargar las configuraciones del archivo config.py

# Manejo del error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_code=404), 404

# Manejo de errores 500 (Error interno del servidor)
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_code=500), 500

# Agrego la logica del modulo y las funciones del archivo register_user
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/userProfile', 'userProfile', userProfile)

app.add_url_rule('/chat', 'chat', chat)

# Se agregan las funciones del archivo agregar.py
app.add_url_rule('/agregar_perfil', 'agregar_perfil', agregar_perfil, methods=['GET', 'POST'])
app.add_url_rule('/profesionales', 'profesionales', profesionales)

# Se agregan las funciones del archivo login.py
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])

# Funciones y rutas del archivo googleSingIn.py
app.add_url_rule('/google-signin', view_func=google_auth)
app.add_url_rule('/google-auth-callback', view_func=google_auth_callback)
app.add_url_rule('/login/callback', view_func=login_callback)

# Funciones del archivo redApoyo.py
app.add_url_rule('/redApoyo', 'redApoyo', redApoyo)
app.add_url_rule('/guardar_red', 'guardar_red', guardar_red, methods=['POST'])
app.add_url_rule('/success', 'success', success)
app.add_url_rule('/red_de_apoyo', 'red_de_apoyo', red_de_apoyo)

# URLs del custom file, que contiene la logica del proyecto Rasa
app.add_url_rule('/greeting', 'greeting', greeting)
app.add_url_rule('/sad', 'sad', sad)
app.add_url_rule('/anxiety_state', 'anxiety_state', anxiety_state)
app.add_url_rule('/happy', 'happy', happy)
app.add_url_rule('/stress', 'stress', stress)
app.add_url_rule('/anxiety', 'anxiety', anxiety)
app.add_url_rule('/depression', 'depression', depression)
app.add_url_rule('/trauma', 'trauma', trauma)
app.add_url_rule('/addiction', 'addiction', addiction)
app.add_url_rule('/insomnia', 'insomnia', insomnia)
app.add_url_rule('/narcolepsy', 'narcolepsy', narcolepsy)
app.add_url_rule('/fobias', 'fobias', fobias)
app.add_url_rule('/bulimia', 'bulimia', bulimia)
app.add_url_rule('/chatbot_response', 'chatbot_response', chatbot_response, methods=['POST'])

# Funciones del para el envio de notificaciones con frases de motivacion
app.add_url_rule('/random_phrase', 'random_phrase', random_phrase)
app.add_url_rule('/show_notification', 'show_notification', show_notification)
app.add_url_rule('/send_notification', 'send_notification', send_notification)


# Funciones para manejar la recuperacion de cuenta
app.config.from_object('config')

mail = Mail(app)

app.add_url_rule('/reset_password/<token>', 'reset_password', reset_password)
app.add_url_rule('/is_valid_email', 'is_valid_email', is_valid_email)
app.add_url_rule('/generate_unique_token', 'generate_unique_token', generate_unique_token)
app.add_url_rule('/send_password_reset_email', 'send_password_reset_email', send_password_reset_email)




# Ruta del index
@app.route('/freud')
def home():
    return render_template('index.html')

@app.route('/subscripcionesUsuario')
def subscripcionesUsuario():
    return render_template('suscripcionesUsuario.html')


# Clase para procesar los mensajes
def process_message():
    user_message = request.json.get('message', '')
    response = get_chatbot_response(user_message)
    save_chat_to_database(user_message, response)
    return jsonify({'response': response})

# Rutas de las funciones del chatbot
app.add_url_rule('/chat', 'chat', chat)
app.add_url_rule('/process_message', 'process_message', process_message, methods=['POST'])



# Funcion para conprobar si existe el codigo del ejecutivo en la base de datos
def check_access_code(access_code):
    connection = connect_to_profesionales_database()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM ejecutivos WHERE codigo = %s"
    cursor.execute(query, (access_code,))
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count > 0

# Si el codigo ingresado esta en la base de datos, se le da el acceso para agregar un nuevo perfil
@app.route('/check-access-code/<access_code>')
def check_access_code_route(access_code):
    exists = check_access_code(access_code)
    return jsonify({'exists': exists})


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



if __name__ == '__main__':
    app.run(debug=True)