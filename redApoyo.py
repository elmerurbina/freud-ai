from flask import Flask, render_template, request, redirect, url_for
from db import connect_to_database
import mysql.connector.errors

app = Flask(__name__)

# Route to render the template with the forms
@app.route('/redApoyo')
def redApoyo():
    return render_template('redApoyo.html')

# Function to handle saving data into the database
@app.route('/guardar_red', methods=['POST'])
def guardar_red():
    # Extract form data
    name_one = request.form['name-one']
    name_two = request.form['name-two']
    psychologist_name = request.form['psychologist-name']
    contact_one = request.form['contact-one']
    contact_two = request.form['contact-two']
    psychologist_contact = request.form.get('psychologist-contact', None)

    # Connect to the database
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL INSERT query to save the data
        if psychologist_contact:
            cursor.execute("""
                        INSERT INTO redapoyo (full_name_one, country_code_one, number_one, full_name_two, country_code_two, number_two, psychologist_name, psychologist_contact)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
            name_one, None, contact_one, name_two, None, contact_two, psychologist_name, psychologist_contact))
        else:
            cursor.execute("""
                        INSERT INTO redapoyo (full_name_one, country_code_one, number_one, full_name_two, country_code_two, number_two, psychologist_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (name_one, None, contact_one, name_two, None, contact_two, psychologist_name))

        connection.commit()

        # Close cursor and connection
        cursor.close()
        connection.close()

        # Display success message
        return "Los datos se guardaron correctamente."

    except mysql.connector.Error as e:
        # Handle database errors
        error_message = "No se pudieron guardar los datos, inténtalo de nuevo."
        return error_message

# Route for the success page
@app.route('/success')
def success():
    return render_template('success.html')

# Function to view the support network
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
