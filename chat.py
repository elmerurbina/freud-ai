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


# Palabras claves de posibles mensajes
keyword_responses = {
    'saludos': ['hola', 'saludos', 'buenos días', 'buenos dias', 'buenas tardes', 'buenas noches'],
    'saludos_nicas': ['que onda', 'oe', 'q nta', 'entonces', 'oe perro'],
    'respuesta_bien': ['bien', 'bien gracias a dios'],
    'respuesta_mal': ['mal', 'horrible', 'decepcionado'],
    'ansiedad': ['estoy ansioso', 'ansioso', 'me siento ansioso', 'tengo ansiedad'],
    'estres': ['estres'],
    'soledad': ['me siento solo', 'no tengo a nadie a mi lado'],
    'tristeza': ['me siento triste', 'estoy deprimido'],
    'manejar_estres': ['cómo manejar el estrés', 'consejos para reducir el estrés'],
    'suicidio': ['pensamientos suicidas', 'necesito ayuda urgente'],
    'pensamientos_suicidas': ['me quiero suicidar', 'mi vida es una mierda', 'me quiero morir'],
    'afrontar_estres': ['cómo lidiar con el estrés', 'técnicas de afrontamiento'],
    'explorar_emociones': ['explorar emociones', 'autoconocimiento'],
    'gratitud': ['agradecimiento', 'cómo encontrar la positividad'],
    'preguntas': ['cómo', 'qué', 'cuándo', 'dónde']
}


