import os

class GenKeyAesGcm:
    
    @staticmethod
    def creat_key_16():
        return os.urandom(16)
    
    @staticmethod
    def creat_key_24():
        return os.urandom(24)
    
    @staticmethod 
    def creat_key_32():
        return os.urandom(32)