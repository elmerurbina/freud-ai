from flask import Flask, render_template, redirect, url_for, request, session
from db import check_username_exists  # Import the function from db.py

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/panelPsicologo', methods=['GET', 'POST'])
def panelPsicologo():
    if request.method == 'POST':
        username = request.form.get('username')
        if check_username_exists(username):
            # Store the username in the session
            session['username'] = username
            # Redirect to the expediente route with the username
            return redirect(url_for('expediente', username=username))
        else:
            error_message = "Nombre de usuario incorrecto"
            return render_template('panelPsicologo.html', error_message=error_message)
    return render_template('panelPsicologo.html')

if __name__ == '__main__':
    app.run(debug=True)
