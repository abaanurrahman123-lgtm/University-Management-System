from utils import *
from config import *
from file_manager import *
from datetime import datetime

main_menu_callback = None


def set_main_menu(callback):
    global main_menu_callback
    main_menu_callback = callback

def record_exists(sID, dop):
    fee_records = read_fee_records()

    for record in fee_records:
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
            if main_menu_callback:
                main_menu_callback()
            break
        else:
            print("Invalid choice. Please try again.")