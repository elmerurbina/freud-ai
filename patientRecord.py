from flask import Flask, render_template, request, redirect, url_for
from db import *

app = Flask(__name__)

@app.route('/acceder_expediente', methods=['GET', 'POST'])
def acceder_expediente():
    username = request.form.get('username')
    if check_username_exists(username):
        # Fetch patient information based on the username
        patient_info = get_patient_info(username)
        # Render the expediente template and pass patient information
        return render_template('expediente.html', patient_info=patient_info)
    else:
        # Redirect to the same page with an error message
        return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(debug=True)
