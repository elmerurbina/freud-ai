# Archivo de la aplicacion | Maneja todas las rutas del sistema

# Importacion de las rutas y librerias
from register_user import register, userProfile
from flask import request, jsonify
from db import *
from logout import logout
from psicologoAutenticacion import ingresar, registrar, psicologoAutenticacion
from profesionalPlans import profesionalPlans
from panelPsicologo import panelPsicologo
from psicologoManagement import *
from chat import *
from login import *
from googleSinIn import *
from redApoyo import *
from frases import show_notification, send_notification, random_phrase
from recovering import *
from patientRecord import expediente, add_prescription, add_diagnostic_test, add_medical_history, validate_passkey
from aseguradora import aseguradora, check_code_validity, codigoRegistro


# Inicializar la applicacion
app = Flask(__name__)


# Cargar las configuraciones del archivo config.py
app.config.from_pyfile('config.py')


# Agregar la clave secreta generada al hazar
app.config['SECRET_KEY'] = SECRET_KEY


# Manejo del error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_code=404), 404


# Manejo de errores 500 (Error interno del servidor)
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_code=500), 500

# Planes de los psicologos
app.add_url_rule('/profesionalPlans', 'profesionalPlans', profesionalPlans)

app.add_url_rule('/ingresar', 'ingresar', ingresar, methods=['POST', 'GET'])
app.add_url_rule('/registrar', 'registrar', registrar, methods=['POST', 'GET'])
app.add_url_rule('/psicologoAutenticacion', 'psicologoAutenticacion', psicologoAutenticacion)


# Agrego la logica del modulo y las funciones del archivo register_user.py
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST']) # Registra el perfil
app.add_url_rule('/userProfile', 'userProfile', userProfile)  # Maneja el perfil de los usuarios


# Ruta del archivo expediente.py el cual maneja el acceso a los expedientes de los pacientes
app.add_url_rule('/expediente', 'expediente', expediente, methods=['GET', 'POST'])
app.add_url_rule('/add_medical_history', 'add_medical_history', add_medical_history)
app.add_url_rule('/add_prescription', 'add_prescription', add_prescription)
app.add_url_rule('/add_diagnostic_test', 'add_diagnostic_test', add_diagnostic_test)
app.add_url_rule('/validate_passkey', 'validate_passkey', validate_passkey, methods=['POST'])


app.add_url_rule('/aseguradora', 'aseguradora', aseguradora, methods=['GET', 'POST'])
app.add_url_rule('/check_code_validity', 'check_code_validity', check_code_validity, methods=['POST'])
app.add_url_rule('/codigoRegistro', 'codigoRegistro', codigoRegistro, methods=['GET', 'POST'])


app.add_url_rule('/panelPsicologo', 'panelPsicologo', panelPsicologo)


# Rutas del archivo chat.py el cual maneja la logica del chatbot
app.add_url_rule('/chat', 'chat', chat)
#app.add_url_rule('/message_history', 'message_history', message_history)
app.add_url_rule('/process_message', 'process_message', process_message, methods=['POST'])


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
app.add_url_rule('/get_chatbot_response', 'get_chatbot_response', get_chatbot_response, methods=[ 'POST'])
app.add_url_rule('/historial', 'historial', historial)


# Se agregan las funciones del archivo agregar.py
app.add_url_rule('/agregar_perfil', 'agregar_perfil', agregar_perfil, methods=['GET', 'POST'])
app.add_url_rule('/profesionales', 'profesionales', profesionales)
app.add_url_rule('/check_profile', 'check_profile', check_profile, methods=['POST'])
app.add_url_rule('/delete_profile/<int:profile_id>', 'delete_profile', delete_profile, methods=['POST'])
app.add_url_rule('/edit_profile', 'edit_profile', edit_profile, methods=['GET', 'POST'])


# Se agregan las funciones del archivo login.py
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
# Maneja los inicio de sesion
login_manager = LoginManager()
login_manager.init_app(app)

# Registra la funcion de cargar el usuario en la sesion
login_manager.user_loader(load_user)


# Ruta del archivo logout.py para cerrar sesion
app.add_url_rule('/logout', 'logout', logout)


# Funciones y rutas del archivo googleSingIn.py para inicio de sesion con Google
app.add_url_rule('/google-signin', view_func=google_auth)
app.add_url_rule('/google-auth-callback', view_func=google_auth_callback)
app.add_url_rule('/login/callback', view_func=login_callback)


# Funciones del archivo redApoyo.py, brinda soporte a los pacientes en riesgos de suicidio
app.add_url_rule('/redApoyo', 'redApoyo', redApoyo)
app.add_url_rule('/guardar_red', 'guardar_red', guardar_red, methods=['POST'])
app.add_url_rule('/success', 'success', success)
app.add_url_rule('/red_de_apoyo', 'red_de_apoyo', red_de_apoyo)


# Funciones del para el envio de notificaciones con frases de motivacion, archivo notificaciones.py
app.add_url_rule('/random_phrase', 'random_phrase', random_phrase)
app.add_url_rule('/show_notification', 'show_notification', show_notification)
app.add_url_rule('/send_notification', 'send_notification', send_notification)


# Manejo de recuperacion de cuenta, archivo recover.py
app.config.from_object('config')
mail = Mail(app)


# Funciones y rutas del archivo reset_password.py para el cambio de credenciales
app.add_url_rule('/reset_password', 'reset_password', reset_password)
app.add_url_rule('/is_valid_email', 'is_valid_email', is_valid_email)
app.add_url_rule('/generate_unique_token', 'generate_unique_token', generate_unique_token)
app.add_url_rule('/send_password_reset_email', 'send_password_reset_email', send_password_reset_email)



# Ruta del index
@app.route('/freud')
def home():
    return render_template('index.html')


# Momentaneamente muestra una estructura basica de los planes de suscripcion
@app.route('/subscripcionesUsuario')
def subscripcionesUsuario():
    return render_template('suscripcionesUsuario.html')


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


# Funcion para configurar las notificaciones
@app.route('/notificaciones')
def  notificaciones():
    return render_template('notificaciones.html')



if __name__ == '__main__':
    app.run(debug=True)