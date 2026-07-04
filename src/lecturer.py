from utils import *
from config import *
from file_manager import *

main_menu_callback = None


def set_main_menu(callback):
    global main_menu_callback
    main_menu_callback = callback

def load_modules(lecturer_id):
    modules_list = read_modules()
    #text_to_list function can extract the list, and it already has exception handling
    filtered_modules=[] #this is the module for the specific lecturer
    for module in modules_list:
        if module[3] == lecturer_id:
            filtered_modules.append([module[0],module[1]])
    return filtered_modules


# shows all modules for the lecturer
def view_assigned_modules(lecturer_id):
    modules = load_modules(lecturer_id)
    if len(modules) == 0:
        print("You don't have any modules!")
        return

    print("\nYour Modules:")
    print("-" * 30)
    for module in modules:
        print(f"Code: {module[0]} - {module[1]}")


# saves or updates student grade
def record_grade(lecturer_id, module_code, student_id, grade):
    # check if lecturer can grade this module
    can_grade = False
    for module in load_modules(lecturer_id):
        if module[0] == module_code:
            can_grade = True
            break

    if not can_grade:
        print("Whoops! Looks like you can't grade this module!")
        return False

    # read old grades
    grades_list = read_grades()
    # update grade if exists, else add new one
    found = False
    for i in range(len(grades_list)):
        if grades_list[i][0] == student_id and grades_list[i][1] == module_code:
            grades_list[i] = [student_id, module_code, grade]
            found = True
            break

    if not found:
        grades_list.append([student_id, module_code, grade])

    # save all grades back to file
    write_grades(grades_list)
    #list to text function can be used to write the list to the text file, already does exception handling


# shows students in a module
def view_student_list(lecturer_id, module_code):
    # check if lecturer teaches this module
    can_view = False
    for module in load_modules(lecturer_id):
        if module[0] == module_code:
            can_view = True
            break

    if not can_view:
        print("Whoops! Looks like you can't view this module's students!")
        return

    enrollments_list = read_enrollments()
    print(f"\nStudents in {module_code}:")
    print("-" * 30)
    found_students = False
    for enrollment in enrollments_list:
        if enrollment[1] == module_code:
            print(f"Student ID: {enrollment[0]}")
            found_students = True
    if not found_students:
        print("No students enrolled yet!")


# saves student attendance
def track_attendance(lecturer_id, module_code, date, student_id, status):
    # check if lecturer teaches this module
    can_track = False
    for module in load_modules(lecturer_id):
        if module[0] == module_code:
            can_track = True
            break

    if not can_track:
        print("Whoops! Looks like you can't track attendance for this module!")
        return False

    try:
        record = f"{date}, {module_code}, {student_id}, {status}"
        append_attendance(record)
        print("Saved attendance!")
        return True
    except Exception:
        print("Whoops! Looks like you couldn't save the attendance.")
        return False


# shows grades for all students in a module
def view_student_grades(lecturer_id, module_code):
    # check if lecturer teaches this module
    can_view = False
    for module in load_modules(lecturer_id):
        if module[0] == module_code:
            can_view = True
            break

    if not can_view:
        print("Whoops! Looks like you can't view grades for this module!")
        return

    grades_list = read_grades()
    print(f"\nGrades for {module_code}:")
    print("-" * 30)
    found_grades = False
    for grade in grades_list:
        if grade[1] == module_code:
            print(f"Student: {grade[0]} - Grade: {grade[2]}")
            found_grades = True
    if not found_grades:
        print("No grades recorded yet!")


# shows main menu options
def show_menu():
    print("\n=== Lecturer System ===")
    print("1. See My Modules")
    print("2. Record a Grade")
    print("3. See Student List")
    print("4. Take Attendance")
    print("5. See Student Grades")
    print("6. Exit")
    print("\nPick an option (1-6): ")


# handles grade recording menu
def handle_grades(lecturer_id):
    while True:
        print("\n=== Record Grades ===")
        print("1. Add Grade")
        print("2. Back to Main Menu")

        choice = input("\nPick an option (1-2): ")

        if choice == '1':
            module = input("Module code: ")
            student = input("Student ID: ")
            grade = input("Grade: ")
            record_grade(lecturer_id, module, student, grade)
        elif choice == '2':
            print("Going back...")
            break
        else:
            print("Invalid choice!")


# handles student list menu
def handle_students(lecturer_id):
    while True:
        print("\n=== Student List ===")
        print("1. See Module Students")
        print("2. Back to Main Menu")

        choice = input("\nPick an option (1-2): ")

        if choice == '1':
            module = input("Module code: ")
            view_student_list(lecturer_id, module)
        elif choice == '2':
            print("Going back...")
            break
        else:
            print("Invalid choice!")


# handles attendance menu
def handle_attendance(lecturer_id):
    while True:
        print("\n=== Take Attendance ===")
        print("1. Record Attendance")
        print("2. Back to Main Menu")

        choice = input("\nPick an option (1-2): ")

        if choice == '1':
            while True:
                module = input("Module code: ")
                date = input("Date (YYYY-MM-DD): ")
                student = input("Student ID: ")
                status = input("Status (present/absent): ")

                if track_attendance(lecturer_id, module, date, student, status):
                    print("\nWhat next?")
                    print("1. Record Another")
                    print("2. Back to Main Menu")
                    next_choice = input("\nPick an option (1-2): ")
                    if next_choice == '2':
                        return
                    elif next_choice != '1':
                        print("Invalid choice!")
                        break
                else:
                    print("Going back to attendance menu...")
                    break

        elif choice == '2':
            print("Going back...")
            break
        else:
            print("Invalid choice!")


# handles viewing grades menu
def handle_view_grades(lecturer_id):
    while True:
        print("\n=== View Grades ===")
        print("1. See Module Grades")
        print("2. Back to Main Menu")

        choice = input("\nPick an option (1-2): ")

        if choice == '1':
            module = input("Module code: ")
            view_student_grades(lecturer_id, module)
        elif choice == '2':
            print("Going back...")
            break
        else:
            print("Invalid choice!")


# main program
def lecturer_menu():
    lecturer_id = input("Enter your lecturer ID: ")

    while can_login(lecturer_id,LECTURERS_FILE, "Lecturer"):
        show_menu()
        choice = input()

        if choice == '1':
            view_assigned_modules(lecturer_id)
            input("\nPress Enter to continue...")
        elif choice == '2':
            handle_grades(lecturer_id)
        elif choice == '3':
            handle_students(lecturer_id)
        elif choice == '4':
            handle_attendance(lecturer_id)
        elif choice == '5':
            handle_view_grades(lecturer_id)
        elif choice == '6':
            print("Thank you for using the system. Goodbye for now!")
            break
        else:
            print("Invalid choice!")