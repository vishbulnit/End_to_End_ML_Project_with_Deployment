

class FileProcessingError(Exception):
    def __init__(self, message, filename, lineno):
        super().__init__(message)
        self.filename = filename
        self.lineno = lineno

    def __str__(self):
        return f"{self.message} in {self.filename} at line {self.lineno}"


try:
    raise FileProcessingError("Syntax error", "example.txt", 13)
except FileProcessingError as e:
    print(f"Caught an error: {e}")