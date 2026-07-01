from utils import *
from config import *
from file_manager import *

# Adding Functions

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

    append_file(course,COURSES_FILE)
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

    append_file(student, STUDENTS_FILE)
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

    append_file(lecturer, LECTURERS_FILE)
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


    append_file(module, MODULES_FILE)
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
    edit_entity('Lecturer', 'lecturers.txt', ['Name','Contact',], admin_lecturer_menu)
    continue_menu(function_title, admin_lecturer_menu, edit_lecturer)


# NEW ADDITION
def edit_course():
    function_title = "Edit Course Information"
    print(f"---{function_title}---\n")
    edit_entity('Course', 'courses.txt', ['Name'], admin_course_menu)
    continue_menu(function_title, admin_course_menu, edit_course)


# NEW ADDITION
def edit_student():
    function_title = "Edit Student Information"
    print(f"---{function_title}---\n")
    edit_entity('Student', 'STUDENTS_FILE', ['Name', 'Course ID', 'Contact', 'Email'], admin_student_menu)
    continue_menu(function_title, admin_student_menu, edit_student)


# NEW ADDITION
def edit_module():
    function_title = "Edit Module Information"
    print(f"---{function_title}---\n")
    edit_entity('Module', 'modules.txt', ['Name'], admin_module_menu)
    continue_menu(function_title, admin_student_menu, edit_student)



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

    with open("report.txt", "w") as reportFile: # Write report data to the file
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

    with open("allData.txt", "w") as allDataFile:  # Open file in write mode

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
            main()
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


#---------------------------------------------------------------------------------------------------------------------
#Lecturer Part


# reads modules from file for a specific lecturer
def load_modules(lecturer_id):
    modules_list = [
        line.strip().split(", ")
        for line in read_modules()
    ]
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
    grades_list = [
        line.strip().split(", ")
        for line in read_grades()
    ]
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
    write_grades(
        [", ".join(row) + "\n" for row in grades_list]
    )
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

    enrollments_list = [
        line.strip().split(", ")
        for line in read_enrollments()
    ]
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

    grades_list = [
        line.strip().split(", ")
        for line in read_grades()
    ]
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






#-----------------------------------------------------------------------------------------------------------------------
#Registrar Part


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
            print("Thank you!")
            break
        else:
            print("You can only write(1,2,3,4)")

#Making a def function for registering students
def register_student():
    students = read_students()  # Read existing data
    print("You can now register:")
    while True:
        student_tp = input("Please enter your TP number: ").upper()  # .upper() for consistency
        if not student_tp.strip():  # Check for empty or space-only input
            print("Your TP number cannot be empty or consist of spaces. Please enter your TP number again.")
        elif not check_unique_id(student_tp, students, 0):
            print("This TP number is already used. Please use a unique TP number.")
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
            print("Your E-mail cannot be empty or just be space. Please enter your program again.")
        elif check_unique_id(email, students, 4):             #We use the def function unique_email
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

    student_details = [student_tp, student_name, program, contact_information, email, birthday]
    students.append(student_details)  # Append the new student's details
    write_students(students)  # Write the updated list back to the file
    print("You are now registered.")
        #This def function will ensure that the TP number is not taken already


#Making a def function for finding a student based on TP number
def find_student_by_tp(tp_number):
    students = read_students()
    for student in students:
        if student[0] == tp_number:         #It will check if the TP number is already given or not
            return student
    return None

#Making a def function for displaying student details
def student_display():
    students = read_students()
    if not students:
        print("There are no registered students.")
        return
    print(f"Total students registered: {len(students)}")        #len(students) will count the number of students registered


