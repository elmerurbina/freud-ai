
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/clinicas')
def clinicas():
    return render_template('clinicas.html')

if __name__ == '__main__':
    app.run(debug=True)
