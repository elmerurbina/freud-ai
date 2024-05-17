from flask import render_template, redirect, url_for, request, session, Flask
from db import connect_to_database, close_connection, get_patient_info_by_user_id, get_chat_messages_by_user_id
from datetime import datetime
from db import save_prescription, save_diagnostic_test, save_medical_history_entry

app = Flask(__name__)

@app.route('/expediente', methods=['GET', 'POST'])
def expediente():
    if 'user_id' in session:
        user_id = session['user_id']
        # Fetch patient information based on the user ID
        patient_info = get_patient_info_by_user_id(user_id)
        if patient_info:  # Check if patient_info is not None
            # Fetch the most common messages sent by the user
            common_messages = get_most_common_messages(user_id)
            # Calculate the age of the patient based on their birthdate
            age = calculate_age(patient_info['date_of_birth'])
            # Render the expediente template and pass patient information
            return render_template('expediente.html', patient_info=patient_info, common_messages=common_messages, age=age)
        else:
            # Handle the case where patient_info is None (e.g., patient not found)
            return "No pudimos encontrar la informacion del paciente."
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('login'))


def calculate_age_from_birthdate(birthdate):
    today = datetime.today()
    birthdate_str = birthdate.strftime('%Y-%m-%d')  # Convert datetime.date to string
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')  # Convert string to datetime
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Function to retrieve top messages
def retrieve_top_messages(messages):
    # Implement your logic here to determine the top messages
    # For demonstration purposes, let's assume we return the first 5 messages
    top_messages = messages[:5]
    return top_messages

def get_most_common_messages(user_id):
    connection = connect_to_database()
    if connection:
        try:
            messages = get_chat_messages_by_user_id(connection, user_id)
            # Implement logic to determine most common messages
            # This could involve counting occurrences of each message and selecting the top ones
            # For demonstration purposes, let's assume we have a function to retrieve top messages
            common_messages = retrieve_top_messages(messages)
            close_connection(connection)
            return common_messages
        except Exception as e:
            print("Error fetching common messages:", e)
            close_connection(connection)
            return []
    else:
        return []

def calculate_age(birthdate):
    # Implement logic to calculate age based on birthdate
    # This could involve parsing the birthdate and subtracting it from the current date
    # For demonstration purposes, let's assume we have a function to calculate age
    return calculate_age_from_birthdate(birthdate)

@app.route('/add_medical_history', methods=['POST'])
def add_medical_history():
    if 'user_id' in session:
        user_id = session['user_id']
        fecha = request.form.get('fecha')
        descripcion = request.form.get('descripcion')

        # Save the medical history entry to the database
        success = save_medical_history_entry(user_id, fecha, descripcion)

        if success:
            # Redirect to the expediente page after adding the entry
            return redirect(url_for('expediente'))
        else:
            # Handle error case, maybe display an error message
            return "Error: Failed to add medical history entry"
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('login'))

@app.route('/add_prescription', methods=['POST'])
def add_prescription():
    if 'user_id' in session:
        user_id = session['user_id']
        fecha = request.form.get('fecha')
        medicamento = request.form.get('medicamento')

        # Save the prescription entry to the database
        success = save_prescription(user_id, fecha, medicamento)

        if success:
            # Redirect to the expediente page after adding the entry
            return redirect(url_for('expediente'))
        else:
            # Handle error case, maybe display an error message
            return "Error: Failed to add prescription entry"
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('login'))

@app.route('/add_diagnostic_test', methods=['POST'])
def add_diagnostic_test():
    if 'user_id' in session:
        user_id = session['user_id']
        fecha = request.form.get('fecha')
        prueba = request.form.get('prueba')
        resultado = request.form.get('resultado')

        # Save the diagnostic test entry to the database
        success = save_diagnostic_test(user_id, fecha, prueba, resultado)

        if success:
            # Redirect to the expediente page after adding the entry
            return redirect(url_for('expediente'))
        else:
            # Handle error case, maybe display an error message
            return "Error: Failed to add diagnostic test entry"
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)