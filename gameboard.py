import json

class Gameboard:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
        self.gameboard = config
        self.nbr_total_item = 3
        self.pos_item_1_y = 0
        self.pos_item_1_x = 0
        self.pos_item_2_y = 0
        self.pos_item_2_x = 0
        self.pos_item_3_y = 0
        self.pos_item_3_x = 0
        self.pos_character_y = 0
        self.pos_character_x = 0
        self.pos_keeper_y = 13
        self.pos_keeper_x = 14

    def display(self, gameboard):
        """Fonction qui affiche le gameboard"""
        for liste in gameboard:
            for element in liste:
                print(element, end = "")
            print("")

