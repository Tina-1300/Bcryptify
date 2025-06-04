from .ISymmetricCipher import ISymmetricCipher
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

class AesGcmCipher(ISymmetricCipher):
    def __init__(self, key: bytes):
        if len(key) not in (16, 24, 32):
            raise ValueError("The key must be 128, 192 or 256 bits")
        self.key = key
        self.aesgcm = AESGCM(key)

    def encrypt(self, plaintext: bytes) -> bytes:
        nonce = os.urandom(12)  # 96-bit nonce recommended
        ciphertext = self.aesgcm.encrypt(nonce, plaintext, None)
        return nonce + ciphertext 

    def decrypt(self, ciphertext: bytes) -> bytes:
        nonce = ciphertext[:12]
        actual_ct = ciphertext[12:]
        return self.aesgcm.decrypt(nonce, actual_ct, None)
