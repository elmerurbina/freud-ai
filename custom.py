import random
from db import save_chat_message, close_connection, connect_to_database, fetch_data_from_information_table
from Join_Rasa_Python import get_combined_data
from chat import get_chatbot_response

# Acceder a los datas del Rasa Project
combined_data = get_combined_data()

# Establece la conexion con la base de datos
connection = connect_to_database()

# Metodos para cada intencion
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

def chatbot_response(user_input):
    # Check for predefined responses first
    response = get_chatbot_response(user_input)
    if response:
        return response
    # Call the appropriate function based on user input

    if 'narcolepsia' in user_input.lower():
        response = narcolepsy(user_input)

    elif 'fobias' in user_input.lower():
        response = fobias(user_input)

    elif 'bulimia' in user_input.lower():
        response = bulimia(user_input)

    elif 'insomnia' in user_input.lower():
        response = insomnia(user_input)

    elif 'stress' in user_input.lower():
        response = stress(user_input)

    elif 'ansiedad' in user_input.lower():
        response = anxiety(user_input)

    elif 'estado_ansiedad' in user_input.lower():
        response = anxiety_state(user_input)

    elif 'estres_traumatico' in user_input.lower():
        response = trauma(user_input)

    elif 'feliz' in user_input.lower():
        response = happy(user_input)

    elif 'triste' in user_input.lower():
        response = sad(user_input)

    elif 'adiccion' in user_input.lower():
        response = addiction(user_input)

    elif 'depresion' in user_input.lower():
        response = depression(user_input)

    else:
        response = "Lo siento. No puedo entender lo que me quieres decir."
    return response

def handle_user_message(user_id, message):
    # Process the user message and get the appropriate response
    response = process_message(message)

    # Guardar los mensajes del usuario en la base de datos
    connection = connect_to_database(database='usuarios')  # Conectar a la bd
    if connection:
        save_chat_message(connection, user_id, message, response)
        close_connection(connection)  # Cierra la conexion

    return response

def process_message(message):

    return "Response to user message"
close_connection(connection)
