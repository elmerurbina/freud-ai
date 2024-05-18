from flask import Flask, request, render_template, jsonify
from db import valid_code

app = Flask(__name__)

@app.route('/aseguradora', methods=['GET', 'POST'])
def aseguradora():
    if request.method == 'POST':
        codigo = request.form['codigo']
        if valid_code(codigo):
            # If code is valid, render the registration form
            return render_template('codigoAseguradora.html', display_credenciales=True)
        else:
            # If code is invalid, display error message and stay on the same page
            return render_template('codigoAseguradora.html', codigo_error="Código incorrecto. Inténtalo de nuevo.")
        # If method is GET or if code validation failed, display the initial page
    return render_template('codigoAseguradora.html', display_credenciales=False)

@app.route("/check_code_validity", methods=["POST"])
def check_code_validity():
    codigo = request.json.get("codigo")
    if valid_code(codigo):
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})

if __name__ == '__main__':
    app.run(debug=True)
