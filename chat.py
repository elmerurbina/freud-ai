from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'  # Set a secret key for session security

# Sample user data
users = {
    'example_user': {'name': 'John Doe', 'profile_image_url': '/static/default_profile.png'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    # Check if the user is logged in
    if 'username' not in session:
        return redirect(url_for('index'))

    # Get user data from the session or database
    username = session['username']
    user_data = users.get(username, {'name': 'Guest', 'profile_image_url': '/static/default_profile.png'})

    # Pass user data to the template
    return render_template('chat.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
