from flask import Flask, render_template, redirect, url_for
from register_user import register
from flask_dance.contrib.google import make_google_blueprint, google
from flask import request, jsonify
from db import insert_contact, db_connection
from profileUser import get_user_data
from agregar import agregar_perfil, profesionales
from chat import get_chatbot_response, save_chat_to_database, chat
from login import *
from googleSinIn import *




app = Flask(__name__)

app.config.from_pyfile('config.py')  # Cargar las configuraciones del archivo config.py

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_code=404), 404

# Manejo de errores 500 (Error interno del servidor)
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_code=500), 500

# Google OAuth blueprint
google_bp = make_google_blueprint(

    redirect_to="login_callback"
)
app.register_blueprint(google_bp, url_prefix="/login")


app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/chat', 'chat', chat)


app.add_url_rule('/agregar_perfil', 'agregar_perfil', agregar_perfil, methods=['GET', 'POST'])
app.add_url_rule('/profesionales', 'profesionales', profesionales)


app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])

# Add routes for Google sign-in
app.add_url_rule('/google-signin', view_func=google_auth)
app.add_url_rule('/google-auth-callback', view_func=google_auth_callback)
app.add_url_rule('/login/callback', view_func=login_callback)


# Ruta del index
@app.route('/freud')
def home():
    return render_template('index.html')



def process_message():
    user_message = request.json.get('message', '')
    response = get_chatbot_response(user_message)
    save_chat_to_database(user_message, response)
    return jsonify({'response': response})

# Add URL rules for each function in chat.py
app.add_url_rule('/chat', 'chat', chat)
app.add_url_rule('/process_message', 'process_message', process_message, methods=['POST'])



# Funcion para conprobar si existe el codigo del ejecutivo en la base de datos
def check_access_code(access_code):
    connection = db_connection()
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



# Permitir al usuario recuperar y actualizar sus credenciales
@app.route('/password_recovery')
def  password_recovery():
    return render_template('recover_account.html')




# Permite el acceso y la funcionalidad a la interfaz para actualizar credenciales
@app.route('/reset_password')
def  reset_password():
    return render_template('reset_password.html')


if __name__ == '__main__':
    app.run(debug=True)