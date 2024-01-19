import random
import numpy as np
import pyttsx3
from win10toast import ToastNotifier








humor = {
        "1": "¿Cuál es el animal más antiguo? La cebra, ¡porque está en blanco y negro!",

}



def random_phrase():
    categories = [
        'general', 'soledad', 'estres', 'motivacion', 'ansiedad', 'celebres', 'depresion', 'alimentacion',
        'dormir', 'adicciones', 'suicidio', 'humor', 'procrastinacion'
    ]

    random_category = np.random.choice(categories)

    if random_category == 'general':
        phrases = general
    elif random_category == 'soledad':
        phrases = soledad
    elif random_category == 'estres':
        phrases = estres
    elif random_category == 'motivacion':
        phrases = motivacion
    elif random_category == 'alimentacion':
        phrases = alimentacion
    elif random_category == 'ansiedad':
        phrases = ansiedad
    elif random_category == 'humor':
        phrases = humor
    elif random_category == 'procrastinacion':
        phrases = procrastinacion
    else:
        print(f"No se encontraron frases en esta categoría {random_category}")
        return ""

    if phrases:
        phrase_ids = list(phrases.keys())
        random_id = random.choice(phrase_ids)
        return phrases[random_id]
    else:
        print(f"No se encontraron frases en esta categoría: {random_category}")
        return ""

def show_notification(title, message):
    toaster = ToastNotifier()

    if not message:
        message = "No se encontraron frases en esta categoría."

    toaster.show_toast(title, message, duration=10)

    if message:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.say(message)
        engine.runAndWait()

# Call random_phrase once and use the result throughout
phrase = random_phrase()
print(f"Random Phrase: {phrase}")

show_notification("Freud AI", phrase)