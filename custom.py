from Join_Rasa_Python import get_combined_data
import random
from db import fetch_data_from_information_table


combined_data = get_combined_data()

def greeting(saludar):
    if saludar in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][saludar])

    else:
        response = fetch_data_from_information_table

        return response


def sad(estado_animo_triste):
    if estado_animo_triste in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estado_animo_triste])
    else:
        response = fetch_data_from_information_table
        return response


def anxiety_state(estado_animo_ansioso):
    if estado_animo_ansioso in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estado_animo_ansioso])
    else:
        response = fetch_data_from_information_table

        return response


def happy(estado_animo_feliz):
    if estado_animo_feliz in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estado_animo_feliz])

    else:
        response = fetch_data_from_information_table

        return response


def stress(estres):
    if estres in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estres])

    else:
        response = fetch_data_from_information_table

        return response

def anxiety(ansiedad):
    if ansiedad in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][ansiedad])

    else:
        response = fetch_data_from_information_table

        return response

def depression(depresion):
    if depresion in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][depresion])

    else:
        response = fetch_data_from_information_table

        return response


def trauma(estres_post_traumatico):
    if estres_post_traumatico in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][estres_post_traumatico])

    else:
        response = fetch_data_from_information_table

        return response


def addiction(adiccion):
    if adiccion in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][adiccion])

    else:
        response = fetch_data_from_information_table

        return response


def insomnia(insomnio):
    if insomnio in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][insomnio])

    else:
        response = fetch_data_from_information_table

        return response


def narcolepsy(narcolepsia):
    if narcolepsia in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][narcolepsia])

    else:
        response = fetch_data_from_information_table

        return response


def fobias(Fobias):
    if Fobias in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][Fobias])

    else:
        response = fetch_data_from_information_table

        return response


def bulimia(Bulimia):
    if Bulimia in combined_data.get('responses', {}):
        response = random.choice(combined_data['responses'][Bulimia])

    else:
        response = fetch_data_from_information_table

        return response








