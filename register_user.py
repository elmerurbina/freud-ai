from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from db import get_db
from flask_wtf import CSRFProtect
from encrypt import encrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

csrf = CSRFProtect(app)

def is_email_registered(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE correo = %s", (email,))
    count = cursor.fetchone()[0]
    return count > 0

def register_logic(name, email, password, repeat_password, affiliation, role, pais, departamento, municipio):
    # Validate password
    if len(password) < 8 or not any(char.isdigit() for char in password) \
            or not any(char.isupper() for char in password) \
            or not any(char.islower() for char in password):
        return {'success': False, 'error': 'Password must be at least 8 characters long and contain uppercase, lowercase, and numeric characters.'}

    # Validate email (you can use regex for more accurate email validation)
    if '@' not in email or '.' not in email:
        return {'success': False, 'error': 'Invalid email address.'}

    if is_email_registered(email):
        return {'success': False, 'error': 'La cuenta ya existe. Vaya a iniciar sesión.'}

    # Make left group required
    if not name or not email or not password or not repeat_password:
        return {'success': False, 'error': 'All fields in the left group are required.'}

    # Check if passwords match
    if password != repeat_password:
        return {'success': False, 'error': 'Passwords do not match.'}

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

    return {'success': True}

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            repeat_password = request.form['repeat_password']
            affiliation = request.form['affiliation']
            role = request.form['role']
            pais = request.form['pais']
            departamento = request.form['departamento']
            municipio = request.form['municipio']

            result = register_logic(name, email, password, repeat_password, affiliation, role, pais, departamento, municipio)

            if result.get('success'):
                flash('Registration successful!', 'success')
                return redirect(url_for('profile', username=name))
            else:
                flash(result.get('error'), 'error')
                return render_template('register.html', name=name, email=email, affiliation=affiliation, role=role, pais=pais, departamento=departamento, municipio=municipio)
        except Exception as e:
            # Log the exception for debugging
            print(f"An error occurred: {str(e)}")
            flash('An error occurred during registration. Please try again.', 'error')
            return render_template('register.html')

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)