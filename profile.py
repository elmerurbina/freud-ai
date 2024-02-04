from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store user data in memory (replace with a database in a real-world application)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    name = request.form['name']
    # Add more fields as needed

    # Handle image upload
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        # Handle image storage, e.g., save to a folder or a cloud storage service

    # Save user data (replace with database logic)
    users[username] = {'name': name, 'profile_image_url': 'path_to_image'}

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

