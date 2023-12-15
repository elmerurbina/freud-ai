from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static')



@app.route('/expediente')
def verExpediente():
    return render_template('verExpediente.html')

if __name__ == '__main__':
        app.run(debug=True)