#def function for updating student details
def student_update():
    tp_number = input("Enter your TP number: ").upper()
    students = read_students()  # Load all students from the file
    student_found = False
    for student in students:
        if student[0] == tp_number:  # Check if the TP number matches
            student_found = True
            print("Your current details are:")
            print(f"TP Number: {student[0]}, Name: {student[1]}, Program: {student[2]}, Contact: {student[3]}, Email Address: {student[4]}, Birthday: {student[5]}")
            print("Do you want to update your 'program','contact information' or 'E-mail ID'?")
            print("Press 1 for program, 2 for contact information, 3 for E-mail ID and 4 for exit.")
            update_details = input()
            if update_details == "1":
                new_program = input("Enter your new program: ")
                student[2] = new_program  # This code will change the student program of the selected student to new_program
            elif update_details == "2":
                new_contact = input("Enter your new contact information: ")
                student[3] = new_contact  # This code will change the student contact of the selected student to new_contact
            elif update_details == "3":
                new_email = input("Enter your new E-mail ID: ")
                student[4] = new_email
            elif update_details == "4":
                return
            else:
                print("You can only enter 1, 2, 3 or 4")
                return
            
            write_students(students)  # Write the updated list back to the file
            print("Your updated details are:")
            print(f"TP Number: {student[0]}, Name: {student[1]}, Program: {student[2]}, Contact: {student[3]}, Email Address: {student[4]}, Birthday: {student[5]}")
            print("Your details have been updated.")
            return
        
    if not student_found:
        print("Invalid TP number. Please check again.")


#Making a def function for checking details of each student
def each_details():
    tp_number = input("Please enter your TP number: ").upper()
    student = find_student_by_tp(tp_number)         #This will check if the TP number is used
    if student:      #\n is used to change lines
        print("Student details are:")
        print(f"TP Number: {student[0]} \nName: {student[1]} \nProgram: {student[2]} \nContact: {student[3]} \nE-mail ID: {student[4]}  \nBirthday: {student[5]}")
    else:
        print("Invalid TP number.")






#-----------------------------------------------------------------------------------------------------------------------
#Accountant Part


from datetime import datetime

def record_exists(sID, dop):
    with open("fee_records.txt", "r") as file:
        for line in file:
            record = line.strip().split(',')
            if len(record) >= 5 and record[0] == sID and record[4] == dop:
                return True
    return False


