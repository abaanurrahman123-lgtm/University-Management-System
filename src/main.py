from file_manager import *
from utils import *

import admin
import registrar
import lecturer

#---------------------------------------------------------------------------------------------------------------------
#Lecturer Part



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
                accountant_menu()
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

#calling the main menu function
main()
