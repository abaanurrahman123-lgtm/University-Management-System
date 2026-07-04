from file_manager import *
from utils import *

import admin
import registrar
import lecturer
import accountant

#-----------------------------------------------------------------------------------------------------------------------
# Student Functions

# View grades for the student

def view_grades(student_id):
    grades_list = read_grades()
    print(f"\nGrades for Student ID: {student_id}")
    found_grades = False
    for grade in grades_list:
        if grade[0] == student_id:
            print(f"Module: {grade[1]} - Grade: {grade[2]}")
            found_grades = True
    if not found_grades:
        print("No grades recorded yet.")

# View attendance for the student
def view_attendance(student_id):
    attendance_list = read_attendance()
    print(f"\nAttendance for Student ID: {student_id}")
    found_attendance = False
    for record in attendance_list:
        if record[2] == student_id:
            print(f"Date: {record[0]}, Module: {record[1]}, Status: {record[3]}")
            found_attendance = True
    if not found_attendance:
        print("No attendance records found.")

# Enroll in a module
def enroll_in_module(student_id):
    modules_list = read_modules()
    enrollments_list = read_enrollments()

    print("\nAvailable Modules:")
    for module in modules_list:
        print(f"Code: {module[0]} - Name: {module[1]}")

    module_code = input("\nEnter the Module Code you want to enroll in: ")

    # Check if the module exists
    module_exists = any(module[0] == module_code for module in modules_list)
    if not module_exists:
        print("Invalid Module Code. Please try again.")
        return

    # Check if already enrolled
    already_enrolled = any(
        enrollment[0] == student_id and enrollment[1] == module_code for enrollment in enrollments_list)
    if already_enrolled:
        print("You are already enrolled in this module.")
        return

    # Add the enrollment record
    enrollments_list.append([student_id, module_code])
    write_enrollments(enrollments_list)
    print(f"Successfully enrolled in Module: {module_code}")


# View enrolled modules
def view_enrolled_modules(student_id):
    enrollments_list = read_enrollments()
    modules_list = read_modules()
    print(f"\nEnrolled Modules for Student ID: {student_id}")
    found_modules = False
    for enrollment in enrollments_list:
        if enrollment[0] == student_id:
            module_code = enrollment[1]
            # Find the module name
            module_name = next((module[1] for module in modules_list if module[0] == module_code), "Unknown Module")
            print(f"Code: {module_code} - Name: {module_name}")
            found_modules = True
    if not found_modules:
        print("You are not enrolled in any modules.")


# Student Menu
def student_menu():
    student_id = input("Enter your Student ID: ")

    while can_login(student_id, STUDENTS_FILE, "Student"):
        print("\n=== Student System ===")
        print("1. View Grades")
        print("2. View Attendance")
        print("3. Enroll in a Module")
        print("4. View Enrolled Modules")
        print("5. Exit")

        choice = input("\nPick an option (1-5): ")

        if choice == '1':
            view_grades(student_id)
            input("\nPress Enter to continue...")
        elif choice == '2':
            view_attendance(student_id)
            input("\nPress Enter to continue...")
        elif choice == '3':
            enroll_in_module(student_id)
            input("\nPress Enter to continue...")
        elif choice == '4':
            view_enrolled_modules(student_id)
            input("\nPress Enter to continue...")
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")






#-----------------------------------------------------------------------------------------------------------------------
#Main Menu

def main():
    while True:
            userchoice = input(f"---Main Menu---"
                               f"\n"
                               f"\nAccess as:"
                               f"\nAdministrator [Press 1]"
                               f"\nRegistrar [Press 2]"
                               f"\nAccountant [Press 3]"
                               f"\nLecturer [Press 4]"
                               f"\nStudent [Press 5]"
                               f"\n"
                               f"\nPress 0 to exit program\n")
            if userchoice == "0":
                print("You have exited the program.")
                exit()
            elif userchoice == "1":
                while True:
                    entered_password = input(
                        f"Enter password. (password is {ADMIN_PASSWORD})\n"
                    )

                    if entered_password == ADMIN_PASSWORD:
                        admin.admin_menu()
                        break
                    else:
                        print("Incorrect password. Try again.")
            elif userchoice == "2":
                registrar.registrar_menu()
            elif userchoice == "3":
                accountant.accountant_menu()
            elif userchoice == "4":
                lecturer.lecturer_menu()
            elif userchoice == "5":
                student_menu()

            # add menu of other roles
            else:
                print("Invalid input.")
            #this is to catch any error that has not been handled.

admin.set_main_menu(main)
registrar.set_main_menu(main)
lecturer.set_main_menu(main)
accountant.set_main_menu(main)

#calling the main menu function
main()
