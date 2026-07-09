from file_manager import *

import admin
import registrar
import lecturer
import accountant
import student

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
                student.student_menu()
            else:
                print("Invalid input.")

admin.set_main_menu(main)
registrar.set_main_menu(main)
lecturer.set_main_menu(main)
accountant.set_main_menu(main)
student.set_main_menu(main)

main()
