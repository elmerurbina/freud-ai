from flask import redirect, Flask, url_for, session, request
from oauthlib.oauth2 import WebApplicationClient
import requests

app = Flask(__name__)

# Initialize the client ID and other credentials
GOOGLE_CLIENT_ID = '512814388268-1db0c3s4gj5pjdljv9qa5h3ohrikb42n.apps.googleusercontent.com'
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Callback URL for Google OAuth
GOOGLE_REDIRECT_URI = 'http://127.0.0.1:5000/login/callback'

@app.route('/google-auth')
def google_auth():
    # Redirect to Google OAuth consent screen
    authorization_endpoint = 'https://accounts.google.com/o/oauth2/auth'
    url = client.prepare_request_uri(authorization_endpoint, redirect_uri=GOOGLE_REDIRECT_URI)
    return redirect(url)

@app.route('/login/callback')
def login_callback():
    return "Login callback received"

@app.route('/google-auth-callback')
def google_auth_callback():
    # Handle Google OAuth callback
    code = request.args.get('code')
    token_endpoint = 'https://oauth2.googleapis.com/token'
    token_url, headers, body = client.prepare_token_request(token_endpoint, authorization_response=request.url, redirect_url=GOOGLE_REDIRECT_URI)
    token_response = requests.post(token_url, headers=headers, data=body, auth=(GOOGLE_CLIENT_ID, 'your-client-secret'))
    client.parse_request_body_response(token_response.json())
    userinfo_endpoint = 'https://openidconnect.googleapis.com/v1/userinfo'
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    userinfo = userinfo_response.json()
    session['user'] = userinfo  # Save user info in session
    return redirect(url_for('chat'))
