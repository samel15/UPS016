# Import modules
from Files import *


def main_menu():
    """
    The main function - allows to run the application and displays the main menu
    :return:
    """
    # The global variables
    choice = None

    # The main loop of the program - the lottery menu
    while choice != 0:
        print(
            """
        The lottery menu
    
        0 - Close the application
        1 - Choose JSON files with or without weights
        2 - Choose CSV files with or without weights
        """
        )
        choice = input("Choose: ")

        # Choice 0 - Exit the application
        if choice == "0":
            input("\nPress 'Enter' to confirm and close the application: ")
            break

        # Choice 1 - Choose JSON files with or without weights
        elif choice == "1":
            choose = ask_yes_no("To choose JSON file without weights press y, otherwise press n. (y/n): ")

            # Load the function with the JSON file without weights
            if choose == "y":
                load_json_wow()

            # Load the function with the JSON file with weights
            elif choose == "n":
                load_json_ww()

            # The user selected an undefined option.
            else:
                print("\nSomething went wrong! Try again please.")

        elif choice == "2":
            choose = ask_yes_no("To choose CSV file without weights press y, otherwise press n. (y/n): ")

            # Load the function with the CSV file without weights
            if choose == "y":
                load_csv_wow()

            # Load the function with the CSV file with weights
            elif choose == "n":
                load_csv_ww()

            # The user selected an undefined option.
            else:
                print("\nSomething went wrong! Try again please.")
        elif choice not in range(0, 2):
            print("Choose a correct number described in the menu.")
        # The user selected an undefined option.
        else:
            print("\nSomething went wrong! Try again please.")


if __name__ == '__main__':
    main_menu()

