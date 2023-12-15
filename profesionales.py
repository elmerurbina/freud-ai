from flask import Flask, render_template
from flask import Blueprint
app = Flask (__name__, static_url_path='/static')

perfil = [


]

profesionales_blueprint = Blueprint('profesional', __name__)

@app.route('/profesionales')
def profesionals():
    return render_template('profesionales.html', perfiles=perfil)



if __name__ == '__main__':
    app.run(debug=True)


