# Rodin Opuz - undergraduate.py
# Task 2
# Week 4

# This imports the Student class from student.py file.
from models.student import Student

# This defines a subclass Undergraduate. It inherits from the Student class
class Undergraduate(Student):
    # This creates a constructor method for the subclass Undergraduate.
    def __init__(self, name, student_id, course, year, minor):
        super().__init__(name, student_id, course, year) # This calls the parent Student class to set the name, ID, course and year.
        self.minor = minor # Sets the minor.
    
    # This gets the details about a student.
    def get_details(self):
        student_details = super().get_details() # This gets the details of the student from Student.
        return f"{student_details}, Minor - {self.minor}" # This adds the minor.