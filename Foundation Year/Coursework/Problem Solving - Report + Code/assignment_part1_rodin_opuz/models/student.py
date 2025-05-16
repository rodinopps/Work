# Rodin Opuz - student.py
# Task 1
# Week 3

# This is the class Student and defines the class.
class Student: 
    # This creates a constructor method for the class Student with self, name, student_id, course and year as parameters.
    def __init__(self, name, student_id, course, year):
        self.name = name # This sets the name of the student.
        self.__student_id = student_id # This sets the private student ID.
        self.course = course # This sets the course of the student.
        self.year = year # This sets the year of the student.
    
    # This is a getter method for the student id attribute which is private. Getter returns the value of a class attribute.
    def get_student_id(self):
        return self.__student_id # This returns the value of the student id attribute.
    
    # This is a setter method for the private student id attribute where it updates it.
    def set_student_id(self, new_id):
        self.__student_id = new_id # This updates the student id with a new id.

    # This is a method that updates the course the student is in.
    def update_course(self, new_course):
        self.course = new_course # This updates the course with a new course.

    # This is a method that returns the details of the student.
    def get_details(self):
        # This returns the student information.
        return f"Name - {self.name}, ID - {self.__student_id}, Course - {self.course}, Year - {self.year}"
    
'''
# Test
student1 = Student("Rodin", 18378, "CS", 2025)
print(student1.get_details())
'''