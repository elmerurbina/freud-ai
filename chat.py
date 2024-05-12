# Contiene la logica del chatbot

import random
from db import save_chat_message, close_connection, connect_to_database, fetch_data_from_information_table
from Join_Rasa_Python import get_combined_data
from flask import jsonify, request, Flask, session


# Inicializacion de la app
app = Flask(__name__)


# Acceder a los datos del Rasa Project
combined_data = get_combined_data()


# Establece la conexión con la base de datos
connection = connect_to_database()


# Métodos para cada intención
def greeting(saludar):
    if saludar in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][saludar])
    else:
        response = fetch_data_from_information_table()
    return response

def sad(estado_animo_triste):
    if estado_animo_triste in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estado_animo_triste])
    else:
        response = fetch_data_from_information_table()
    return response

def anxiety_state(estado_animo_ansioso):
    if estado_animo_ansioso in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estado_animo_ansioso])
    else:
        response = fetch_data_from_information_table()
    return response

def happy(estado_animo_feliz):
    if estado_animo_feliz in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estado_animo_feliz])
    else:
        response = fetch_data_from_information_table()
    return response

def stress(estres):
    if estres in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estres])
    else:
        response = fetch_data_from_information_table()
    return response

def anxiety(ansiedad):
    if ansiedad in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][ansiedad])
    else:
        response = fetch_data_from_information_table()
    return response

def depression(depresion):
    if depresion in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][depresion])
    else:
        response = fetch_data_from_information_table()
    return response

def trauma(estres_post_traumatico):
    if estres_post_traumatico in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estres_post_traumatico])
    else:
        response = fetch_data_from_information_table()
    return response

def addiction(adiccion):
    if adiccion in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][adiccion])
    else:
        response = fetch_data_from_information_table()
    return response

def insomnia(insomnio):
    if insomnio in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][insomnio])
    else:
        response = fetch_data_from_information_table()
    return response

def narcolepsy(narcolepsia):
    if narcolepsia in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][narcolepsia])
    else:
        response = fetch_data_from_information_table()
    return response

def fobias(Fobias):
    if Fobias in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][Fobias])
    else:
        response = fetch_data_from_information_table()
    return response

def bulimia(Bulimia):
    if Bulimia in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][Bulimia])
    else:
        response = fetch_data_from_information_table()
    return response


# El chatbot reconocera ciertas palabras posibles en los mensajes del usuario y le dara una respuesta predeterminada
def get_chatbot_response(user_input):


    # Expresiones predefinidas de saludo
    if any(word in user_input.lower() for word in ['hola', 'saludos', 'buenos días', 'buenos dias', 'buenas tardes', 'buenas noches']):
        return '¡Hola! ¿Cómo te encuentras?'


      # Posibles respuestas al saludo
    elif any(word in user_input.lower() for word in ['bien', 'bien gracias a Dios', 'bien gracias a dios']):
        return 'Me alegro que estés bien, ¿De qué tema te gustaría hablar hoy?'


      # Para respuestas negativas
    elif any(word in user_input.lower() for word in ['mal', 'horrible', 'decepcionado']):
        return 'Comprendo que te sientas mal, estoy aquí para escucharte y ayudarte, cuéntame ¿por qué te sientes mal?'


    elif any(word in user_input.lower() for word in ['estoy ansioso', 'ansioso', 'me siento ansioso', 'tengo ansiedad']):
        return 'Entiendo. La ansiedad es una experiencia común. ¿Te gustaría hablar sobre lo que la está desencadenando?'


    elif 'estres' in user_input.lower():
        return 'Algunas causas del estrés son fracaso, universidad, mucho trabajo. ¿En los últimos días has tenido alguno de estos problemas?'


    elif any(word in user_input.lower() for word in ['me siento solo', 'no tengo a nadie a mi lado']):
        return 'La soledad no siempre es mala, muchas veces nos ayuda a reflexionar y a encontrarnos a nosotros mismos. ¿Dime de qué tema deseas hablar?'


    elif any(word in user_input.lower() for word in ['me siento triste', 'estoy deprimido']):
        return 'Lamento escuchar que te sientes así. ¿Puedes compartir más sobre lo que ha estado sucediendo?'


    elif any(word in user_input.lower() for word in ['cómo manejar el estrés', 'consejos para reducir el estrés']):
        return 'El manejo del estrés es importante. Algunas estrategias incluyen la práctica de la respiración profunda y el autocuidado. ¿Te gustaría más información?'


    elif any(word in user_input.lower() for word in ['pensamientos suicidas', 'necesito ayuda urgente']):
        return 'Lo siento mucho que estés pasando por esto. Es crucial buscar ayuda de emergencia. Por favor, comunícate con una línea de prevención de suicidios o busca ayuda profesional de inmediato.'


    elif any(word in user_input.lower() for word in ['me quiero suicidar', 'mi vida es una mierda', 'me quiero morir']):
        return 'La vida es algo muy valioso, entiendo que te sientas mal pero yo estoy aquí para ayudarte. Cuéntame más sobre lo que estás pasando y te brindaré todo mi apoyo'


    elif any(word in user_input.lower() for word in ['cómo lidiar con el estrés', 'técnicas de afrontamiento']):
        return 'Hay diversas técnicas de afrontamiento, como la meditación, el ejercicio y la búsqueda de apoyo social. ¿Te gustaría más sugerencias personalizadas?'


    elif any(word in user_input.lower() for word in ['explorar emociones', 'autoconocimiento']):
        return 'Explorar tus emociones puede ser un viaje enriquecedor. ¿Te gustaría discutir más sobre tus sentimientos y experiencias?'


    elif any(word in user_input.lower() for word in ['agradecimiento', 'cómo encontrar la positividad']):
        return 'Practicar la gratitud puede tener un impacto positivo. ¿Hay algo específico por lo que te sientas agradecido hoy?'


    elif any(word in user_input.lower() for word in ['cómo', 'qué', 'cuándo', 'dónde']):
        return 'Esa es una pregunta interesante. ¿Puedes proporcionar más detalles?'


# Si el bot no logra identificar los ninguna palabra clave, mostara un mensaje de default
    else:
        return 'Lo siento, no entiendo completamente. ¿Puedes proporcionar más información o formular tu pregunta de otra manera?'


# Maneja los mensajes d elos usuarios
def handle_user_message(user_id, message):
    # Procesa el mensaje y da al usuario la respuesta apropiada
    response = get_chatbot_response(message)


    # Guardar los mensajes del usuario en la base de datos
    connection = connect_to_database(database='usuarios')  # Conectar a la bd
    if connection:
        save_chat_message(connection, user_id, message, response)
        close_connection(connection)  # Cierra la conexión

    return response


# Procesa los mensajes
@app.route('/process_message', methods=['POST'])
def process_message(): # Checa si el usuario inicio sesion correctamente
    if 'user_id' not in session:
        return jsonify({'response': 'Su sesion a expirado. Por favor inicie sesion nuevamente!'})


# Consigue el mensaje utilizando una solicitud de tipo JSON
    request_data = request.get_json()
    user_message = request_data.get('message', '')


    # Cargar el id del usuario
    user_id = session['user_id']

    # Pasa dicho id a la funcion de manejo de los mensajes
    response = handle_user_message(user_id=user_id, message=user_message)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
