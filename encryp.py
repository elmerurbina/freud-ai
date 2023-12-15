from cryptography.fernet import Fernet

# Se genera la clave para encriptar
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Se carga la clave desde el documento que se creo en el paso anterior
def load_key():
    return open("secret.key", "rb").read()

# Encripta la informacion
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Desencripta la informacion para poder ser accedida
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

