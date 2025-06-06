from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from .IRsaKeyManager import IRsaKeyManager

class RsaKeyManager(IRsaKeyManager):
    def __init__(self):
        self._private_key = None
        self._public_key = None
        self.supported_key_sizes = [1024, 2048, 4096]

    def generate_keys(self, key_size: int):
        if key_size not in self.supported_key_sizes:
            raise ValueError(f"Unsupported key size: {key_size}. Supported sizes: {self.supported_key_sizes}")
        
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )
        self._public_key = self._private_key.public_key()
        # generated rsa key

    def load_private_key(self, filename: str, password: str = None):
        with open(filename, "rb") as f:
            pem_data = f.read()
        
        self._private_key = serialization.load_pem_private_key(
            pem_data,
            password=password.encode('utf-8') if password else None
        )
        self._public_key = self._private_key.public_key()
        # loading rsa keys

    def save_private_key(self, filename: str, password: str = None):
        if not self._private_key:
            raise ValueError("The private key was not generated or loaded.")
        
        encoding = serialization.Encoding.PEM
        format = serialization.PrivateFormat.PKCS8
        encryption_algorithm = serialization.NoEncryption()
        if password:
            encryption_algorithm = serialization.BestAvailableEncryption(password.encode('utf-8'))

        pem = self._private_key.private_bytes(
            encoding=encoding,
            format=format,
            encryption_algorithm=encryption_algorithm
        )
        with open(filename, "wb") as f:
            f.write(pem)


    def load_public_key(self, filename: str):
        with open(filename, "rb") as f:
            pem_data = f.read()

        self._public_key = serialization.load_pem_public_key(pem_data)


    def save_public_key(self, filename: str):
        if not self._public_key:
            raise ValueError("The public key was not generated or loaded.")

        pem = self._public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(filename, "wb") as f:
            f.write(pem)


    def get_public_key(self):
        if not self._public_key:
            raise ValueError("The public key is not available.")
        return self._public_key

    def get_private_key(self):
        if not self._private_key:
            raise ValueError("The private key is not available.")
        return self._private_key