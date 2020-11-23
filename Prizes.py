# Import modules
from pathlib import Path
import json


def item_giveaway():
    """
    Load the giveaway prize template
    :return: prize name
    """
    path = Path.cwd() / "data" / "item_giveaway.json"
    with path.open() as path:
        prize = json.load(path)
        print("As a winner you received a prize: ")
        for name_of_prize in prize['prizes']:
            name = (name_of_prize['name'])
        for amount_of_prizes in prize['prizes']:
            (int(amount_of_prizes['amount']))
        return print(name)


def separate_prizes():
    """
    Load the separate prize template
    :return: prize names
    """
    path = Path.cwd() / "data" / "separate_prizes.json"
    with path.open() as path:
        prize = json.load(path)
        print("As a winner you received a prize: ")
        for name_of_prize in prize['prizes']:
            print(name_of_prize['name'])
            int(name_of_prize['amount'])
