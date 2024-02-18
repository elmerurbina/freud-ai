from flask import Flask, render_template

app = Flask(__name__)

# Sample profile data (replace this with actual data retrieval logic)
profile_data = {
    'file_path': r'C:\Users\elmer\PycharmProjects\Freud_AI\static\imagenes\perfil.jpg',
    'nombre': 'John Doe',
    'ubicacion': 'City, Country',
    'contacto': 'johndoe@example.com',
    'licencia': '123456',
    'estudios_academicos': 'Bachelor of Science in Computer Science',
    'keywords': 'Python, Flask, Web Development',
    'descripcion': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lobortis mi nec tristique suscipit.'
}

# Define a context processor to make profile_data available to all templates
@app.context_processor
def inject_profile_data():
    return dict(profile_data=profile_data)

@app.route('/perfil')
def view_profile():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True)
