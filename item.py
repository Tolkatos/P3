import random

class Item:
    """Class qui représente les objets.
    Attribut(2):
    pos_y : ligne
    pos_x : sprite"""

    def __init__(self, gameboard):
        """Constructeur. Prends la structure en argument"""

        self.pos_y, self.pos_x = self.random_pos(gameboard)

    def random_pos(self, gameboard):
        """Methode qui défini une position aléatoire.
        Prends la structure en argument"""

        i = True
        while i:
            pos_y = random.randint(0, 14)
            pos_x = random.randint(0, 14)
            if gameboard[pos_y][pos_x] == 0:
                i = False
        return pos_y, pos_x
