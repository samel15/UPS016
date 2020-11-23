# Import modules
import csv
import random
import numpy as np

from Prizes import *
from Questions import *


# Load JSON files - participants without weights
def load_json_wow():
    """
    Opens a JSON file without weights, allows to input number of winners, draw them from the file and assign a prize.
    :return: given number of drawn winners from the established range and assigns prizes
    """
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
def load_json_ww():
    """
    Opens a JSON file with weights, allows to input number of winners, draw them from the file and assign a prize.
    :return: given number of drawn, unique winners from the established range and assigns prizes
    """
    path = Path.cwd() / "data" / "participants2.json"
    with path.open() as path:
        participants = json.load(path)
        weights = []
        for participant in participants:
            weights.append(int(participant['weight']))
        weights = np.array(weights, dtype=np.float64)
        weights /= weights.sum()  # normalize
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = np.random.choice(participants, replace=False, p=weights, size=winner)
        print("\nOur reliable lottery machine has chosen lottery winners: ")
        for row in resume:
            lottery_winners = f"\nCongratulations! \n~~ {row['first_name']} {row['last_name']} ~~ You are a winner one"
            print(lottery_winners)
            item_giveaway()


# Load CSV files - participants without weights
def load_csv_wow():
    """
    Opens a CSV file without weights, allows to input number of winners, draw them from the file and assign a prize.
    :return: given number of drawn winners from the established range and assigns prizes
    """
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
def load_csv_ww():
    """
    Opens a CSV file with weights, allows to input number of winners, draw them from the file and assign a prize.
    :return: given number of drawn, unique winners from the established range and assigns prizes
    """
    path = Path.cwd() / "data" / "participants2.csv"
    with open(path) as path:
        participants = list(csv.DictReader(path))
        weights = []
        for participant in participants:
            weights.append(int(participant['weight']))
        weights = np.array(weights, dtype=np.float64)
        weights /= weights.sum()  # normalize
        winner = ask_number("Choose the number of winners (1 - 5):", 1, 6)
        resume = np.random.choice(participants, replace=False, p=weights, size=winner)
        print("\nOur reliable lottery machine has chosen lottery winners: ")
        for row in resume:
            lottery_winners = f"\nCongratulations! \n~~ {row['first_name']} {row['last_name']} ~~ You are a winner one"
            print(lottery_winners)
            item_giveaway()
