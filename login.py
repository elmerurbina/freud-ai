from flask import Flask, render_template, request, redirect, url_for
from db import connect_to_database

app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        connection = connect_to_database()
        cursor = connection.cursor()

        # Check if the email and password match the records in the database
        query = "SELECT * FROM sistema_registro WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        # Fetch all remaining rows from the result set
        cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        if user:
            # Redirect to chat.html upon successful login
            return redirect(url_for('chat'))
        else:
            error = 'Credenciales incorrectas. Por favor, inténtelo de nuevo.'
            return render_template('login.html', error=error)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
