
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')


app.secret_key = 'your_secret_key'


users = {
    'example_user': {'name': 'John Doe', 'profile_image_url': '/static/default_profile.png'}
}


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

    if any(word in user_input.lower() for word in ['bien', 'bien gracias a Dios', 'bien gracias a dios']):
        return 'Me alegro que estes bien, ¿De que tema te gustaria hablar hoy?'


    # Expresar emociones
    elif any(word in user_input.lower() for word in ['estoy ansioso', 'me siento ansioso']):
        return 'Entiendo. La ansiedad es una experiencia común. ¿Te gustaría hablar sobre lo que la está desencadenando?'

    if 'si' in user_input.lower():
        return 'Sí, la ansiedad puede tener diversas causas. Algunas de las causas comunes incluyen el estrés, cambios en la vida, problemas de salud, entre otros. ¿Cual crees que sea la causa que te esta afectando?'

    if 'estres' in user_input.lower():
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


if __name__ == '__main__':
    app.run(debug=True)
