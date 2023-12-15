from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector
from db import get_db_connection
app = Flask (__name__, static_url_path='/static')
from flask import Blueprint

conn = get_db_connection()



register_blueprint = Blueprint('register', __name__)



@app.route('/register', methods=['GET', 'POST'])
def register_user():
    with get_db_connection() as conn, conn.cursor() as cursor:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            repeat_password = request.form['repeat_password']
            nationality = request.form['nationality']
            affiliation = request.form.get('affiliation', '')
            role = request.form.get('role', '')
            language = request.form['language']

            if password != repeat_password:
                print("Password must match")
            else:
                insert_query = "INSERT INTO users (name, email, password, nationality, affiliation, role, language) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (name, email, password, nationality, affiliation, role, language)

                try:
                    cursor.execute(insert_query, values)
                    conn.commit()
                    flash("success")
                    print("redirecting")
                    return redirect(url_for('bot'))
                except mysql.connector.Error as err:
                    conn.rollback()
                    flash(f"Error: {err}", "error")

    return render_template('register.html')





if __name__ == '__main__':
    app.run(debug=True)


