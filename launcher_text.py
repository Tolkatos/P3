#! /usr/bin/python3
# coding : utf-8

from gameboard import *
from item import *
from character import *
from keeper import *

class TextApplication:

    def __init__(self, config_file, nbr_total_item):
        self.level = Gameboard(config_file, nbr_total_item)
        self.character = Character()
        self.keeper = Keeper()
        i = 0
        while i < nbr_total_item:
            self.item_i = Item()
            self.item_i.pos_x = self.item_i.random_position(self.level.gameboard)
            self.level.gameboard[self.item_i.pos_y][self.item_i.pos_x] = "I"
            i += 1

    def run(self):
        self.level.display()
        #Nouvelle boucle pour relancer le jeu sur demande de l'utilisateu
        while self.character.check_item(self.level, self.keeper):
            print("\n")
            move = input("Déplacement : z (haut), s (bas), q (gauche), d (droite) \n")
            self.character.move(move, self.level)
            self.character.check_item(self.level, self.keeper)
            self.level.display()
            print("\n")
            print("Nombre d'objet : ", self.character.nbr_item)



play = TextApplication('config.json', 5)
play.run()
