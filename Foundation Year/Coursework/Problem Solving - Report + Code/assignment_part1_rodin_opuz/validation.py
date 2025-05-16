# Rodin Opuz - validation.py

# This imports the custom exceptions from the file used for validation.
from exceptions import InvalidIDException, DuplicateStudentIDException

# This creates a function that validates the ID and takes the student id and students list as parameters.
def validate_student_id(student_id, students):
    # This checks if the student ID is not all numbers and if the length is not 9 digits.
    if not student_id.isdigit() or len(student_id) != 9:
        # If is invalid and meets the criteria above, it will raise the custom exception for invalid ID exception.
        raise InvalidIDException()
    # This loops through all the existing students to check for duplicate IDs.
    for i in students:
        if i.get_student_id() == student_id: # If the student ID matches it, it will raise the exception.
            raise DuplicateStudentIDException() # Duplicate ID exception.