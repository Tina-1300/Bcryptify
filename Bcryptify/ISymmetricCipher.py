from abc import ABC, abstractmethod

class ISymmetricCipher(ABC):
    @abstractmethod
    def encrypt(self, plaintext: bytes) -> bytes:
        pass
    
    @abstractmethod
    def decrypt(self, ciphertext: bytes) -> bytes:
        pass

