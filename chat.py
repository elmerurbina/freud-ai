from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'  # Set a secret key for session security

# Sample user data
users = {
    'example_user': {'name': 'John Doe', 'profile_image_url': '/static/default_profile.png'}
}


@app.route('/chat')
def chat():
    return render_template('chat.html')


    # Pass user data to the template



@app.route('/process_message', methods=['POST'])
def process_message():
    user_message = request.json.get('message', '')

    # Process user input and generate response
    response = get_chatbot_response(user_message)

    return jsonify({'response': response})

def get_chatbot_response(user_input):
    # Add your logic here to analyze user input and generate a relevant response
    if 'hola' in user_input.lower():
        return '¡Hola! ¿En qué puedo ayudarte hoy?'
    elif 'estoy ansioso' in user_input.lower():
        return 'Entiendo. ¿Puedes contarme más sobre lo que te preocupa?'
    else:
        return 'Lo siento, no entiendo. ¿Puedes reformular tu pregunta?'

# ... (remaining Flask code)


if __name__ == '__main__':
    app.run(debug=True)
