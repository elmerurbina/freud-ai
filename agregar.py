from flask import Flask, render_template, request, redirect, url_for
from db import *
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

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


if __name__ == '__main__':
    app.run(debug=True)
