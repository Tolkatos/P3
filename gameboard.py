import json

class Gameboard:
    def __init__(self, config_file, nbr_total_item):
        with open(config_file, 'r') as file:
            config = json.load(file)
        self.gameboard = config
        self.nbr_total_item = nbr_total_item

    def display(self):
        """Fonction qui affiche le gameboard"""
        for liste in self.gameboard:
            for element in liste:
                print(element, end = "")
            print("")
