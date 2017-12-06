import json


class Gameboard:
    def __init__(self, config_file, nbr_total_item):
        with open(config_file, 'r') as file:
            config = json.load(file)
        self.gameboard = config
        self.nbr_total_item = nbr_total_item
