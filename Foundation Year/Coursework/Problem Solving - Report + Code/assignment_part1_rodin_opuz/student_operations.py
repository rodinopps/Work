# Rodin Opuz - student_operations.py
# Task 3
# Week 2

# This imports Student from student file.
from models.student import Student
# This imports Undergraduate from undergraduate file.
from models.undergraduate import Undergraduate
# This imports custom exceptions.
from exceptions import InvalidIDException, DuplicateStudentIDException
# This imports the function that validates ID.
from validation import validate_student_id

# This is an empty list that stores student which are represented as objects.
students = []

# This adds a new student.
def add_student(name, student_id, course, year, minor = None):
    validate_student_id(student_id, students)

    # If the student has a minor study, it creates an Undergraduate object.
    if minor:
        student = Undergraduate(name, student_id, course, year, minor) # Undergraduate class
        students.append(student) # This adds the student to the list.
        print(f"Student - (Name - {name}, ID - {student_id}, Course - {course}, Year - {year}, Minor - {minor}) has been added. ") # Confirms it has been added.
    # If the student does not have a minor study, it creates a Student class.
    else:
        student = Student(name, student_id, course, year) # It adds a Student class.
        students.append(student) # Appends it to the list.
        print(f"Student - (Name - {name}, ID - {student_id}, Course - {course}, Year - {year}) has been added. ") # Confirmation statement.

# This deletes a student.
def delete_student(student_id):
    # This is exception handling.
    try:
        delete = 0 # This indicates if the student has been deleted. 0 means it has not been deleted, 1 means it has.
        for i in students:
            # This checks if the student ID matches.
            if i.get_student_id() == student_id: 
                students.remove(i) # Removes the student the list.
                print(f"Student ({student_id}) has been deleted. ") # Confirmation message.
                delete = 1 # This indicates it has been deleted. 1 = Student deleted.
                break # Exits the for loop since the student that has been looked for has been deleted.
        # If the student has not been found (0) it raises an error.
        if delete == 0:
            raise InvalidIDException() # Custom exception.
    # This runs if the program would crash.
    except:
        raise InvalidIDException() # Custom exception.

# This updates a student.
def update_student(student_id, new_course):
    # Exception handling. This runs the code regardless of if it crashes or not.
    try:
        update = 0 # Same as the delete function. 0 = Not updated, 1 = Updated.
        for i in students:
            # If the student ID that has been found. 
            if i.get_student_id() == student_id:
                i.update_course(new_course) # Updates the course.
                print(f"Student ({student_id}) has been updated. ") # Confirmation message.
                update = 1 # Update variable updates into 1 indicating it has been updated.
                break # Exits the for loop since the student's course was updated.
        # If the student has not been found, therefore it has not been updated, it runs the code below.
        if update == 0:
            raise InvalidIDException() # Custom exception that raises if the ID is invalid (not found). 
    # If the code does crash, it runs an error message below.
    except:
        raise InvalidIDException() # This is the custom exception that runs if the code would crash.

# This lists all the students
def list_students():
    # If the students list is not empty
    if students:
        # This iterates through the list of students.
        for i in students:
            print(i.get_details()) # This uses get detail function from the Student class.
    # If the student list is empty, it will output a message indicating that.
    else:
        print("No students. ") # This confirms the empty list by outputting that there are no students. 