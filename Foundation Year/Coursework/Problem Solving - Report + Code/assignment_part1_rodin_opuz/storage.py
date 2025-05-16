# Rodin Opuz - storage.py
# Task 5
# Week 7

# This imports the json module to handle JSON files. 
import json

# This imports Student class from student.py in models folder.
from models.student import Student

# This imports Undergraduate class from undergraduate.py in models folder.
from models.undergraduate import Undergraduate

# This is a function that saves the list of students to a JSON file which in this work is called students.json.
def save_students(students):
    # This is an empty list to store student information as dictionaries.
    student_list = []
    # This loops through the students in the list.
    for i in students:
        # This stores the attributes of a student as a dictionary 
        student_information = {"Type": i.__class__.__name__, "Name": i.name, "ID": i.get_student_id(), "Course": i.course, "Year": i.year}
        
        # This loads if the student is an Undergraduate.
        if isinstance(i, Undergraduate):
            student_information["Minor"] = i.minor # If the student is an undergraduate, it adds the minor study to the dictionary.
        student_list.append(student_information) # The student information is added to the student list.

    # This opens or creates the file if it does not exist. w = Write.
    with open("students.json", 'w') as file:
        json.dump(student_list, file) # This puts the student list into JSON file.

    print("Students saved.") # Confirmation message.

# This is a function that loads the list of students from the JSON file.
def load_students(students):
    # This is exception handling.
    try:
        # Opens the JSON file students.json. r = Read.
        with open("students.json", "r") as file:
            student_list = json.load(file) # This loads the contents of the JSON file in the variable student list.
        students.clear() # This empties the list to remove student objects in case of duplicates.
        # Looops through each student in the list.
        for i in student_list:
            # If the type is Undergraduate, it adds a minor study.
            if i["Type"] == "Undergraduate":
                # Undergraduate class for a student.
                student = Undergraduate(i["Name"], i["ID"], i["Course"], i["Year"], i["Minor"])
            # If the type is Student, it adds just Name, ID, Course and Year.
            else:
                # Student class.
                student = Student(i["Name"], i["ID"], i["Course"], i["Year"])
            students.append(student) # Adds the student which is an object to the list.
    # If the program crashes, it will show an error message.
    except:
        print("Error") # Error message.