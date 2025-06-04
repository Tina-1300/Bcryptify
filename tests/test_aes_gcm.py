import sys
import os
import unittest

# python -m unittest test_aes_gcm.py

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from Bcryptify.aes_gcm import AesGcmCipher

# Unit Testing
import unittest
import os
from Bcryptify.aes_gcm import AesGcmCipher

class TestAesGcmCipher(unittest.TestCase):

    def setUp(self):
        # Generating a 256-bit (32 bytes) key
        self.key = os.urandom(32)
        self.cipher = AesGcmCipher(self.key)
        self.plaintext = "Message secret à chiffrer".encode('utf-8')

    def test_encrypt_decrypt(self):
        ciphertext = self.cipher.encrypt(self.plaintext)
        self.assertIsInstance(ciphertext, bytes)

        # The ciphertext must be longer than the plaintext (nonce + ciphertext)
        self.assertGreater(len(ciphertext), len(self.plaintext))
        
        decrypted = self.cipher.decrypt(ciphertext)
        self.assertEqual(decrypted, self.plaintext)

    def test_different_ciphertexts_for_same_plaintext(self):
        ciphertext1 = self.cipher.encrypt(self.plaintext)
        ciphertext2 = self.cipher.encrypt(self.plaintext)

        # Even plaintext, ciphertexts must be different because of the random nonce
        self.assertNotEqual(ciphertext1, ciphertext2)

    def test_invalid_key_length(self):
        # Invalid key for AESGCM (must be 128, 192 or 256 bits)
        with self.assertRaises(ValueError):
            AesGcmCipher(b"short_key")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)