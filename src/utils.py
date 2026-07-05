from file_manager import read_records, write_records
"""
utils.py

Shared utility functions used throughout the University Management System.
"""

def text_to_list(file_path):
    #this function will be used each time what data is extracted from a text file to put in a list variable for processing
    my_list = []
    try:
        with open(file_path, "r") as file: # open in reading mode
            lines = file.readlines() # extract the lines from the file
            for line in lines: #loop that goes through each line in the text file
                my_list.append(line.strip().split(", "))
                # line.strip() removes any extra whitespace or newline characters from the start and end of the line
                # .split(", ") then splits the line into a list of strings based on the separator ", "
        file.close()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except IOError:
        print(f"Error: An input/output error occurred while accessing {file_path}.")
    return my_list

def list_to_text(my_list, file_path):
    try:
        with open(file_path, "w") as file: #open in write mode
            for row in my_list: # for each row in the list, write it to the file and use a separator
                file.write(", ".join(row) + "\n")
        file.close()
    except IOError:
        print(f"Error: Could not write to file {file_path}.")

def append_file(record, file_path):  
    # Check if the file exists by trying to open it in read mode
    try:
        with open(file_path, "r"):
            pass  # If this succeeds, the file exists
    except FileNotFoundError:
        print(f"File {file_path} not found. Creating a new file...")

    # Append the record to the file (or create it if it doesn't exist)
    try:
        with open(file_path, "a") as file:
            file.write(f"{record}\n")  # Add a newline after the record
    except IOError:
        print(f"Error: An input/output error occurred while accessing {file_path}.")

def remove_entity(entity_name, entity_file):  
    search_id = input(f"Enter {entity_name} ID: ")

    my_list = read_records(entity_file)

    # Loop through the list with an index to keep track of positions
    for index, record in enumerate(my_list):
        if search_id == record[0]:
            print(f"Record selected: {record}")
            choice_verification = input("Are you sure you want to delete this record? (y/n): ")
            if choice_verification.lower() == 'y':
                del my_list[index]
                print(f"{entity_name} {search_id} removed successfully.")
                write_records(entity_file, my_list)
            else:
                print("Delete cancelled.")
            return
    print(f"{entity_name} {search_id} not found.")


def edit_entity(entity_name, file_path, fields, menu_function):  

    search_id = input(f"Enter {entity_name} ID: ")

    # Load the entity list from the file
    entity_list = read_records(file_path)

    # Find the entity by ID
    for index, entity in enumerate(entity_list):
        if search_id == entity[0]:
            print(f"Current information: {entity}")
            while True:
                print("\n".join([f"Press {i + 1} to change {field}." for i, field in enumerate(fields)]))
                print("Press 0 to return to the previous menu.")
                userchoice = input("Choose an option: ")

                if userchoice == "0":
                    menu_function()  # Go back to the menu
                    break
                elif userchoice.isdigit() and 1 <= int(userchoice) <= len(fields):
                    field_index = int(userchoice) - 1
                    new_value = input(f"Enter the new {fields[field_index]}: ")
                    entity[field_index + 1] = new_value  # Update the appropriate field
                    print(f"{entity_name} {fields[field_index]} updated to {new_value}")
                else:
                    print("Invalid option. Please choose a valid option.")
                    continue  # If invalid option is entered, restart the loop

                # Ask if they want to make more changes
                continue_editing = input("Would you like to make more changes? (y/n): ")
                if continue_editing.lower() != 'y':
                    break  # Exit the loop if no further changes are needed

            # Save updated entity information
            entity_list[index] = entity
            print(f"{entity_name} {entity[0]} updated successfully!")

            # Write the updated list back to the file
            write_records(file_path, entity_list)
            return

    print(f"{entity_name} {search_id} not found.")



def continue_menu(function_title, role_menu, repeating_function):  
    while True:
        userchoice = input(f"\nPress 1 to {function_title}. Press 0 to return to menu.\n")
        if userchoice == "1":
            repeating_function()
        elif userchoice == "0":
            role_menu()
            break
        else:
            print("Invalid input.")


def display_list(display_file, entity_name, entity_file):  
    display_file.write(f"\n\n---{entity_name}---\n\n")
    with open(entity_file, "r") as file:
        my_list = file.readlines()
        for row in my_list:
            display_file.write(row.strip() + "\n")


def can_login(search_id, file_path, entity_name):
    my_list = read_records(file_path)

    for entity in my_list:
        # Check if the entity's ID matches the ID we are searching for
        if search_id == entity[0]:
            return True

    # If no match is found after checking all entities, print a message and return False
    print(f"{entity_name} {search_id} not found.")
    return False


def check_unique_id(id, list, column):
    #This def function will ensure that an ID is unique
    return not any(row[column] == id for row in list)