
## this file is to check few use cases

class MyCustomError(Exception):
    """Exception raised for custom error in the application."""

    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
    
def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 400)
    return a / b


try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"Caught an error: {e}")

'''
import os
from datetime import datetime
import sys

# Joining directory and file names
path1 = os.path.join("my_folder", "my_file.txt")
print(f"Path 1: {path1}")

# Joining multiple directory levels
path2 = os.path.join("base_dir", "sub_dir", "another_sub_dir", "final_file.csv")
print(f"Path 2: {path2}")

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print(f"The current working directory is: {current_directory}")

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
print(logs_path)

'''
