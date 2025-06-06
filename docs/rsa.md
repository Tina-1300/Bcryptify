# Example RSA


```python
import os
from Bcryptify.RsaKeyManager import RsaKeyManager
from Bcryptify.rsa import RsaCipher

key_manager = RsaKeyManager()

try:
    key_manager.generate_keys(2048)
except ValueError as e:
    print(e)
    return


private_key_filename = "rsa_private_key.pem"
public_key_filename = "rsa_public_key.pem"

password = "a_strong_password"


key_manager.save_private_key(private_key_filename, password=password)
key_manager.save_public_key(public_key_filename)

print("\n--- Encryption/decryption test with generated keys ---")


rsa_encryptor = RsaCipher(public_key=key_manager.get_public_key())

rsa_decryptor = RsaCipher(private_key=key_manager.get_private_key())

message = b"This is a top secret message for RSA."
print(f"Original post: {message.decode()}")


encrypted_message = rsa_encryptor.encrypt(message)
print(f"Encrypted message (in hex): {encrypted_message.hex()}")


decrypted_message = rsa_decryptor.decrypt(encrypted_message)
print(f"Decrypted message: {decrypted_message.decode()}")

assert message == decrypted_message
print("Encryption/decryption test successful !\n")

print("--- Key loading test and usage ---")


new_key_manager = RsaKeyManager()
new_key_manager.load_private_key(private_key_filename, password=password)


other_party_key_manager = RsaKeyManager()
other_party_key_manager.load_public_key(public_key_filename)


other_message = b"Hi, message from another person!"
print(f"Message from the other party: {other_message.decode()}")
    
other_rsa_encryptor = RsaCipher(public_key=other_party_key_manager.get_public_key())
encrypted_other_message = other_rsa_encryptor.encrypt(other_message)
print(f"Message encrypted by the other party (in hex): {encrypted_other_message.hex()}")


decrypted_other_message = RsaCipher(private_key=new_key_manager.get_private_key()).decrypt(encrypted_other_message)
print(f"Message decrypted by the loaded private key: {decrypted_other_message.decode()}")
    
assert other_message == decrypted_other_message
print("Inter-key communication test passed !\n")
```