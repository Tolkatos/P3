class Character:
    """Class qui représente le personnage

    Attribut(4):
    pos_y : ligne
    pos_x : sprite
    nbr_item : nombre d'objet rammassé
    level : objet de la class Gameboard"""
    def __init__(self, level):
        self.pos_y = 0
        self.pos_x = 0
        self.nbr_item = 0
        self.level = level

    def move(self, move_input):
        """Methode qui gère le déplacement du personnage

        Paramètre(1):
        move_input : contient l'entrée utilisateur"""
        if move_input == "z":
            if self.pos_y - 1 >= 0:
                if self.level.gameboard[self.pos_y - 1][self.pos_x] != 1:
                    if self.level.gameboard[self.pos_y - 1][self.pos_x] == "I":
                        self.nbr_item += 1
                    self.level.gameboard[self.pos_y][self.pos_x] = 0
                    self.pos_y -= 1
                    self.level.gameboard[self.pos_y][self.pos_x] = "M"
                else:
                    print("Mouvement impossible")
            else:
                print("Mouvement impossible")
        if move_input == "s":
            if self.pos_y + 1 <= 14:
                if self.level.gameboard[self.pos_y + 1][self.pos_x] != 1:
                    if self.level.gameboard[self.pos_y + 1][self.pos_x] == "I":
                        self.nbr_item += 1
                    self.level.gameboard[self.pos_y][self.pos_x] = 0
                    self.pos_y += 1
                    self.level.gameboard[self.pos_y][self.pos_x] = "M"
                else:
                    print("Mouvement impossible")
            else:
                print("Mouvement impossible")
        if move_input == "q":
            if self.pos_x - 1 >= 0:
                if self.level.gameboard[self.pos_y][self.pos_x - 1] != 1:
                    if self.level.gameboard[self.pos_y][self.pos_x - 1] == "I":
                        self.nbr_item += 1
                    self.level.gameboard[self.pos_y][self.pos_x] = 0
                    self.pos_x -= 1
                    self.level.gameboard[self.pos_y][self.pos_x] = "M"
                else:
                    print("Mouvement impossible")
            else:
                print("Mouvement impossible")
        if move_input == "d":
            if self.pos_x + 1 <= 14:
                if self.level.gameboard[self.pos_y][self.pos_x + 1] != 1:
                    if self.level.gameboard[self.pos_y][self.pos_x + 1] == "I":
                        self.nbr_item += 1
                    self.level.gameboard[self.pos_y][self.pos_x] = 0
                    self.pos_x += 1
                    self.level.gameboard[self.pos_y][self.pos_x] = "M"
                else:
                    print("Mouvement impossible")
            else:
                print("Mouvement impossible")

    def check_item(self, keeper):
        """Methode qui vérifie le nombre d'item lorsque le personnage
        se présente devant le garde.

        Paramètre(1):
        keeper = objet de la class Keeper"""
        if self.pos_y == keeper.pos_y:
            if self.pos_x == keeper.pos_x:
                if self.level.nbr_total_item == self.nbr_item:
                    print("Victoire")
                    return False
                else:
                    print("Defaite")
                    return False
