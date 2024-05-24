# Maneja la logica de agregar, mostrar, editar, eliminar los perfiles de los psicologos

from flask import *
from werkzeug.utils import secure_filename
import os
from db import *
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from config import SECRET_KEY
from flask_wtf.file import FileAllowed



# Instancia de la aplicacion
app = Flask(__name__)


# Clave secreta secreta generada al hazar
app.config['SECRET_KEY'] = SECRET_KEY


# Lugar donde se guardan y almacenan (en maquina local) las fotos de perfil subidas
UPLOAD_FOLDER = 'static/uploads'


# Formatos de imagen permitidos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# Configuracion del guardado de las fotos
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Formulario de los campos para agregar un nuevo perfil
class ProfessionalForm(FlaskForm):
    profile_picture = FileField('Subir imagen de perfil:', validators=[FileAllowed(ALLOWED_EXTENSIONS, 'Solo imágenes permitidas')])
    nombre_completo = StringField('Nombre Completo:', validators=[DataRequired()]) # Valor requerido
    licencia = StringField('No. De Licencia:', validators=[DataRequired()]) # Valor requerido
    estudios_academicos = TextAreaField('Estudios Académicos:')
    contacto = StringField('Información de contacto:', validators=[DataRequired()]) # Campo requerido
    keywords = StringField('Palabras Clave:', validators=[DataRequired()]) # Campo requerido
    ubicacion = StringField('Ubicación:')
    descripcion = TextAreaField('Descripción:')
    whatsapp = StringField('WhatsApp:')
    submit = SubmitField('Agregar')

# Ruta para agregar el nuevo perfil
@app.route('/agregar_perfil', methods=['GET', 'POST'])
def agregar_perfil():
    form = ProfessionalForm()
    # Inicializacion de la variable message para utilizarse en la plantilla
    message = None

    # Una vez se hace click en el boton "Agregar"
    if form.validate_on_submit():
        try: # Manejo de excepciones
            # Conectar a la base de datos
            connection = connect_to_profesionales_database()

            file_path = None  # Se inicializa la variable de la foto de perfil

            # Guardar el archivo subido
            if form.profile_picture.data:
                profile_picture = form.profile_picture.data
                filename = secure_filename(profile_picture.filename)
                file_path = f"{UPLOAD_FOLDER}/{filename}"
                profile_picture.save(file_path)

            # Crear un nuevo perfil
            if save_profesional(connection, form, file_path):
                message = "Perfil agregado correctamente" # Si el perfil se agrega correctamente
                return redirect(url_for('profesionales')) # Redirige a la pagina donde se muestran los perfiles
            else:
                # De lo contrario se muestra un mensaje de error
                message = "Ocurrió un error! No se pudo agregar el nuevo perfil."
        except Error as e:
            print(f"Error: {e}")
            message = "Ocurrió un error! No se pudo agregar el nuevo perfil."
        finally:
            if connection is not None:
                close_profesionales_connection(connection)

    # Esta es la plantilla desde la cual se llena el formulario
    return render_template('agregar.html', form=form, message=message)

# Ruta para mostrar los perfiles de los profesionales en su respectiva plantilla
@app.route('/profesionales')

def profesionales():
    connection = connect_to_profesionales_database() # Funcion para conectar a la base de datos
    professionals = get_profesionales_data(connection) # Accedida de db.py
    close_profesionales_connection(connection)
    # Plantilla para mostrar los perfiles
    return render_template('profesionales.html', professionals=professionals)


#Funcion para ver perfil utilizando el numero de Licencia como verificacion
@app.route('/check_profile', methods=['POST'])
def check_profile():
    # Recibe un numero de licencia
    licencia = request.form.get('licencia')
    connection = connect_to_profesionales_database()
    # Funcion accedida de db.py comprubea si la Licencia existe en la base de datos
    profesional = get_profesional_by_licencia(connection, licencia)
    if profesional:
       # Si existe la Licencia mostrarle su perfil
        return render_template('perfil.html', profesional=profesional)
    else:
        # En caso contrario mostrar un mensaje de error
        return f'Error: No encontramos su perfil, por favor verifique su licencia'


# Ruta para eliminar perfil
@app.route('/delete_profile/<int:profile_id>', methods=['POST'])

def delete_profile(profile_id):
    connection = connect_to_profesionales_database() # Conectar a la base de datos
    try:
        # Llevar acabo la eliminacion del perfil a traves del ID del perfil
        if delete_professional(connection, profile_id):
            return 'Perfil eliminado correctamente', 200
        else:
            return 'Error: No se pudo eliminar el perfil', 500
    except Exception as e:
        print(f"Error deleting profile: {e}")
        return 'Error: No se pudo eliminar el perfil', 500
    finally:
        close_connection(connection)


# Ruta para manejar la edicion del perfil y la plantillla de las formas
@app.route('/edit_profile', methods=['GET', 'POST'])

def edit_profile():


    if request.method == 'GET':
        # Mostrar la plantilla de edicion
        return render_template('perfil.html')  # Se carga el perfil


    elif request.method == 'POST':
        # Maneja la solicitud del formato y actualiza el perfil
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


        # Permite subir una foto de perfil
        if foto.filename != '':
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Se guarda en la carpeta uploads
            foto_path = os.path.join('uploads', filename)
        else:
            foto_path = None

        # Accede al id del usuaio
        profile_id = request.form.get('id')  # Adjust this according to your session or form structure


        # Conecta a la base de datos
        connection = connect_to_profesionales_database()


        # Actualiza la informacion de los profesionales en la base de datos
        if update_professional(connection, profile_id, nombre, ubicacion, contacto, licencia, estudios_academicos, keywords, descripcion, foto_path):
            message = "Perfil actualizado exitosamente"
        else:
            message = "Ocurrió un error al actualizar el perfil"


        # Consigue los datos actualizados desde la base de datos
        professionals = get_profesionales_data(connection)


        # Cierra la conexion con la base de datos
        close_profesionales_connection(connection)


        # Retornar a la plantilla de los profesionales con la nformacion actualizada
        return render_template('profesionales.html', message=message, professionals=professionals)


if __name__ == '__main__':
    app.run(debug=True)
