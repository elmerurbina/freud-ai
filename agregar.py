from flask import Flask, render_template, request
import os
from db import insert_profile_data
from flask import Blueprint

app = Flask (__name__, static_url_path='/static')

agregar_blueprint = Blueprint('Agregar', __name__)
@app.route('/agregar', methods=['POST', 'GET'])
def agregar_perfil():
    if request.method == 'POST':
        # Retrieve form data
        nombre = request.form['nombre']
        licencia = request.form['licencia']
        ubicacion = request.form['ubicacion']
        contacto = request.form['contacto']
        descripcion = request.form['descripcion']

        profile_picture = request.files['profile_picture']

        upload_folder = 'uploads'
        file_path = os.path.join(upload_folder, profile_picture.filename)
        profile_picture.save(file_path)

        if insert_profile_data(nombre, licencia, ubicacion, contacto, descripcion, file_path):
            return f"Profile for {nombre} Agregado exitosamente: {file_path}"

    return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)
