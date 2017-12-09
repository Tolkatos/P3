import random


class Item:
    """Class qui représente les objets
    Attribut(2):
    pos_y : ligne (défini aléatoirement dans la constructeur)
    pos_x : sprite"""
    def __init__(self):
        self.pos_y = random.randint(0, 14)
        self.pos_x = 0

    def random_pos(self, gameboard):
        """Methode qui défini une position aléatoire"""
        i = 0
        while i == 0:
            pos_x = random.randint(0, 14)
            if gameboard[self.pos_y][pos_x] == 0:
                i += 1
        return pos_x
