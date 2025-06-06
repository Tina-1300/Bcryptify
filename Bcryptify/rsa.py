from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from .IAsymmetricCipher import IAsymmetricCipher
from cryptography.hazmat.primitives.asymmetric import rsa

class RsaCipher(IAsymmetricCipher):

    def __init__(self, public_key=None, private_key=None):
        if public_key is None and private_key is None:
            raise ValueError("At least one key (public or private) must be provided.")
        
        self._public_key = public_key
        self._private_key = private_key

    def encrypt(self, plaintext: bytes) -> bytes:
        if not self._public_key:
            raise ValueError("Unable to encrypt: public key is not available.")
        
        ciphertext = self._public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt(self, ciphertext: bytes) -> bytes:
        if not self._private_key:
            raise ValueError("Unable to decrypt: Private key is not available.")
        
        plaintext = self._private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext