from flask import Flask, render_template, request, jsonify
from db import connect_to_database, save_chat_message, close_connection
import datetime

app = Flask(__name__, static_url_path='/static')


app.secret_key = 'your_secret_key'


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/process_message', methods=['POST'])
def process_message():
    user_message = request.json.get('message', '')

    # Procesar el mensaje del usuario y generar un mensaje
    response = get_chatbot_response(user_message)

    return jsonify({'response': response})

# Clase para definir la logica de las respuestas a generar
def get_chatbot_response(user_input):
    # Saludos comunes
    if any(word in user_input.lower() for word in ['hola', 'saludos', 'buenos días', 'buenas tardes', 'buenas noches']):
        return '¡Hola! ¿Cómo te encuentras?'


def save_chat_to_database(user_message, response):
    try:
        connection = connect_to_database(database='usuarios')
        if connection:
            now = datetime.datetime.now()
            save_chat_message(connection, now, user_message, response)
            close_connection(connection)
    except Exception as e:
        print("Error saving chat message:", e)

# Rest of your code...

if __name__ == '__main__':
    app.run(debug=True)
