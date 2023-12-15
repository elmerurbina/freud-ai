from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static')



@app.route('/chatBot')
def chat():
    return render_template('ChatBot.html')

if __name__ == '__main__':
        app.run(debug=True)




