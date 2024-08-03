from cryptography.fernet import Fernet

# storing key in file after generation
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# loading key
def load_key():
    return open("secret.key", "rb").read()

# encrypting
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypting
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Key
generate_key()

# Encrypt the name "Tanvir Singh Aulakh"
name_to_encrypt = "Tanvir Singh Aulakh"
encrypted_name = encrypt_message(name_to_encrypt)
print(f"Encrypted Name: {encrypted_name}")

# Decrypt the name
decrypted_name = decrypt_message(encrypted_name)
print(f"Decrypted Name: {decrypted_name}")
