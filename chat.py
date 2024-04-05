from flask import Flask, render_template, request, jsonify
from db import connect_to_database, save_chat_message, close_connection


app = Flask(__name__, static_url_path='/static')


app.secret_key = 'your_secret_key'


@app.route('/chat')
def chat():
    return render_template('chat.html')


# Procesa los mensajes del usuario
@app.route('/process_message', methods=['POST'])
def process_message():
    user_message = request.json.get('message', '')

    # Procesa los mensajes del usuario y genera una respuesta
    response = get_chatbot_response(user_message)

    save_chat_to_database(user_message, response)

    return jsonify({'response': response})

# Muestra las respuestas del chatbot
def get_chatbot_response(user_input):
    # Estas son algunas respuestas pre-programadas a los saludos mas comunes
    # Saludos comunes
    if any(word in user_input.lower() for word in ['hola', 'saludos', 'buenos días', 'buenas tardes', 'buenas noches']):
        return '¡Hola! ¿Cómo te encuentras?'

    elif any(word in user_input.lower() for word in ['bien', 'bien gracias a Dios', 'bien gracias a dios']):
        return 'Me alegro que estes bien, ¿De que tema te gustaria hablar hoy?'

    elif any(word in user_input.lower() for word in ['mal', 'horrible', 'decepcionado']):
        return 'Comprendo que te sientas mal, estoy aqui para escucharte y ayudarte, cuentame ¿por que te sientes mal?'


    # Expresar emociones
    elif any(word in user_input.lower() for word in ['estoy ansioso', 'ansioso', 'me siento ansioso']):
        return 'Entiendo. La ansiedad es una experiencia común. ¿Te gustaría hablar sobre lo que la está desencadenando?'


    elif 'estres' in user_input.lower():
        return 'Algunas causas del estres son fracaso, universidad, mucho trabajo. ¿En los ultimos dias has tenido alguno de estos problemas?'


    elif any(word in user_input.lower() for word in ['me siento solo', 'no tengo a nadie a mi lado']):
        return 'La soledad no siempre es mala, muchas veces nos ayuda a reflexionar y a encontrarnos a nosotros mismos. ¿Dime de que tema deseas hablar?'

    elif any(word in user_input.lower() for word in ['me siento triste', 'estoy deprimido']):
        return 'Lamento escuchar que te sientes así. ¿Puedes compartir más sobre lo que ha estado sucediendo?'

    # Manejo del estres
    elif any(word in user_input.lower() for word in ['cómo manejar el estrés', 'consejos para reducir el estrés']):
        return 'El manejo del estrés es importante. Algunas estrategias incluyen la práctica de la respiración profunda y el autocuidado. ¿Te gustaría más información?'

    # Prevenir el suicidio
    elif any(word in user_input.lower() for word in ['pensamientos suicidas', 'necesito ayuda urgente']):
        return 'Lo siento mucho que estés pasando por esto. Es crucial buscar ayuda de emergencia. Por favor, comunícate con una línea de prevención de suicidios o busca ayuda profesional de inmediato.'

    elif any(word in user_input.lower() for word in ['me quiero suicidar', 'mi vida es una mierda', 'me quiero morir']):
        return 'La vida es algo muy valioso, entiendo que te sientas mal pero yo estoy aqui para ayudarte. cuentame mas sobre lo que estas pasando y te brindare todo mi apoyo'


    # Tecnicas para lidiar con el estres
    elif any(word in user_input.lower() for word in ['cómo lidiar con el estrés', 'técnicas de afrontamiento']):
        return 'Hay diversas técnicas de afrontamiento, como la meditación, el ejercicio y la búsqueda de apoyo social. ¿Te gustaría más sugerencias personalizadas?'

    # Explorar emociones
    elif any(word in user_input.lower() for word in ['explorar emociones', 'autoconocimiento']):
        return 'Explorar tus emociones puede ser un viaje enriquecedor. ¿Te gustaría discutir más sobre tus sentimientos y experiencias?'

    # Gratitud y positivismo
    elif any(word in user_input.lower() for word in ['agradecimiento', 'cómo encontrar la positividad']):
        return 'Practicar la gratitud puede tener un impacto positivo. ¿Hay algo específico por lo que te sientas agradecido hoy?'

    # Respondiendo preguntas frecuentes
    elif any(word in user_input.lower() for word in ['cómo', 'qué', 'cuándo', 'dónde']):
        return 'Esa es una pregunta interesante. ¿Puedes proporcionar más detalles?'

    else:
        return 'Lo siento, no entiendo completamente. ¿Puedes proporcionar más información o formular tu pregunta de otra manera?'

# Funcion para guardar los mensajes del usuario
def save_chat_to_database(user_message, response):
    try:
        connection = connect_to_database(database='usuarios')
        if connection:
            save_chat_message(connection, user_id=0, message=user_message, response=response)  # Assuming user_id 0 for chatbot
            close_connection(connection)
    except Exception as e:
        print("Error saving chat message:", e)



if __name__ == '__main__':
    app.run(debug=True)
