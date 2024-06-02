import os
from getpass import getpass
from dotenv import load_dotenv
from scripts.encrypt import generate_key, save_key, load_key, encrypt_data

def load_env_variables():
    load_dotenv()

def set_env_variable(key, value):
    with open('.env', 'a') as f:
        f.write(f'{key}={value}\n')

def get_env_variable(key):
    load_dotenv()
    return os.getenv(key)

def prompt_for_config():
    ssc_url = input("Enter SSC URL: ")
    set_env_variable('SSC_URL', ssc_url)

    username = input("Enter SSC Username: ")
    password = getpass("Enter SSC Password: ")

    # Generate and set token
    from scripts.generate_token import generate_auth_token
    auth_token = generate_auth_token(ssc_url, username, password)

    # Encrypt the token
    key = generate_key()
    save_key(key, 'encryption.key')
    encrypted_token = encrypt_data(auth_token, key)
    set_env_variable('SSC_AUTH_TOKEN', encrypted_token.decode())

    print("Configuration completed.")

if __name__ == "__main__":
    prompt_for_config()