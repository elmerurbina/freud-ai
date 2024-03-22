from flask import Flask, render_template, redirect, url_for
#from register_user import register_user
from flask_dance.contrib.google import make_google_blueprint, google
from flask import request, jsonify
from db import insert_contact, db_connection
from profileUser import get_user_data
from agregar import agregar_perfil, profesionales



app = Flask(__name__)

app.config.from_pyfile('config.py')  # Cargar las configuraciones del archivo config.py

# Google OAuth blueprint
google_bp = make_google_blueprint(

    redirect_to="login_callback"
)
app.register_blueprint(google_bp, url_prefix="/login")


#app.add_url_rule('/register_user', 'register_user', register_user, methods=['POST'])


app.add_url_rule('/agregar_perfil', 'agregar_perfil', agregar_perfil, methods=['GET', 'POST'])
app.add_url_rule('/profesionales', 'profesionales', profesionales)



# Ruta del index
@app.route('/freud')
def home():
    return render_template('index.html')


@app.route('/register')
def register_user():
    return render_template('register.html')


def check_access_code(access_code):
    connection = db_connection()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM ejecutivos WHERE codigo = %s"
    cursor.execute(query, (access_code,))
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count > 0

@app.route('/check-access-code/<access_code>')
def check_access_code_route(access_code):
    exists = check_access_code(access_code)
    return jsonify({'exists': exists})




@app.route("/profile")
def profile():
    # Fetch user data
    user_data = get_user_data()
    if user_data:
        return render_template("profile.html", user_data=user_data)
    else:
        return "Lo lamentamos, no pudimos encontrar su usario. Por favor intentalo mas tarde!"



@app.route("/support", methods=["GET", "POST"])
def redApoyo():
    if request.method == "POST":
        # Get form data
        contact_one = request.form.get("contact-one")
        contact_two = request.form.get("contact-two")
        psychologist_email = request.form.get("psychologist-email")

        # Check if country code is included
        if '+' not in contact_one or '+' not in contact_two:
            error_message = "Por favor, asegúrese de incluir el código de país en los números de contacto."
            return render_template("redApoyo.html", error=error_message)

        # Insert data into database
        insert_contact(contact_one, contact_two, psychologist_email)

        # Return success response
        success_message = "Información guardada con éxito."
        return render_template("redApoyo.html", success=success_message)

    # Render the redApoyo.html template for GET requests
    return render_template("redApoyo.html")


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





# Permitir al usuario recuperar y actualizar sus credenciales
@app.route('/password_recovery')
def  password_recovery():
    return render_template('recover_account.html')




# Permite el acceso y la funcionalidad a la interfaz para actualizar credenciales
@app.route('/reset_password')
def  reset_password():
    return render_template('reset_password.html')



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
    # Saludos comunes
    if any(word in user_input.lower() for word in ['hola', 'saludos', 'buenos días', 'buenas tardes', 'buenas noches']):
        return '¡Hola! ¿Cómo te encuentras?'

    elif any(word in user_input.lower() for word in ['bien', 'bien gracias a Dios', 'bien gracias a dios']):
        return 'Me alegro que estes bien, ¿De que tema te gustaria hablar hoy?'

    elif any(word in user_input.lower() for word in ['mal', 'horrible', 'decepcionado']):
        return 'Comprendo que te sientas mal, estoy aqui para escucharte y ayudarte, cuentame ¿por que te sientes mal?'


    # Expresar emociones
    elif any(word in user_input.lower() for word in ['estoy ansioso', 'ansioso', 'me siento ansioso']):
        return 'Entiendo. La ansiedad es una experiencia común. ¿Te gustaría hablar sobre lo que la está desencadenando?'


    elif 'estres' in user_input.lower():
        return 'Algunas causas del estres son fracaso, universidad, mucho trabajo. ¿En los ultimos dias has tenido alguno de estos problemas?'


    elif any(word in user_input.lower() for word in ['me siento solo', 'no tengo a nadie a mi lado']):
        return 'La soledad no siempre es mala, muchas veces nos ayuda a reflexionar y a encontrarnos a nosotros mismos. ¿Dime de que tema deseas hablar?'

    elif any(word in user_input.lower() for word in ['me siento triste', 'estoy deprimido']):
        return 'Lamento escuchar que te sientes así. ¿Puedes compartir más sobre lo que ha estado sucediendo?'

    # Manejo del estres
    elif any(word in user_input.lower() for word in ['cómo manejar el estrés', 'consejos para reducir el estrés']):
        return 'El manejo del estrés es importante. Algunas estrategias incluyen la práctica de la respiración profunda y el autocuidado. ¿Te gustaría más información?'

    # Prevenir el suicidio
    elif any(word in user_input.lower() for word in ['pensamientos suicidas', 'necesito ayuda urgente']):
        return 'Lo siento mucho que estés pasando por esto. Es crucial buscar ayuda de emergencia. Por favor, comunícate con una línea de prevención de suicidios o busca ayuda profesional de inmediato.'

    elif any(word in user_input.lower() for word in ['me quiero suicidar', 'mi vida es una mierda', 'me quiero morir']):
        return 'La vida es algo muy valioso, entiendo que te sientas mal pero yo estoy aqui para ayudarte. cuentame mas sobre lo que estas pasando y te brindare todo mi apoyo'


    # Tecnicas para lidiar con el estres
    elif any(word in user_input.lower() for word in ['cómo lidiar con el estrés', 'técnicas de afrontamiento']):
        return 'Hay diversas técnicas de afrontamiento, como la meditación, el ejercicio y la búsqueda de apoyo social. ¿Te gustaría más sugerencias personalizadas?'

    # Explorar emociones
    elif any(word in user_input.lower() for word in ['explorar emociones', 'autoconocimiento']):
        return 'Explorar tus emociones puede ser un viaje enriquecedor. ¿Te gustaría discutir más sobre tus sentimientos y experiencias?'

    # Gratitud y positivismo
    elif any(word in user_input.lower() for word in ['agradecimiento', 'cómo encontrar la positividad']):
        return 'Practicar la gratitud puede tener un impacto positivo. ¿Hay algo específico por lo que te sientas agradecido hoy?'

    # Respondiendo preguntas frecuentes
    elif any(word in user_input.lower() for word in ['cómo', 'qué', 'cuándo', 'dónde']):
        return 'Esa es una pregunta interesante. ¿Puedes proporcionar más detalles?'

    else:
        return 'Lo siento, no entiendo completamente. ¿Puedes proporcionar más información o formular tu pregunta de otra manera?'


if __name__ == '__main__':
    app.run(debug=True)