# Respuestas a las palabras claves d elos mensajes del usuarios
responses = {
    'saludos': [
        '¡Hola! ¿Cómo te encuentras?',
        '¡Hola! ¿Qué tal tu día?',
        '¡Hola! ¿Cómo te va?'
    ],
    'saludos_nicas': [
        'Hola! Gusto saludarte',
        '¡Qué onda! ¿Cómo estás?',
        '¡Hola! ¿Qué tal todo?'
    ],
    'respuesta_bien': [
        'Me alegro que estés bien, ¿De qué tema te gustaría hablar hoy?',
        '¡Qué bueno saberlo! ¿Quieres conversar sobre algo en particular?',
        '¡Excelente! ¿Te gustaría hablar de algo específico?'
    ],
    'respuesta_mal': [
        'Comprendo que te sientas mal, estoy aquí para escucharte y ayudarte, cuéntame ¿por qué te sientes mal?',
        'Lamento que te sientas así, ¿quieres hablar más al respecto?',
        'Entiendo, es difícil. ¿Quieres contarme qué está pasando?'
    ],
    'ansiedad': [
        'Entiendo. La ansiedad es una experiencia común. ¿Te gustaría hablar sobre lo que la está desencadenando?',
        'La ansiedad puede ser abrumadora. ¿Quieres hablar sobre lo que la está causando?',
        'Sé que la ansiedad puede ser difícil de manejar. ¿Qué ha estado pasando?'
    ],
    'estres': [
        'Algunas causas del estrés son fracaso, universidad, mucho trabajo. ¿En los últimos días has tenido alguno de estos problemas?',
        'El estrés puede ser causado por varias cosas. ¿Has enfrentado algo estresante recientemente?',
        'Comprendo, el estrés puede venir de muchas fuentes. ¿Qué te ha estado afectando últimamente?'
    ],
    'soledad': [
        'La soledad no siempre es mala, muchas veces nos ayuda a reflexionar y a encontrarnos a nosotros mismos. ¿Dime de qué tema deseas hablar?',
        'La soledad puede ser difícil, pero también una oportunidad para el autodescubrimiento. ¿Quieres hablar más sobre ello?',
        'Sentirse solo puede ser duro. Estoy aquí para escucharte. ¿De qué te gustaría hablar?'
    ],
    'tristeza': [
        'Lamento escuchar que te sientes así. ¿Puedes compartir más sobre lo que ha estado sucediendo?',
        'Es difícil sentirse triste. ¿Quieres hablar sobre lo que te ha pasado?',
        'Siento mucho que te sientas triste. ¿Qué te ha llevado a sentirte así?'
    ],
    'manejar_estres': [
        'El manejo del estrés es importante. Algunas estrategias incluyen la práctica de la respiración profunda y el autocuidado. ¿Te gustaría más información?',
        'Reducir el estrés puede implicar varias técnicas, como el ejercicio y la meditación. ¿Quieres saber más?',
        'Hay muchas maneras de manejar el estrés. ¿Qué tipo de consejos buscas?'
    ],
    'suicidio': [
        'Lo siento mucho que estés pasando por esto. Es crucial buscar ayuda de emergencia. Por favor, comunícate con una línea de prevención de suicidios o busca ayuda profesional de inmediato.',
        'Es muy importante que hables con alguien de confianza o busques ayuda profesional de inmediato.',
        'Tu bienestar es lo más importante. Busca ayuda de emergencia lo antes posible, por favor.'
    ],
    'pensamientos_suicidas': [
        'La vida es algo muy valioso, entiendo que te sientas mal pero yo estoy aquí para ayudarte. Cuéntame más sobre lo que estás pasando y te brindaré todo mi apoyo',
        'Es muy importante hablar con alguien que pueda ayudarte en este momento. Cuéntame más y veamos cómo puedo apoyar.',
        'Lamento que te sientas así. Es crucial buscar apoyo de alguien de confianza o un profesional. ¿Quieres hablar sobre lo que te ha llevado a sentirte así?'
    ],
    'afrontar_estres': [
        'Hay diversas técnicas de afrontamiento, como la meditación, el ejercicio y la búsqueda de apoyo social. ¿Te gustaría más sugerencias personalizadas?',
        'Afrontar el estrés puede involucrar varias estrategias. ¿Qué tipo de ayuda estás buscando?',
        'El manejo del estrés puede ser multifacético. ¿Qué técnicas has probado hasta ahora?'
    ],
    'explorar_emociones': [
        'Explorar tus emociones puede ser un viaje enriquecedor. ¿Te gustaría discutir más sobre tus sentimientos y experiencias?',
        'Hablar sobre tus emociones puede ayudarte a entenderte mejor. ¿Qué te gustaría explorar hoy?',
        'El autoconocimiento es muy valioso. ¿De qué aspecto emocional quieres hablar?'
    ],
    'gratitud': [
        'Practicar la gratitud puede tener un impacto positivo. ¿Hay algo específico por lo que te sientas agradecido hoy?',
        'Encontrar la positividad en pequeñas cosas puede hacer una gran diferencia. ¿Qué te ha traído alegría últimamente?',
        'La gratitud puede cambiar nuestra perspectiva. ¿Qué te hace sentir agradecido hoy?'
    ],
    'preguntas': [
        'Esa es una pregunta interesante. ¿Puedes proporcionar más detalles?',
        'Me encantaría ayudarte con eso. ¿Podrías darme más información?',
        'Buena pregunta. ¿Puedes darme más contexto?'
    ],
    'default': [
        'Lo siento, no entiendo completamente. ¿Puedes proporcionar más información o formular tu pregunta de otra manera?',
        'No estoy seguro de cómo responder a eso. ¿Puedes decirlo de otra forma?',
        'Podrías intentar reformular tu pregunta. Estoy aquí para ayudar.'
    ]
}




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
    user_input = user_input.lower()

    # Iterate over the keyword_responses dictionary
    for intent, keywords in keyword_responses.items():
        for keyword in keywords:
            if keyword in user_input:
                return random.choice(responses[intent])

    # If no keyword is found, return a default response
    return random.choice(responses['default'])
# Maneja los mensajes d elos usuarios


# Store conversation history for each user session
conversation_history = {}


# Define a function to handle user messages and generate responses
def handle_user_message(user_id, message):
    # Retrieve conversation history for the user
    history = conversation_history.get(user_id, [])

    # Add the current message to the conversation history
    history.append(message)
    conversation_history[user_id] = history

    # Process the conversation context to determine the response
    response = generate_contextual_response(user_id, history)

    # If a contextual response is not generated, fallback to keyword-based response
    if response is None:
        response = get_chatbot_response(message)

    # Save the user message and bot response in the database
    connection = connect_to_database(database='usuarios')
    if connection:
        save_chat_message(connection, user_id, message, response)
        close_connection(connection)

    return response


# Define a function to generate a contextual response based on conversation history
def generate_contextual_response(user_id, history):
    # Analyze the conversation history to determine the context
    # You can use machine learning models or rule-based approaches for context analysis

    # Based on the context, select an appropriate response
    # You can use conditional logic or a response selection model

    # For example, if the user's last message mentioned anxiety, the bot can respond with an anxiety-related message
    if 'anxiety' in history[-1].lower():
        return random.choice(responses['ansiedad'])

    # If no specific context is detected, return None to indicate that no contextual response is generated
    return None


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
