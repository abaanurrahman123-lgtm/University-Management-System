from admin import *

#---------------------------------------------------------------------------------------------------------------------
#Lecturer Part


# reads modules from file for a specific lecturer
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

        fee_records = read_fee_records()
        if any(record[0] == sID and record[4] == dop for record in fee_records):
            print(f"Error: A record already exists for Student ID {sID} on {dop}.")
        else:
            fee_records.append([sID, sN, f"{aP:.2f}", f"{oB:.2f}", dop])
            write_fee_records(fee_records)
            print("Tuition fees recorded successfully.")

        if not repeat_action(function_title):
            break


def view_outstanding_fees():
    function_title = "View Outstanding Fees"
    while True:
        print(f"---{function_title}---")

        fee_records = read_fee_records()

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

        fee_records = read_fee_records()
        for record in fee_records:
            if record[0] == sID:
                outstanding_balance = float(record[3]) - aP
                record[3] = f"{max(outstanding_balance, 0):.2f}"
                record[2] = f"{aP:.2f}"
                write_fee_records(fee_records)
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

        fee_records = read_fee_records()
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
        fee_records = read_fee_records()

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

set_main_menu(main)

#calling the main menu function
main()
