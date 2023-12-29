from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

def encrypt(text, password):
    password = password.encode('utf-8')
    salt = b'salt_123'  # Change this salt to something unique for your application

    # Derive a key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(password))

    # Generate a random IV (Initialization Vector)
    iv = urlsafe_b64encode(os.urandom(16))

    # Encrypt the text using AES-GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(text.encode('utf-8')) + encryptor.finalize()

    # Combine IV and ciphertext, and encode as base64
    encrypted_data = iv + ciphertext
    return urlsafe_b64encode(encrypted_data)

def decrypt(encrypted_data, password):
    password = password.encode('utf-8')
    salt = b'salt_123'  # Use the same salt as in the encryption function

    # Derive a key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(password))

    # Decode the base64-encoded input
    encrypted_data = urlsafe_b64decode(encrypted_data)

    # Extract IV from the encrypted data
    iv = encrypted_data[:16]

    # Decrypt the ciphertext using AES-GCM
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

    return decrypted_text.decode('utf-8')
