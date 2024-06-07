from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    # Here you can handle the message, e.g., save it to a database
    return jsonify({"status": "success", "message": message})

if __name__ == '__main__':
    app.run(debug=True)
