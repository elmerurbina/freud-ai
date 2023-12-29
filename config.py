import secrets

SECRET_KEY = secrets.token_hex(16)
WTF_CSRF_SECRET_KEY = secrets.token_hex(16)
