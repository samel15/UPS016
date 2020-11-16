# Import modules
import csv
import json
import random


# Load JSON files - participants without weights
def load_json_wow():
    with open("data\\participants1.json.", "r", encoding="utf-8") as jsonfile:
        participants = json.load(jsonfile)
        winner = ask_number("Choose the number of winners (1 - 10):", 1, 11)
        resume = random.sample(participants, winner)
        for row in resume:
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])


# Load JSON files - participants with weights
# (The weights are to enable the control of the probability of a given participant being drawn.)
def load_json_ww():
    with open("data\\participants2.json.", "r", encoding="utf-8") as jsonfile:
        participants = json.load(jsonfile)
        winner = ask_number("Choose the number of winners (1 - 10):", 1, 11)
        for row in participants:
            id_lottery = row["id"]
            weight = row["weight"]
            print("parti", len(participants))
            print("waga", len(weight))
            print("id", len(id_lottery))
            resume = random.choices(population=participants, weights=weight, k=winner)
            '''print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])
            print("Weight:", row["weight"])
'''


# Load CSV files - participants without weights
def load_csv_wow():
    with open("data\\participants1.csv.", "r", encoding="utf-8") as csvfile:
        participants = csv.DictReader(csvfile)
        winner = ask_number("Choose the number of winners (1 - 10):", 1, 11)
        resume = random.sample(participants, winner)
        for row in resume:
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])


# Load CSV files - participants with weights
# (The weights are to enable the control of the probability of a given participant being drawn.)
def load_csv_ww():
    with open("data\\participants2.csv.", "r", encoding="utf-8") as csvfile:
        participants_w = csv.DictReader(csvfile)
        winner = ask_number("Choose the number of winners (1 - 10):", 1, 11)
        for row in participants_w:
            id_lottery = row["id"]
            weight = row["weight"]
            print("parti", len(participants_w))
            print("waga", len(weight))
            print("id", len(id_lottery))
            resume = random.choices(population=participants_w, weights=weight, k=winner)
            '''print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])
            print("Weight:", row["weight"])
'''


def ask_yes_no(question):
    """Ask the question yes or no"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Enter the number of winners"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


choice = None

# The loop of the lottery menu
while choice != 0:
    print(
        """
    The lottery menu

    0 - Close the application
    1 - Choose a file with or without weights
    """
    )
    choice = input("Choose: ")

    # Choice 0 - Exit the application
    if choice == "0":
        input("\nPress 'Enter'' to close the application: ")
        break

    # Choice 1 - choose a file with or without weights
    elif choice == "1":
        choose = ask_yes_no("To choose a file without weights press y, otherwise press n. (y/n): ")

        # Load the function with the JSON file without weights
        if choose == "y":
            load_json_wow()

        # Load the function with the JSON file with weights
        elif choose == "n":
            load_json_ww()

        # The user selected an undefined option.
        else:
            print("\nSomething went wrong! Try again please.")

    # The user selected an undefined option.
    else:
        print("\nSomething went wrong! Try again please.")
