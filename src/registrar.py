from utils import *
from file_manager import *
from services.student_service import (
    find_student,
    register_student,
    email_available,
    update_student,
)
from services.student_service import register_student as register_student_service

main_menu_callback = None


def set_main_menu(callback):
    global main_menu_callback
    main_menu_callback = callback

def register_student():
    print("You can now register:")
    while True:
        student_tp = input("Please enter your TP number: ").upper()  # .upper() for consistency
        if not student_tp.strip():  # Check for empty or space-only input
            print("Your TP number cannot be empty or consist of spaces. Please enter your TP number again.")
        elif find_student(student_tp) is not None:
            print("This TP number is already used.")
        else:
            break

    while True:
        student_name = input("Please enter your full name: ")
        if any(char.isdigit() for char in student_name):  # char.isdigit is used to make sure there are no digits
            print("Your name cannot have numbers. Please enter your full name again.")
        elif not student_name.strip():  # This code will stop people from entering empty name or name that only consists of spaces in student name
            print("Your name cannot be empty or just be space. Please enter your full name again.")
        else:
            break

    while True:
        program = input("Please enter your program: ")
        if any(char.isdigit() for char in program):
            print("Your program cannot have numbers in it. Please enter your program again.")
        elif not program.strip():         #This code will stop people from entering empty program or program that only consists of spaces
            print("Your program cannot be empty or just be space. Please enter your program again.")
        else:
            break

    while True:
        contact_information = input("Please enter your contact number: ")
        if any(char.isalpha() for char in contact_information):         #char.isalpha() is used to make sure there are no alphabets used in contact information
            print("Your contact number cannot have an alphabet in it. Please enter your contact number again.")
        elif not contact_information.strip():               #This code will stop people from entering empty contact or contact that only consists of spaces
            print("Your contact number cannot be empty or just be space. Please enter your contact number again.")
        else:
            break

    while True:
        email = input("Please enter your e-mail address: ")
        if not email.strip():             #This code will stop people from entering empty e_mail or e_mail that only consists of spaces
            print("Your E-mail cannot be empty or just be space. Please enter your E-mail again.")
        elif email_available(email):
            break
        else:
            print("This email ID has already been taken. Please enter a unique email ID.")

    while True:
        birthday = input("Please enter your birthday: ")
        if any(char.isalpha() for char in birthday):
            print("Your birthday cannot have alphabets. Please enter your birthday again.")
        elif not birthday.strip():              #This code will stop people from entering empty birthday or birthday that only consists of spaces
            print("Your birthday cannot be empty or just be space. Please enter your birthday again.")
        else:
            break

    student_data = (
        student_tp,
        student_name,
        program,
        contact_information,
        email,
        birthday,
    )

    success, message = register_student_service(student_data)

    print(message)
        #This def function will ensure that the TP number is not taken already


from services.student_service import find_student

def find_student_by_tp(tp_number):
    return find_student(tp_number)


# Making a def function for displaying student details
def student_display():
    students = read_students()
    if not students:
        print("There are no registered students.")
        return
    print(f"Total students registered: {len(students)}")  # len(students) will count the number of students registered


# def function for updating student details
def student_update():
    tp_number = input("Enter your TP number: ").upper()
    student = find_student(tp_number)
    if student is None:
        print("Invalid TP number. Please check again.")
        return
    print("Your current details are:")
    print(
        f"TP Number: {student.tp_number}, "
        f"Name: {student.name}, "
        f"Program: {student.program}, "
        f"Contact: {student.contact}, "
        f"Email Address: {student.email}, "
        f"Birthday: {student.birthday}"
    )

    print("Do you want to update your 'program', 'contact information' or 'E-mail ID'?")
    print("Press 1 for program, 2 for contact information, 3 for E-mail ID and 4 for exit.")

    update_details = input("Enter your choice: ")
    if update_details == "1":
        new_program = input("Enter your new program: ")

        success, result = update_student(
            tp_number,
            program=new_program,
        )

        if not success:
            print(result)
            return

        student = result
    elif update_details == "2":
        new_contact = input("Enter your new contact information: ")

        success, result = update_student(
            tp_number,
            contact=new_contact,
        )

        if not success:
            print(result)
            return

        student = result
    elif update_details == "3":
        new_email = input("Enter your new E-mail ID: ")

        success, result = update_student(
            tp_number,
            email=new_email,
        )

        if not success:
            print(result)
            return

        student = result
    elif update_details == "4":
        return
    else:
        print("You can only enter 1, 2, 3 or 4")
        return
    print("Your updated details are:")
    print(
        f"TP Number: {student.tp_number}, "
        f"Name: {student.name}, "
        f"Program: {student.program}, "
        f"Contact: {student.contact}, "
        f"Email Address: {student.email}, "
        f"Birthday: {student.birthday}"
    )

    print("Your details have been updated.")

def each_details():
    tp_number = input("Please enter your TP number: ").upper()
    student = find_student_by_tp(tp_number)         #This will check if the TP number is used
    if student:      #\n is used to change lines
        print("Student details are:")
        print(
            f"TP Number : {student.tp_number}"
            f"\nName      : {student.name}"
            f"\nProgram   : {student.program}"
            f"\nContact   : {student.contact}"
            f"\nEmail     : {student.email}"
            f"\nBirthday  : {student.birthday}"
        )
    else:
        print("Invalid TP number.")

#Making a def function for menu
def registrar_menu():
    while True:
        print("------Registrar------")
        print("1.Register \n2.Student update \n3.View student details. \n4.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_student()              #register_student() is written to use the def function register_student()
            student_display()               #student_display() is written to use the def function student_display()
        elif choice == "2":
            student_update()                #student_update() is written to use the def function student_update()
        elif choice == "3":
            each_details()                  #each_details() is written to use the def function each_details()
        elif choice == "4":
            if main_menu_callback:
                main_menu_callback()
            break
        else:
            print("You can only write(1,2,3,4)")