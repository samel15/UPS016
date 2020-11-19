# Import modules
import csv
import json
import random
from pathlib import Path
import click

# The template of the 'requirements' text file containing names of external modules
requirements = Path.cwd() / "data" / "requirements.txt"
requirements.write_text('External modules:\n')


# Load JSON files - participants without weights
def load_json_wow():
    path = Path.cwd() / "data" / "participants1.json"
    with path.open() as path:
        participants = json.load(path)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.sample(participants, winner)
        print("\nOur reliable lottery machine has chosen lottery winners: ")
        for row in resume:
            lottery_winners = f"\nCongratulations! \n~~ {row['first_name']} {row['last_name']} ~~ You are a winner one"
            print(lottery_winners)
            item_giveaway()


# Load JSON files - participants with weights
# (The weights are to enable the control of the probability of a given participant being drawn.)
def load_json_ww():
    path = Path.cwd() / "data" / "participants2.json"
    with path.open() as path:
        participants = json.load(path)
        weights = []
        for participant in participants:
            weights.append(int(participant['weight']))
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.choices(population=participants, weights=weights, k=winner)
        print("\nOur reliable lottery machine has chosen lottery winners: ")
        for row in resume:
            lottery_winners = f"\nCongratulations! \n~~ {row['first_name']} {row['last_name']} ~~ You are a winner one"
            print(lottery_winners)
            item_giveaway()


# Load CSV files - participants without weights
def load_csv_wow():
    path = Path.cwd() / "data" / "participants1.csv"
    with open(path) as path:
        participants = csv.DictReader(path)
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.sample(list(participants), winner)
        print("\nOur reliable lottery machine has chosen lottery winners: ")
        for row in resume:
            lottery_winners = f"\nCongratulations! \n~~ {row['first_name']} {row['last_name']} ~~ You are a winner one"
            print(lottery_winners)
            item_giveaway()


# Load CSV files - participants with weights
# (The weights are to enable the control of the probability of a given participant being drawn.)
def load_csv_ww():
    """Load a CSV file - participants with weights and draw chosen number of winners"""
    path = Path.cwd() / "data" / "participants2.csv"
    with open(path) as path:
        participants = list(csv.DictReader(path))
        weights = []
        for participant in participants:
            weights.append(int(participant['weight']))
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = random.choices(population=participants, weights=weights, k=winner)
        print("\nOur reliable lottery machine has chosen lottery winners: ")
        for row in resume:
            lottery_winners = f"\nCongratulations! \n~~ {row['first_name']} {row['last_name']} ~~ You are a winner one"
            print(lottery_winners)
            item_giveaway()


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
        print("As a winner you received a prize: ")
        for name_of_prize in prize['prizes']:
            name = (name_of_prize['name'])
            print(name)
        for amount_of_prizes in prize['prizes']:
            amount = (int(amount_of_prizes['amount']))


def separate_prizes():
    """Load the separate prize template"""
    path = Path.cwd() / "data" / "separate_prizes.json"
    with path.open() as path:
        prize = json.load(path)
        print("As a winner you received a prize: ")
        for name_of_prize in prize['prizes']:
            name = print(name_of_prize['name'])
            amount = (int(name_of_prize['amount']))


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
