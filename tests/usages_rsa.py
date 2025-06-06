
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


from Bcryptify.RsaKeyManager import RsaKeyManager
from Bcryptify.rsa import RsaCipher


def run_rsa_example():
    key_manager = RsaKeyManager()

    try:
        key_manager.generate_keys(2048)
    except ValueError as e:
        print(e)
        return


    #private_key_filename = "rsa_private_key.pem"
    #public_key_filename = "rsa_public_key.pem"
    password = "a_strong_password"

    private_key_filename = os.path.join(BASE_DIR, "rsa_private_key.pem")
    public_key_filename = os.path.join(BASE_DIR, "rsa_public_key.pem")

    #key_manager.save_private_key(private_key_filename, password=password)
    #key_manager.save_public_key(public_key_filename)

    print("\n--- Test de chiffrement/déchiffrement avec les cles generees ---")


    rsa_encryptor = RsaCipher(public_key=key_manager.get_public_key())
    rsa_decryptor = RsaCipher(private_key=key_manager.get_private_key())

    message = b"Ceci est un message tres secret pour RSA."
    print(f"Message original: {message.decode()}")


    encrypted_message = rsa_encryptor.encrypt(message)
    print(f"Message chiffre (en hex): {encrypted_message.hex()}")


    decrypted_message = rsa_decryptor.decrypt(encrypted_message)
    print(f"Message dechiffre: {decrypted_message.decode()}")

    assert message == decrypted_message
    print("Test de chiffrement/dechiffrement reussi !\n")

    print("--- Test de chargement de cles et utilisation ---")


    new_key_manager = RsaKeyManager()
    new_key_manager.load_private_key(private_key_filename, password=password)


    other_party_key_manager = RsaKeyManager()
    other_party_key_manager.load_public_key(public_key_filename)



    other_message = b"Salut, message d'une autre personne!"
    print(f"Message de l'autre partie: {other_message.decode()}")
    
    other_rsa_encryptor = RsaCipher(public_key=other_party_key_manager.get_public_key())
    encrypted_other_message = other_rsa_encryptor.encrypt(other_message)
    print(f"Message chiffre par l'autre partie (en hex): {encrypted_other_message.hex()}")


    decrypted_other_message = RsaCipher(private_key=new_key_manager.get_private_key()).decrypt(encrypted_other_message)
    print(f"Message dechiffre par la cle privee chargee: {decrypted_other_message.decode()}")
    
    assert other_message == decrypted_other_message
    print("Test de communication inter-cles reussi !\n")



if __name__ == "__main__":
    run_rsa_example()