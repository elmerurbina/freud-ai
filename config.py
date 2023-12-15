
from flask import Flask
from flask_caching import Cache
from flask_session import Session
import redis
from datetime import timedelta


app = Flask(__name__)

# Generacion de la clave secreta


# Configuracion de Cache, redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_KEY_PREFIX'] = 'my_cache_'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0

# Se inicializa el sistema de Cache
cache = Cache(app)



# Implementacion de logout despues de 30 minutos de inactividad

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'myapp:'
app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379, db=0)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['SESSION_COOKIE_SECURE'] = True

# Inicializacion de flask-session
session = Session(app)
