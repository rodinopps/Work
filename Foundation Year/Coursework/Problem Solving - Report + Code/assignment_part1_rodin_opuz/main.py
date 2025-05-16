# Rodin Opuz - main.py
# Task 6
# Week 1

# This imports the save students and load students functions from storage.py.
from storage import save_students, load_students

# This imports the different functions for the management system and the students list.
from student_operations import students, add_student, delete_student, update_student, list_students

# This loads the students from the students.json file onto the list.
load_students(students)

# This is an infinite loop unless the user presses 5 which exits the system.
while True:
    # This displays the options for the menu where it has 5 options for the user represented as 5 numbers.
    print("""Object-Oriented Student Management System
    1. Add student
    2. Delete student
    3. Update student
    4. List students
    5. Exit system""")

    # This asks the user to select a number and stores it in a variable.
    menu_choice = input("Which option? Enter a number between 1 and 5 - ")

    # Choice 1 - This adds a new student.
    if menu_choice == "1":
        # These are student details.
        print("Add Students") 
        name = input("Enter student name - ") # Student name.
        student_id = input("Enter student ID (9 digits) - ") # Student ID.
        course = input("Enter student's course - ") # Student course.
        year = input("Enter student's year - ") # Student year.
        study = input("Undergraduate or Postgraduate - ") # Student study.

        # This is exception handling.
        try:
            # If the student is an undergraduate student, it will ask for the minor study.
            if study.lower() == "undergraduate":
                minor = input("Enter student's minor - ") # Student minor.
                add_student(name, student_id, course, year, minor) # This adds a student and their information with the minor
            # If the student is a postgraduate student, it will not ask for minor study.
            elif study.lower() == "postgraduate":
                add_student(name, student_id, course, year) # This adds a student and their information. (name, id, course and year).
            # If the user has not put a valid option (undergraduate or postgraduate) it will output an error message.
            else:
                print("Invalid. Please try again. ") # Error message.
        # If an error happens that would normally crash the program it will output just an error message instead of crashing.
        except:
            print("Invalid. Please try again. ") # Error message.

    # Choice 2 - Deletes a student ID.
    elif menu_choice == "2":
        print("Delete student ID. ")
        student_id = input("Student ID (9 digits) - ") # 9 digit student ID to delete it.
        # Exception handling.
        try:
            delete_student(student_id) # This is the delete function that deletes the student that corresponds to the 9 digit ID.
        # This occurs if there is an error that would crash the program.
        except:
            print("Invalid. Please try again. ") # Error message

    # Choice 3 - This updates a student's information.    
    elif menu_choice == "3":
        print("Update Students") 
        student_id = input("Enter student ID - ") # This asks for the student ID.
        new_course = input("Enter student's new course - ") # This asks for the new course the student is taking.
        # This is part of the exception handling.
        try:
            update_student(student_id, new_course) # This uses the update function with student id and new course parameters.
        # This occurs if the program may crash from a problem.
        except:
            print("Invalid. Please try again. ") # Error message.

    # Choice 4 - This lists the students.
    elif menu_choice == "4":
        print("List Students") 
        list_students() # The list students function.

    # Choice 5 - This exits the program.
    elif menu_choice == "5":
        save_students(students) # This saves the current list of students to the json file using the function.
        print("You have exit the program.") # Indicating the program has been exit.
        break # Breaks the while loop and exits the program.

    # If the user enteres anything else that is not 1-5. It will output an error message.
    else:
        print("Invalid option. Try again. ")