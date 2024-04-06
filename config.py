import secrets

SECRET_KEY = secrets.token_hex(16)
WTF_CSRF_SECRET_KEY = secrets.token_hex(16)


# config.py

MAIL_SERVER = 'smtp.example.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@example.com'
MAIL_PASSWORD = 'your-email-password'
MAIL_DEFAULT_SENDER = 'your-email@example.com'
