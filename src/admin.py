from utils import *
from file_manager import *

main_menu_callback = None

def set_main_menu(callback):
    global main_menu_callback
    main_menu_callback = callback

def add_course():
    function_title = "Add a Course"
    print(f"---{function_title}---\n")

    course_id = input("Enter the course ID: ")
    course_name = input("Enter the course name: ")

    while True:
        try:
            course_credit = int(input("Enter the course credit: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            #this ensures that the user inputs a numeric value

    course = f"{course_id}, {course_name}, {course_credit}"

    append_course(course)
    print("Course added successfully.")

    # option to do it again or go back to menu
    continue_menu(function_title, admin_course_menu,add_course)

def add_student():
    function_title = "Add a Student"
    print(f"---{function_title}---\n")
    student_id = input("Enter the Student ID: ")
    student_name = input("Enter the student name: ")
    student_course = input("Enter the student department: ")
    student_contact = input("Enter the student contact: ")
    student_email = input("Enter the student email: ")
    student_birthday = input("Enter the student birthday (YYYY-MM-DD format): ")

    student = f"{student_id}, {student_name}, {student_course}, {student_contact}, {student_email}, {student_birthday}"

    append_student(student)
    print("Student added successfully.")

    # option to do it again or go back to menu
    continue_menu(function_title, admin_student_menu,add_student)


def add_lecturer():
    function_title = "Add a Lecturer"
    print(f"---{function_title}---\n")
    lecturer_id = input("Enter the Lecturer ID: ")
    lecturer_name = input("Enter the lecturer's name: ")
    lecturer_contact = input("Enter the lecturer's contact: ")

    lecturer = f"{lecturer_id}, {lecturer_name}, {lecturer_contact}"

    append_lecturer(lecturer)
    print("Lecturer added successfully.")

    # option to do it again or go back to menu
    continue_menu(function_title, admin_lecturer_menu, add_lecturer)


#NEW ADDITION
def add_module():
    function_title = "Add a Module"
    print(f"---{function_title}---\n")

    module_id = input("Enter the module ID: ")
    module_name = input("Enter the module name: ")
    course_id = input("Enter the course ID: ")

    module = f"{module_id}, {module_name}, {course_id}"


    append_module(module)
    print("Module added successfully.")

    # option to do it again or go back to menu
    continue_menu(function_title, admin_module_menu,add_module)

# Removing Functions

def remove_student():
    function_title = f"Remove a Student"
    print(f"---{function_title}---\n")
    remove_entity("Student", STUDENTS_FILE)

    continue_menu(function_title, admin_student_menu, remove_student)


def remove_lecturer():
    function_title = "Remove a Lecturer"
    print(f"---{function_title}---\n")
    remove_entity("Lecturer", LECTURERS_FILE)

    continue_menu(function_title, admin_lecturer_menu, remove_lecturer)


def remove_course(): #NEW ADDITION
    function_title = "Remove a Course"
    print(f"---{function_title}---\n")
    remove_entity("Course", COURSES_FILE)

    continue_menu(function_title, admin_course_menu, remove_course)


def remove_module(): #NEW ADDITION
    function_title = "Remove a Module"
    print(f"---{function_title}---\n")
    remove_entity("Module", MODULES_FILE)

    continue_menu(function_title, admin_module_menu, remove_module)



# Editing Functions

def edit_lecturer():
    function_title = "Edit Lecturer Information"
    print(f"---{function_title}---\n")
    edit_entity('Lecturer', LECTURERS_FILE, ['Name','Contact',], admin_lecturer_menu)
    continue_menu(function_title, admin_lecturer_menu, edit_lecturer)


# NEW ADDITION
def edit_course():
    function_title = "Edit Course Information"
    print(f"---{function_title}---\n")
    edit_entity('Course', COURSES_FILE, ['Name'], admin_course_menu)
    continue_menu(function_title, admin_course_menu, edit_course)


# NEW ADDITION
def edit_student():
    function_title = "Edit Student Information"
    print(f"---{function_title}---\n")
    edit_entity('Student', STUDENTS_FILE, ['Name', 'Course ID', 'Contact', 'Email'], admin_student_menu)
    continue_menu(function_title, admin_student_menu, edit_student)


# NEW ADDITION
def edit_module():
    function_title = "Edit Module Information"
    print(f"---{function_title}---\n")
    edit_entity('Module', MODULES_FILE, ['Name'], admin_module_menu)
    continue_menu(function_title, admin_module_menu, edit_module)

#Other role specific functions

def generate_report():
    #extract data from text file and put it in a list then use the len() function to count each record
    with open(COURSES_FILE, "r") as courseFile:
        course_list = courseFile.readlines()
    total_courses = len(course_list)

    with open(STUDENTS_FILE, "r") as studentFile:
        student_list = studentFile.readlines()
    total_students = len(student_list)

    with open(MODULES_FILE, "r") as moduleFile: # NEW ADDITION
        module_list = moduleFile.readlines()
    total_modules = len(module_list)

    with open(LECTURERS_FILE, "r") as lecturerFile:
        lecturer_list = lecturerFile.readlines()
    total_lecturers = len(lecturer_list)

    with open(REPORT_FILE, "w") as reportFile: # Write report data to the file
        reportFile.write(f"---REPORT---\n\n"
                         f"Total number of Students: {total_students}\n"
                         f"Total number of Courses: {total_courses}\n"
                         f"Total number of Modules: {total_modules}\n" #NEW ADDITION
                         f"Total number of Lecturers: {total_lecturers}\n")
    print("Report generated and saved to 'report.txt'")

    while True: #go back to menu option
        userchoice = input("\nPress 0 to return to menu.\n")
        if userchoice == "0":
            admin_menu()
        else:
            print("Invalid input.")


def view_all_data():

    with open(ALL_DATA_FILE, "w") as allDataFile:  # Open file in write mode

        display_list(allDataFile, "Students", STUDENTS_FILE)
        display_list(allDataFile, "Courses", COURSES_FILE)
        display_list(allDataFile, "Lecturers", LECTURERS_FILE)
        display_list(allDataFile, "Modules", MODULES_FILE) #NEW ADDITION

    print("All data saved to 'allData.txt'")

    # go back to menu option
    while True:
        userchoice = input("\nPress 0 to return to menu.\n")
        if userchoice == "0":
            admin_menu()
        else:
            print("Invalid input.")

#Menus
#Sub-menus


def admin_student_menu():
    while True:
        userchoice = input(f"---Administrator Student Menu---"
                           f"\n"
                           f"\nAdd a new student [Press 1]"
                           f"\nRemove a student [Press 2]"
                           f"\nEdit student information [Press 3]"
                           f"\n"
                           f"\nPress 0 to return to Administrator menu."
                           f"\n"
                           f"\n")
        if userchoice == "0":
            admin_menu()
        elif userchoice == "1":
            add_student()
        elif userchoice == "2":
            remove_student()
        elif userchoice == "3":
            edit_student()
        else:
            print("Invalid input.")


def admin_lecturer_menu():
    while True:
        userchoice = input(f"---Administrator Lecturer Menu---"
                           f"\n"
                           f"\nAdd a new lecturer [Press 1]"
                           f"\nRemove a lecturer [Press 2]"
                           f"\nEdit lecturer information [Press 3]"
                           f"\n"
                           f"\nPress 0 to return to Administrator menu."
                           f"\n"
                           f"\n")
        if userchoice == "0":
            admin_menu()
        elif userchoice == "1":
            add_lecturer()
        elif userchoice == "2":
            remove_lecturer()
        elif userchoice == "3":
            edit_lecturer()
        else:
            print("Invalid input.")


def admin_module_menu():
    while True:
        userchoice = input(f"---Administrator Module Menu---"
                           f"\n"
                           f"\nAdd a new module [Press 1]"
                           f"\nRemove a module [Press 2]"
                           f"\nEdit module information [Press 3]"
                           f"\n"
                           f"\nPress 0 to return to Administrator menu."
                           f"\n"
                           f"\n")
        if userchoice == "0":
            admin_menu()
        elif userchoice == "1":
            add_module()
        elif userchoice == "2":
            remove_module()
        elif userchoice == "3":
            edit_module()
        else:
            print("Invalid input.")


def admin_course_menu():
    while True:
        userchoice = input(f"---Administrator Course Menu---"
                           f"\n"
                           f"\nAdd a new course [Press 1]"
                           f"\nRemove a course [Press 2]"
                           f"\nEdit course information [Press 3]"
                           f"\n"
                           f"\nPress 0 to return to Administrator menu."
                           f"\n"
                           f"\n")
        if userchoice == "0":
            admin_menu()
        elif userchoice == "1":
            add_course()
        elif userchoice == "2":
            remove_course()
        elif userchoice == "3":
            edit_course()
        else:
            print("Invalid input.")



#Administrator menu

def admin_menu():
    while True:
        userchoice = input(f"---Administrator Menu---"
                           f"\n"
                           f"\nManage Courses [Press 1]"
                           f"\nManage Students [Press 2]"
                           f"\nManage Lecturers [Press 3]"
                           f"\nManage Modules [Press 4]"
                           f"\nGenerate a report [Press 5]"
                           f"\nView All Data [Press 6]"
                           f"\n"
                           f"\nPress 0 to return to main menu."
                           f"\n"
                           f"\n")
        if userchoice == "0":
            if main_menu_callback:
                main_menu_callback()
            break
        elif userchoice == "1":
            admin_course_menu()
        elif userchoice == "2":
            admin_student_menu()
        elif userchoice == "3":
            admin_lecturer_menu()
        elif userchoice == "4":
            admin_module_menu()
        elif userchoice == "5":
            generate_report()
        elif userchoice == "6":
            view_all_data()
        else:
            print("Invalid input.")