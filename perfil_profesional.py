from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="7>>HhNN6/fZ",
  database="profesionales"
)

@app.route('/perfil_profesional', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Get form data
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        ubicacion = request.form['ubicacion']
        contacto = request.form['contacto']
        licencia = request.form['licencia']
        estudios_academicos = request.form['estudios_academicos']
        keywords = request.form['keywords']
        foto = request.files['foto']

        # Save photo to desired location
        photo_path = 'static/photos/' + foto.filename
        foto.save(photo_path)

        # Insert data into MySQL database
        mycursor = mydb.cursor()
        sql = "INSERT INTO perfil (nombre, licencia, ubicacion, contacto, descripcion, file_path) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nombre, licencia, ubicacion, contacto, descripcion, photo_path)
        mycursor.execute(sql, val)
        mydb.commit()

        return 'Profile updated successfully!'
    else:
        return render_template('editarPerfilProfesional.html')

if __name__ == '__main__':
    app.run(debug=True)