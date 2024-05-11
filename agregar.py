from flask import *
from werkzeug.utils import secure_filename
import os
from db import *
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Formulario de los campos para agregar un nuevo perfil
class ProfessionalForm(FlaskForm):
    profile_picture = FileField('Subir imagen de perfil:')
    nombre = StringField('Nombre:', validators=[DataRequired()])
    licencia = StringField('No. De Licencia:', validators=[DataRequired()])
    direccion = StringField('Direccion:')
    keywords = StringField('keywords:', validators=[DataRequired()])
    contacto = StringField('Informacion de contacto:', validators=[DataRequired()])
    descripcion = TextAreaField('Descripcion:')
    submit = SubmitField('Agregar')

# Ruta para agregar un perfil
@app.route('/agregar_perfil', methods=['GET', 'POST'])
def agregar_perfil():
    form = ProfessionalForm()
    message = None

    if form.validate_on_submit():
        try:
            # Conectar a la base de datos
            connection = connect_to_profesionales_database()

            file_path = None  # Define file_path variable here

            # Save the uploaded file
            if 'profile_picture' in request.files:
                profile_picture = request.files.get('profile_picture')
                file_path = f"uploads/{profile_picture.filename}"
                profile_picture.save(file_path)

            # Crear un nuevo perfil
            if save_profesional(connection, form, file_path):
                message = "Perfil agregado correctamente"
                return redirect(url_for('profesionales'))
            else:
                message = "Ocurrió un error! No se pudo agregar el nuevo perfil."
        except Error as e:
            print(f"Error: {e}")
            message = "Ocurrió un error! No se pudo agregar el nuevo perfil."
        finally:
            if connection is not None:
                close_profesionales_connection(connection)

    return render_template('agregar.html', form=form, message=message)

# Ruta para mostrar los perfiles de los profesionales en su respectiva plantilla
@app.route('/profesionales')
def profesionales():
    connection = connect_to_profesionales_database()
    professionals = get_profesionales_data(connection)
    close_profesionales_connection(connection)
    return render_template('profesionales.html', professionals=professionals)

#Funcion para ver perfil utilizando el numero de Licencia como verificacion
@app.route('/check_profile', methods=['POST'])
def check_profile():
    licencia = request.form.get('licencia')
    connection = connect_to_profesionales_database()
    profesional = get_profesional_by_licencia(connection, licencia)
    if profesional:

        return render_template('perfil.html', profesional=profesional)
    else:

        return f'Error: No encontramos su perfil, por favor verifique su licencia'

# Funcion para eliminar perfil
@app.route('/delete_profile/<int:profile_id>', methods=['POST'])
def delete_profile(profile_id):
    connection = connect_to_profesionales_database()
    try:
        # Perform delete operation based on the profile ID
        if delete_professional(connection, profile_id):
            return 'Perfil eliminado correctamente', 200
        else:
            return 'Error: No se pudo eliminar el perfil', 500
    except Exception as e:
        print(f"Error deleting profile: {e}")
        return 'Error: No se pudo eliminar el perfil', 500
    finally:
        close_connection(connection)


# Funcion para editar  perfil
@app.route('/editar_perfil', methods=['GET'])
def editar_perfil():
    # Render the edit profile template
    return render_template('editarPerfilProfesional.html')

# Route to handle the form submission and update the profile
@app.route('/edit_profile', methods=['POST'])
def edit_profile():
    # Retrieve form data from the request
    form = ProfessionalForm(request.form)
    foto = request.files['profile_picture']
    nombre = request.form['nombre']
    contacto = request.form['contacto']
    licencia = request.form['licencia']
    keywords = request.form['keywords']
    descripcion = request.form['descripcion']
    ubicacion = request.form.get('ubicacion', None)
    estudios_academicos = request.form.get('estudios_academicos', None)
    whatsapp = request.form.get('whatsapp', None)

    # Handle file upload
    if foto.filename != '':
        filename = secure_filename(foto.filename)
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        foto_path = os.path.join('uploads', filename)
    else:
        foto_path = None

    # Retrieve the profile ID from the session or form data
    profile_id = request.form.get('profile_id')  # Adjust this according to your session or form structure

    # Connect to the database
    connection = connect_to_profesionales_database()

    # Update the professional's information in the database
    if update_professional(connection, profile_id, nombre, ubicacion, contacto, licencia, estudios_academicos, keywords, descripcion, foto_path):
        message = "Perfil actualizado exitosamente"
    else:
        message = "Ocurrió un error al actualizar el perfil"

    # Get the updated professionals' data from the database
    professionals = get_profesionales_data(connection)

    # Close the database connection
    close_profesionales_connection(connection)

    # Render the template with the updated information
    return render_template('profesionales.html', message=message, professionals=professionals)

if __name__ == '__main__':
    app.run(debug=True)
