from flask import Flask, render_template, request, session, url_for, redirect
from logout import logout
from config import SECRET_KEY, cache
from nlp import preprocessed_texts, tfidf_vectorizer, model
from NumPy_Array import ask_questions, evaluate_answers
from db import fetch_data_from_information_table, insert_chat_message, get_user_chat_history
import random
from encryp import encrypt_message, decrypt_message
import Join_Rasa_Python
from Join_Rasa_Python import intent_logic
from rasa.nlu.model import Interpreter


app = Flask(__name__, static_url_path="/static")

combined_data = Join_Rasa_Python.get_combined_data()

app.config ['SECRET_KEY'] = SECRET_KEY

conversation_history = []

# Modelo de NLP
@app.route('/', methods=['GET', 'POST'])
def chatbot():

    nlu_result = None
    bot_response = None
    nlu_intent = None


    if request.method == 'POST':
        user_input = request.form['user_input']
        conversation_history.append(f"You: {user_input}")
        encrypted_user_input = encrypt_message(user_input, secret_key)

        cached_response = cache.get(user_input)
        if cached_response is not None:
            bot_response = decrypt_message(cached_response, secret_key)

        else:
            nlu_result = interpreter.parse(user_input)
            nlu_intent = nlu_result['intent']['name']
            nlu_entities = nlu_result['entities']

        if nlu_result in intent_logic:
            bot_response = intent_logic[nlu_intent]()

        else:
            preprocessed_input = preprocessed_texts(encrypted_user_input)
            tfidf_vector = tfidf_vectorizer.transform([preprocessed_input])
            prediction = model.predict(tfidf_vector)[0]
            bot_responses = fetch_data_from_information_table(user_input)

        if bot_response:
            bot_response = random.choice(bot_response)
        else:
            bot_response = "I am in a phase of experimentation, could you modify your statement, please!"

            encrypted_bot_response = encrypt_message(bot_response, secret_key)

            cache.set(encrypted_user_input, encrypted_bot_response)

        conversation_history.append(f"Bot: {bot_response}")

        if 'user_id' in session:
            user_id = session ['user_id']

            insert_chat_message(user_id, encrypted_user_input)


    return render_template('ChatBot.html', conversation=conversation_history)

@app.route('/chats_history')
def chats_history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']

    chats_history = get_user_chat_history(user_id)

    return render_template('ChatBot.html', chats_history=chats_history)


# Evaluaciones psicologicas
@app.route('/psychological_evaluation', methods=['GET', 'POST'])
def psychological_evaluation():
    if request.method == 'POST':
        answers_dict = ask_questions()
        result = evaluate_answers(answers_dict)
        return render_template('ChatBot.html', result=result)

    return render_template('ChatBot.html')

@app.route('/logout')
def logout_route():
    return logout()


if __name__ == '__main__':
    app.run(debug=True)







