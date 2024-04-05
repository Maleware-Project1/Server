from cryptography.fernet import Fernet

def create_Fernet_key():
    key = Fernet.generate_key()
    return key