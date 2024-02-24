from flask import Flask, render_template
from register_user import register_user_app
from flask import request, jsonify



app = Flask(__name__)

app.config.from_pyfile('config.py')  # Cargar las configuraciones del archivo config.py
app.register_blueprint(register_user_app, url_prefix='/register')

# Ruta del index
@app.route('/freud')
def home():
    return render_template('index.html')




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





# Acceso a las funciones de inicio de sesion
@app.route('/login_account', methods=['GET', 'POST'])
def login_account():
    return render_template('login.html')




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