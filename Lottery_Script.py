# Import modules
import csv
import json
import random
from pathlib import Path


# Load JSON files - participants without weights
def load_json_wow():
    path = Path.cwd() / "data" / "participants1.json"
    with path.open() as path:
        participants = json.load(path)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.sample(participants, winner)
        for row in resume:
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])


# Load JSON files - participants with weights
# (The weights are to enable the control of the probability of a given participant being drawn.)
def load_json_ww():
    path = Path.cwd() / "data" / "participants2.json"
    with path.open() as path:
        participants = json.load(path)
        participant = {}
        ids = []
        weights = []
        for participant in participants:
            ids.append(participant['id'])
            weights.append(participant['weight'])
        print("ID", ids, "WAGI", weights, "Wszystko", participants)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.choices(population=ids, weights=weights, k=winner)
        for row in resume:
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])
            print("Weight:", row["weight"])


# Load CSV files - participants without weights
def load_csv_wow():
    path = Path.cwd() / "data" / "participants1.csv"
    with open(path) as path:
        participants = csv.DictReader(path)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.sample(list(participants), winner)
        for row in resume:
            print("\n ", "ID:", row["id"])
            print("First Name:", row["first_name"])
            print("Last Name:", row["last_name"])


# Load CSV files - participants with weights
# (The weights are to enable the control of the probability of a given participant being drawn.)
def load_csv_ww():
    """Load a CSV file - participants with weights and draw chosen number of winners"""
    path = Path.cwd() / "data" / "participants2.csv"
    with open(path) as path:
        participants = csv.DictReader(path)
        participants = list(participants)
        participant = {}
        ids = []
        weights = []
        for participant in participants:
            ids.append(participant['id'])
            weights.append(participant['weight'])
        print("ID", ids, "WAGI", weights, "Wszystko", participants)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.choices(population=participants, weights=weights, k=winner)
        for row in resume:
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
    path = Path.cwd() / "data" / "item_giveaway.json"
    with path.open() as path:
        prize = json.load(path)
        print(prize)
        print(type(prize))
        print(prize.keys())
        prizes = print(prize['prizes'])
        print(type(prizes))
        prizes = list
        print(type(prizes))
        print(prizes)
        print(prizes['name'])
        # for row in list_of_prizes:
        #     print(row['name'])
        # print(name_of_prize)
        # for prize_w in prize:
        #     ids.append(participant['id'])
        #     weights.append(participant['weight'])


def separate_prizes():
    """Load the separate prize template"""
    path = Path.cwd() / "data" / "separate_prizes.json"
    with path.open() as path:
        prize = json.load(path)
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
            #separate_prizes()
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
