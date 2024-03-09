from flask import Flask, redirect, url_for, jsonify, request
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Google OAuth blueprint
google_bp = make_google_blueprint(
    client_id="http://512814388268-1db0c3s4gj5pjdljv9qa5h3ohrikb42n.apps.googleusercontent.com",
    client_secret="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",
    redirect_to="login_callback"
)
app.register_blueprint(google_bp, url_prefix="/login")



@app.route("/login/callback")
def login_callback():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text

    # Use resp.json() to get user information
    # Implement your logic to handle user login or registration here

    return redirect(url_for("chat"))  # Redirect to chat interface after successful login


@app.route("/google_login", methods=['POST'])
def google_login():
    id_token = request.form['id_token']

    # Verify the ID token with Google
    # You can use libraries like google-auth or pyjwt to verify the token
    # Example verification logic should be added here

    # If the token is valid, proceed with the login process
    # You can get user information from the ID token
    # For example, idinfo['email'], idinfo['name'], etc.
    # Implement your logic to handle the user login or registration here

    return jsonify({'status': 'success'})
