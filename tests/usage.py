import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


from Bcryptify.aes_gcm import AesGcmCipher

# --- Configuration ---

# Clé AES 256 bits (32 bytes)
key = b'\xcd_\x8d\xfd1E\xd4\xe3uj\xee_\x1dj\x9c\x07\xa3\x13\x95\x96\x10\xa6\xf3\rb\xc0\x08\xde\xfa\xb6\x99\xc9'

# Initialisation du cipher AES-GCM
aes_gcm = AesGcmCipher(key)

#message = "je suis la essey de m'attrapper ààà merde".encode("utf-8")


#message_cipher = aes_gcm.encrypt(message)

#print(message_cipher)

#decrypt_message = aes_gcm.decrypt(message_cipher)

#print()

#print(decrypt_message.decode('utf-8'))

# -----------------------------

# Chiffre un fichier et le déchiffre


def read_file(filename: str) -> bytes:
    with open(filename, "rb") as f:
        return f.read()

def write_file(filename: str, data: bytes) -> None:
    with open(filename, "wb") as f:
        f.write(data)

def encrypt_file(filepath: str) -> None:
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    data = read_file(filepath)
    encrypted = aes_gcm.encrypt(data)

    encrypted_filepath = filepath + ".lock"
    write_file(encrypted_filepath, encrypted)

    os.remove(filepath) 
    print(f"File encrypted in {encrypted_filepath} and original file deleted.")

def decrypt_file(encrypted_filepath: str) -> None:
    if not encrypted_filepath.endswith(".lock"):
        raise ValueError("The decrypted file must have the extension '.lock'.")

    if not os.path.isfile(encrypted_filepath):
        raise FileNotFoundError(f"The file {encrypted_filepath} does not exist.")

    data = read_file(encrypted_filepath)
    decrypted = aes_gcm.decrypt(data)

    original_filepath = encrypted_filepath[:-5] 
    write_file(original_filepath, decrypted)

    os.remove(encrypted_filepath)
    print(f"Decrypted file in {original_filepath} and encrypted file deleted.")

# Example of use

file_path = os.path.join(BASE_DIR, "chap 12.pdf")
encrypt_file(file_path)
decrypt_file(file_path + ".lock")