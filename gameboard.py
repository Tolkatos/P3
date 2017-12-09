import json


class Gameboard:
    """Class qui charge le fichier de configuration
    et représente la structure du plateau de jeu

    Attribut(2):
    gameboard : plateau de jeu
    nbr_total_item : nombre total d'objet présent dans le jeu"""
    def __init__(self, config_file, nbr_total_item):
        with open(config_file, 'r') as file:
            config = json.load(file)
        self.gameboard = config
        self.nbr_total_item = nbr_total_item

    def is_a_wall(self, x, y):
        """Méthode qui vérifie si les coordonnées pointent sur un mur"""
        if self.gameboard[x][y] == 1:
            return True
        else:
            return False

    def is_a_floor(self, x, y):
        """Méthode qui vérifie si les coordonnées pointent sur un passage"""
        if self.gameboard[x][y] == 0:
            return True
        else:
            return False
