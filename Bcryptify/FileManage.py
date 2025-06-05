

class FileManage:

    def __init__(self):
        self.extension = ".key"
    
    def read_file_key(self, filename: str) -> bytes:
        with open(filename + self.extension , "rb") as f:
            return f.read()
        
    def write_file_key(self, filename: str, data: bytes) -> None:
        with open(filename + self.extension, "wb") as f:
            f.write(data)

    def write_file(self, filename: str, data: bytes) -> None:
        with open(filename, "wb") as f:
            f.write(data)

    def read_file(self, filename: str) -> bytes:
        with open(filename , "rb") as f:
            return f.read()
    

        