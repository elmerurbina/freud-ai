from flask import Flask, jsonify

app = Flask(__name__)

# Sample profile data
profile = {
    'photo': 'https://example.com/photo.jpg',
    'license': '12345',
    'nombre': 'John Doe',
    'direccion': '123 Main St, City, Country',
    'descripcion': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'keywords': ['Lorem', 'ipsum', 'dolor'],
    'contacto': 'john@example.com',
    'estudios_academicos': 'Bachelor of Science in Computer Science'
}

@app.route('/profile_data')
def get_profile_data():
    return jsonify(profile)

if __name__ == '__main__':
    app.run(debug=True)
