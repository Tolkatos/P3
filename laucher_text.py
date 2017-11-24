#! /usr/bin/python3
# coding : utf-8

from gameboard import *
from item import *
from character import *

#class TextApplication:
#
#    def __init__(self):
#        self.level = Gameboard('config.json')
#        self.character = Character()
#
#    def run(self):
#        pass



level = Gameboard('config.json')
character = Character()

i = 0
while i < 3:
    item_i = Item()
    item_i.pos_x = item_i.random_position(level.gameboard)
    level.pos_item_i_x = item_i.pos_x
    level.pos_item_i_y = item_i.pos_y
    level.gameboard[level.pos_item_i_y][level.pos_item_i_x] = "I"
    i += 1


level.display()


#Nouvelle boucle pour relancer le jeu sur demande de l'utilisateur
while character.check_item(level) == True:
    print("\n")
    move = input("Déplacement : z (haut), s (bas), q (gauche), d (droite) \n")
    character.move(move, level)
    character.check_item(level)
    level.display()
    print("\n")
    print("Nombre d'objet : ", character.nbr_item)
