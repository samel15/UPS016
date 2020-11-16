# Import modules
import csv
import json
import random


# Load JSON files - participants without weights
def load_json_wow():
    with open("data\\participants1.json.", "r", encoding="utf-8") as jsonfile:
        participants = json.load(jsonfile)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
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

        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        for row in participants:
            id_lottery = row["id"]
            weight = row["weight"]
            print("id", len(id_lottery))
            print("weight", len(weight))
            resume = random.choices(population=participants, weights=weight, k=winner)
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])
            print("Weight:", row["weight"])


# Load CSV files - participants without weights
def load_csv_wow():
    with open("data\\participants1.csv.", "r", encoding="utf-8") as csvfile:
        participants = csv.DictReader(csvfile)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.sample(list(participants), winner)
        for row in resume:
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])


# Load CSV files - participants with weights
# (The weights are to enable the control of the probability of a given participant being drawn.)
def load_csv_ww():
    with open("data\\participants2.csv.", "r", encoding="utf-8") as csvfile:
        participants_w = csv.DictReader(csvfile)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        for row in participants_w:
            id_lottery = row["id"]
            weight = row["weight"]
            resume = random.choices(population=list(participants_w), weights=weight, k=winner)
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])
            print("Weight:", row["weight"])


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


def item_giveaway():
    """Load the giveaway prize template"""
    with open("data\\item_giveaway.json.", "r", encoding="utf-8") as jsonfile:
        prize = json.load(jsonfile)
        print(prize)


def separate_prizes():
    """Load the separate prize template"""
    with open("data\\separate_prizes.json.", "r", encoding="utf-8") as jsonfile:
        prize = json.load(jsonfile)
        print(prize)


choice = None

# The loop of the lottery menu
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
        input("\nPress 'Enter'' to confirm and close the application: ")
        break

    # Choice 1 - Choose JSON files with or without weights
    elif choice == "1":
        choose = ask_yes_no("To choose JSON file without weights press y, otherwise press n. (y/n): ")

        # Load the function with the JSON file without weights
        if choose == "y":
            load_json_wow()
            item_giveaway()
            separate_prizes()
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

    # The user selected an undefined option.
    else:
        print("\nSomething went wrong! Try again please.")
