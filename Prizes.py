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
        prizes = []
        for name_of_prize in prize['prizes']:
            name = name_of_prize['name']
            prizes.append(name)
            prizes.append(name)
            prizes.append(name)
        return prizes


def separate_prizes():
    """
    Load the separate prize template
    :return: prize names
    """
    path = Path.cwd() / "data" / "separate_prizes.json"
    with path.open() as path:
        prize = json.load(path)
        prizes = []
        for name_of_prize in prize['prizes']:
            name = name_of_prize['name']
            prizes.append(name)
        return prizes
