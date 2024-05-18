from flask import Flask, request, render_template, jsonify, url_for, redirect, flash
from db import valid_code, connect, close

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/aseguradora', methods=['GET', 'POST'])
def aseguradora():
    if request.method == 'POST':
        codigo = request.form['codigo']
        if valid_code(codigo):
            # If code is valid, render the registration form
            return render_template('codigoAseguradora.html', display_credenciales=True)
        else:
            # If code is invalid, display error message and stay on the same page
            return render_template('codigoAseguradora.html', display_credenciales=False, codigo_error="Código incorrecto. Inténtalo de nuevo.")
    # If method is GET, display the initial page
    return render_template('codigoAseguradora.html', display_credenciales=False)

@app.route('/codigoRegistro', methods=['POST'])
def codigoRegistro():
    nombre = request.form['nombre']
    codigo_unico = request.form['codigo_unico']

    connection = connect()
    if connection is None:
        flash('Error connecting to the database.', 'error')
        return redirect(url_for('aseguradora'))

    cursor = connection.cursor()

    # Check if the codigo_unico already exists
    cursor.execute("SELECT * FROM codigo WHERE codigo_unico = %s", (codigo_unico,))
    existing_codigo = cursor.fetchone()

    if existing_codigo:
        flash('El código único ya existe. Por favor, intente con otro código.', 'error')
        close(connection)
        return redirect(url_for('aseguradora'))

    # Insert the new entry into the database
    cursor.execute("INSERT INTO codigo (nombre_y_apellidos, codigo_unico) VALUES (%s, %s)", (nombre, codigo_unico))
    connection.commit()

    flash('Código registrado exitosamente.', 'success')
    close(connection)
    return redirect(url_for('aseguradora'))

@app.route("/check_code_validity", methods=["POST"])
def check_code_validity():
    codigo = request.json.get("codigo")
    if valid_code(codigo):
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})

if __name__ == '__main__':
    app.run(debug=True)
