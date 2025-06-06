from abc import ABC, abstractmethod

class IRsaKeyManager(ABC):
    
    @abstractmethod
    def generate_keys(self, key_size: int):
        pass

    @abstractmethod
    def load_private_key(self, filename: str, password: str = None):
        pass

    @abstractmethod
    def save_private_key(self, filename: str, password: str = None):
        pass

    @abstractmethod
    def load_public_key(self, filename: str):
        pass

    @abstractmethod
    def save_public_key(self, filename: str):
        pass
    
    @abstractmethod
    def get_public_key(self):
        pass
    
    @abstractmethod
    def get_private_key(self):
        pass