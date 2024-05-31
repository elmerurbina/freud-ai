from oauthlib.oauth2 import WebApplicationClient
from flask import Flask, session, redirect, render_template, url_for, request
import requests
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# Initialize the client ID and other credentials
GOOGLE_CLIENT_ID = '512814388268-1db0c3s4gj5pjdljv9qa5h3ohrikb42n.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'
GOOGLE_REDIRECT_URI = 'http://127.0.0.1:5000/login/callback'

client = WebApplicationClient(GOOGLE_CLIENT_ID)

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

@app.route('/google-auth')
def google_auth():
    if 'user' in session:
        return redirect(url_for('chat'))  # Redirect to chat if user is already authenticated
    else:
        google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
        authorization_endpoint = google_provider_cfg['authorization_endpoint']
        request_uri = client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri=GOOGLE_REDIRECT_URI,
            scope=['openid', 'email', 'profile']
        )
        return redirect(request_uri)

@app.route('/login/callback')
def login_callback():
    code = request.args.get('code')
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg['token_endpoint']
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=GOOGLE_REDIRECT_URI,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET)
    )
    client.parse_request_body_response(token_response.text)
    userinfo_endpoint = google_provider_cfg['userinfo_endpoint']
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    userinfo = userinfo_response.json()
    session['user'] = userinfo
    return redirect(url_for('chat'))


if __name__ == '__main__':
    app.run(debug=True)