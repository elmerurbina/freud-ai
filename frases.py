import random
from flask import Flask, render_template, request, jsonify, flash
from plyer import notification
import pyttsx3
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set your secret key for flashing messages

# Mock data for categories and phrases
categories = [
    'general', 'soledad', 'estres', 'motivacion', 'ansiedad',
    'celebres', 'depresion', 'alimentacion', 'dormir', 'adicciones',
    'suicidio', 'humor', 'procrastinacion'
]

def random_phrase(category):
    with open('frases.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        categories_and_phrases = {}

        # Split content by category
        category_blocks = content.split('[')[1:]
        for block in category_blocks:
            parts = block.split(']')
            cat_name = parts[0].strip().lower()
            cat_phrases = [phrase.strip() for phrase in parts[1].strip().split('\n') if phrase.strip()]
            categories_and_phrases[cat_name] = cat_phrases

    return random.choice(categories_and_phrases.get(category, ['No se encontraron frases en esta categoria.']))

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Duration in seconds
    )

    if message:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.say(message)
        engine.runAndWait()

def send_notification(category):
    phrase = random_phrase(category)
    show_notification("Freud AI", phrase)

scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/notificaciones', methods=['GET', 'POST'])
def notificaciones():
    if request.method == 'POST':
        selected_categories = request.form.getlist('category')  # Get selected categories as a list
        time_interval = int(request.form.get('time', 8))  # Get selected time interval from radio button

        for category in selected_categories:
            job_id = f'{category}_job_{time_interval}h'
            scheduler.add_job(send_notification, 'interval', hours=time_interval, args=[category], id=job_id)

        flash('Notificaciones configuradas exitosamente', 'success')  # Flash success message
        return jsonify({'status': 'Configuracion exitosa!', 'categories': selected_categories, 'time_interval': time_interval})

    return render_template('notificaciones.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
