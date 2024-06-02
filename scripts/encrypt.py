from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    return key

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, 'rb').read()

def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

if __name__ == "__main__":
    key = generate_key()
    save_key(key, 'encryption.key')
    print(f"Encryption key saved to 'encryption.key'")