from utils import *
from file_manager import *

main_menu_callback = None


def set_main_menu(callback):
    global main_menu_callback
    main_menu_callback = callback

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

def enroll_in_module(student_id):
    modules_list = read_modules()
    enrollments_list = read_enrollments()

    print("\nAvailable Modules:")
    for module in modules_list:
        print(f"Code: {module[0]} - Name: {module[1]}")

    module_code = input("\nEnter the Module Code you want to enroll in: ")

    module_exists = any(module[0] == module_code for module in modules_list)
    if not module_exists:
        print("Invalid Module Code. Please try again.")
        return

    already_enrolled = any(
        enrollment[0] == student_id and enrollment[1] == module_code for enrollment in enrollments_list)
    if already_enrolled:
        print("You are already enrolled in this module.")
        return

    enrollments_list.append([student_id, module_code])
    write_enrollments(enrollments_list)
    print(f"Successfully enrolled in Module: {module_code}")

def view_enrolled_modules(student_id):
    enrollments_list = read_enrollments()
    modules_list = read_modules()
    print(f"\nEnrolled Modules for Student ID: {student_id}")
    found_modules = False
    for enrollment in enrollments_list:
        if enrollment[0] == student_id:
            module_code = enrollment[1]
            module_name = next((module[1] for module in modules_list if module[0] == module_code), "Unknown Module")
            print(f"Code: {module_code} - Name: {module_name}")
            found_modules = True
    if not found_modules:
        print("You are not enrolled in any modules.")

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
        elif choice == "5":
            if main_menu_callback:
                main_menu_callback()
            break
        else:
            print("Invalid choice. Please try again.")