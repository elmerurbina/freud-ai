from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='profesionales',
            user='root',
            password='7>>HhNN6/fZ'
        )
        if connection.is_connected():
            print(f"Connected to MySQL Server version {connection.get_server_info()}")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")

class ProfessionalForm(FlaskForm):
    profile_picture = FileField('Subir imagen de perfil:', validators=[DataRequired()])
    nombre = StringField('Nombre:', validators=[DataRequired()])
    licencia = StringField('No. De Licencia:', validators=[DataRequired()])
    ubicacion = StringField('Ubicacion:', validators=[DataRequired()])
    contacto = StringField('Informacion de contacto:')
    descripcion = TextAreaField('Descripcion:')
    submit = SubmitField('Agregar')

def get_profesionales_data():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM registro")
    professionals = cursor.fetchall()
    cursor.close()
    close_connection(connection)
    return professionals

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_profesional():
    form = ProfessionalForm()
    connection = None
    message = None

    if form.validate_on_submit():
        try:
            # Connect to MySQL database
            connection = create_connection()

            # Save the uploaded file
            profile_picture = request.files['profile_picture']
            file_path = f"uploads/{profile_picture.filename}"
            profile_picture.save(file_path)

            # Create a new Professional record
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO registro (nombre, licencia, ubicacion, contacto, descripcion, file_path)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (form.nombre.data, form.licencia.data, form.ubicacion.data, form.contacto.data, form.descripcion.data, file_path))
            connection.commit()
            cursor.close()

            message = "Perfil agregado correctamente"
            return redirect(url_for('profesionales'))
        except Error as e:
            print(f"Error: {e}")
            message = "Error al agregar el perfil"
        finally:
            if connection is not None:
                close_connection(connection)

    return render_template('agregar.html', form=form, message=message)

@app.route('/profesionales')
def profesionales():
    professionals = get_profesionales_data()
    return render_template('profesionales.html', professionals=professionals)

if __name__ == '__main__':
    app.run(debug=True)
