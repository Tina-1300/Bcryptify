from abc import ABC, abstractmethod


class IAsymmetricCipher(ABC):
    @abstractmethod
    def encrypt(self, plaintext: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: bytes) -> bytes:
        pass
