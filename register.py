from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from db import get_db
from flask_wtf import CSRFProtect
from encrypt import encrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

csrf = CSRFProtect(app)

# Define route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        affiliation = request.form['affiliation']
        role = request.form['role']
        pais = request.form['pais']
        departamento = request.form['departamento']
        municipio = request.form['municipio']

        # Validate password
        if len(password) < 8 or not any(char.isdigit() for char in password) \
                or not any(char.isupper() for char in password) \
                or not any(char.islower() for char in password):
            flash('Password must be at least 8 characters long and contain uppercase, lowercase, and numeric characters.', 'error')
            return redirect(url_for('register'))

        # Validate email (you can use regex for more accurate email validation)
        if '@' not in email or '.' not in email:
            flash('Invalid email address.', 'error')
            return redirect(url_for('register'))

        # Make left group required
        if not name or not email or not password or not repeat_password:
            flash('All fields in the left group are required.', 'error')
            return redirect(url_for('register'))

        # Check if passwords match
        if password != repeat_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('register'))

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password, method='sha256')

        encrypted_name = encrypt(name, password)
        encrypted_email = encrypt(email, password)
        encrypted_municipio = encrypt(municipio, password)


        # Insert user data into the database
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, contrasena, afiliacion_id, rol_id, pais_id, departamento_id, municipio) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (encrypted_name, encrypted_email, hashed_password, affiliation, role, pais, departamento, encrypted_municipio)
        )
        db.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('register'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
