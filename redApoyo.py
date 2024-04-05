from flask import Flask, render_template, request, redirect, url_for
from db import connect_to_database
import mysql.connector.errors



app = Flask(__name__)

# Route to display the form
@app.route('/redApoyo')
def redApoyo():
    return render_template('redApoyo.html')


# Funcion para manejar el ingreso de los datos en la base de datos
@app.route('/guardar_red', methods=['POST'])
def guardar_red():
    # Extract form data
    contact_one = request.form['contact-one']
    contact_two = request.form['contact-two']
    psychologist_email = request.form.get('psychologist-email', None)

    # Connect to the database
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL INSERT query to save the data
        if psychologist_email:
            cursor.execute("""
                    INSERT INTO redapoyo (contact_one, contact_two, psychologist_email)
                    VALUES (%s, %s, %s)
                """, (contact_one, contact_two, psychologist_email))
        else:
            cursor.execute("""
                    INSERT INTO redapoyo (contact_one, contact_two)
                    VALUES (%s, %s)
                """, (contact_one, contact_two))

        # Commit the transaction
        connection.commit()

        # Close cursor and connection
        cursor.close()
        connection.close()

        # Redirect to a success page or return a success message
        return redirect(url_for('success'))

    except mysql.connector.Error as e:
        # Handle database errors
        error_message = "Error saving data to the database: {}".format(e)
        return render_template('error.html', error=error_message)

# Ruta para la pagina de exito
@app.route('/success')
def success():
    return render_template('success.html')

# Funcion para ver la red de apoyo
@app.route('/red_de_apoyo')
def red_de_apoyo():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL SELECT query to retrieve saved contacts
        cursor.execute("SELECT * FROM redapoyo")
        contacts = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        connection.close()

        return render_template('red_de_apoyo.html', contacts=contacts)

    except mysql.connector.Error as e:
        # Handle database errors
        error_message = "Error retrieving data from the database: {}".format(e)
        return render_template('error.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
