# Rodin Opuz - exceptions.py
# Task 4
# Week 5

# Exception is a built in class fior Python.
# This is a custom exception for student IDs that are invalid.
class InvalidIDException(Exception):
    def __init__(self, message="Invalid student ID. "): # This creates a constructor method with a default message for exception handling.
        super().__init__(message) # This calls the message.

# This is a custom exception for student IDs that are duplicates.
class DuplicateStudentIDException(Exception):
    def __init__(self, message = "Student ID already exists. "): # This creates a constructor method with a default message for exception handling.
        super().__init__(message) # This calls the message.