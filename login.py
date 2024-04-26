from flask import Flask, render_template, request, redirect, url_for, session
from db import connect_to_database

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        connection = connect_to_database()
        cursor = connection.cursor()

        try:
            # Check if the email and password match the records in the database
            query = "SELECT id FROM sistema_registro WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user_id = cursor.fetchone()

            # Consume all results (even if only one expected)
            cursor.fetchall()

            if user_id:
                # Store the user ID in the session
                session['id'] = user_id[0]

                # Redirect to chat.html upon successful login
                return redirect(url_for('chat'))
            else:
                error = 'Credenciales incorrectas. Por favor, inténtelo de nuevo.'
                return render_template('login.html', error=error)
        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