def record_tuition_fees():
    function_title = "Record Tuition Fees"
    while True:
        print(f"---{function_title}---")

        sID = input("Enter Student ID: ").strip()
        sN = input("Enter Student Name: ").strip()
        while True:
            try:
                aP = float(input("Enter Amount Paid: "))
                if aP > 0:
                    break
                print("Amount must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        while True:
            try:
                oB = float(input("Enter Outstanding Balance: "))
                if oB >= 0:
                    break
                print("Outstanding balance must not be negative.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        while True:
            dop = input("Enter Date of Payment (DD/MM/YYYY): ").strip()
            try:
                datetime.strptime(dop, "%d/%m/%Y")
                break
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        fee_records = [
            line.strip().split(", ")
            for line in read_fee_records()
        ]
        if any(record[0] == sID and record[4] == dop for record in fee_records):
            print(f"Error: A record already exists for Student ID {sID} on {dop}.")
        else:
            fee_records.append([sID, sN, f"{aP:.2f}", f"{oB:.2f}", dop])
            write_fee_records(
                [", ".join(row) + "\n" for row in fee_records]
            )
            print("Tuition fees recorded successfully.")

        if not repeat_action(function_title):
            break


def view_outstanding_fees():
    function_title = "View Outstanding Fees"
    while True:
        print(f"---{function_title}---")

        fee_records = [
            line.strip().split(", ")
            for line in read_fee_records()
        ]

        # To filter records w valid fees and + oB
        outstanding = [
            record for record in fee_records
            if len(record) >= 4 and record[3].strip() and float(record[3]) > 0
        ]

        if not outstanding:
            print("No outstanding fees.")
        else:
            print("Outstanding Fees:")
            for record in outstanding:
                print(f"Student ID: {record[0]}, Name: {record[1]}, Outstanding Balance: {record[3]}")

        if not repeat_action(function_title):
            break


def update_payment_records():
    function_title = "Update Payment Records"
    while True:
        print(f"---{function_title}---")

        sID = input("Enter Student ID: ").strip()
        try:
            aP = float(input("Enter Amount Paid: "))
            if aP <= 0:
                print("Amount must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        fee_records = [
            line.strip().split(", ")
            for line in read_fee_records()
        ]
        for record in fee_records:
            if record[0] == sID:
                outstanding_balance = float(record[3]) - aP
                record[3] = f"{max(outstanding_balance, 0):.2f}"
                record[2] = f"{aP:.2f}"
                write_fee_records(
                    [", ".join(row) + "\n" for row in fee_records]
                )
                print("Payment record updated successfully.")
                break
        else:
            print(f"No record found for Student ID {sID}.")

        if not repeat_action(function_title):
            break


def issue_fee_receipt():
    function_title = "Issue Fee Receipt"
    while True:
        print(f"---{function_title}---")

        sID = input("Enter Student ID: ").strip()
        dop = input("Enter Date of Payment (DD/MM/YYYY): ").strip()
        try:
            datetime.strptime(dop, "%d/%m/%Y")
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")
            continue

        fee_records = [
            line.strip().split(", ")
            for line in read_fee_records()
        ]
        for record in fee_records:
            if record[0] == sID and record[4] == dop:
                receipt_number = f"RCPT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
                receipt = (
                        f"Receipt Number: {receipt_number}\n"
                        f"Student ID: {record[0]}\n"
                        f"Name: {record[1]}\n"
                        f"Amount Paid: {record[2]}\n"
                        f"Outstanding Balance: {record[3]}\n"
                        f"Date of Payment: {record[4]}\n"
                        + "-" * 30
                )

                append_receipt(receipt)
                print(f"Receipt generated successfully. Receipt Number: {receipt_number}")
                break
        else:
            print(f"No record found for Student ID {sID} on {dop}.")

        if not repeat_action(function_title):
            break


def view_financial_summary():
    function_title = "View Financial Summary"
    while True:
        print(f"---{function_title}---")

        # Convert text data into a list of records
        fee_records = [
            line.strip().split(", ")
            for line in read_fee_records()
        ]

        # Calculate total collected and outstanding
        try:
            total_collected = sum(float(record[2]) for record in fee_records if len(record) > 2)
            total_outstanding = sum(float(record[3]) for record in fee_records if len(record) > 3)

            print(f"Total Fees Collected: {total_collected:.2f}")
            print(f"Total Outstanding Fees: {total_outstanding:.2f}")
        except (ValueError, IndexError) as e:
            print(f"Error processing financial summary: {e}")
            print("Please ensure the data in 'fee_records.txt' is formatted correctly.")

        # Repeat or exit
        if not repeat_action(function_title):
            break


# Other functions + main
def repeat_action(function_title):
    while True:
        choice = input(f"\nWould you like to {function_title.lower()} again? (1 for Yes, 0 for Main Menu): ").strip()
        if choice == "1":
            return True
        elif choice == "0":
            return False
        else:
            print("Invalid input. Please enter 1 or 0.")


# main program
def accountant_menu():
    while True:
        userchoice = input(
            "---Accountant Menu---\n"
            "1. Record Tuition Fees\n"
            "2. View Outstanding Fees\n"
            "3. Update Payment Records\n"
            "4. Issue Fee Receipts\n"
            "5. View Financial Summary\n"
            "0. Return to Main Menu\n"
            "Enter your choice: "
        )
        if userchoice == "1":
            record_tuition_fees()
        elif userchoice == "2":
            view_outstanding_fees()
        elif userchoice == "3":
            update_payment_records()
        elif userchoice == "4":
            issue_fee_receipt()
        elif userchoice == "5":
            view_financial_summary()
        elif userchoice == "0":
            break
        else:
            print("Invalid choice. Please try again.")






#-----------------------------------------------------------------------------------------------------------------------
# Student Functions

# View grades for the student

def view_grades(student_id):
    grades_list = text_to_list("grades.txt")
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
    attendance_list = text_to_list("attendance.txt")
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
    modules_list = text_to_list(MODULES_FILE)
    enrollments_list = text_to_list("enrollments.txt")

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
    list_to_text(enrollments_list, "enrollments.txt")
    print(f"Successfully enrolled in Module: {module_code}")


# View enrolled modules
def view_enrolled_modules(student_id):
    enrollments_list = text_to_list("enrollments.txt")
    modules_list = text_to_list(MODULES_FILE)
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
                # adding a password
                admin_password = "adm1n"
                while True:
                    entered_password = input(f"Enter password. (password is {admin_password})\n")
                    if entered_password == admin_password:
                        admin_menu()
                    else:
                        print("Incorrect password. Try again.")
            elif userchoice == "2":
                registrar_menu()
            elif userchoice == "3":
                accountant_menu()
            elif userchoice == "4":
                lecturer_menu()
            elif userchoice == "5":
                student_menu()

            # add menu of other roles
            else:
                print("Invalid input.")
            print("Error: An unexpected error has occurred.")
            #this is to catch any error that has not been handled.


#calling the main menu function
main()
