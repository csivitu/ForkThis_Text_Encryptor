from cryptography.fernet import Fernet, InvalidToken
import base64
from PIL import Image
from io import BytesIO
def image_to_bytes(image_path="test.jpg"):
    try:
        with open(image_path,"rb") as imageFile:
            image_bytes=imageFile.read()
        return image_bytes
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def generate_key_str() :
    return(Fernet.generate_key().decode())

def encrypt_message(message: str, key: str) -> str:
    """Encrypts a message using the provided key."""
    try:
        f = Fernet(key.encode())
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode()
    except (ValueError, TypeError):
        return "ERROR: Invalid Key for Encryption."
    

def encrypt_image(key:str)->str:
    try:
        f = Fernet(key.encode())
        encrypted_bytes=f.encrypt(image_to_bytes())
        with open("test.jpg", 'rb') as file:
                image_data = file.read()    
        encrypted_data = Fernet.encrypt(image_data)
        encrypted_path = "test" + '.enc'
        with open(encrypted_path, 'wb') as file:
            file.write(encrypted_data)

        return "work"
    except (ValueError, TypeError):
        return "ERROR: Invalid Key for Encryption."
    
from cryptography.fernet import Fernet, InvalidToken



def decrypt_message(encrypted_message: str, key: str) -> str:
    f = Fernet(key.encode())
    decrypted_message = f.decrypt(encrypted_message.encode())
    return decrypted_message.decode()