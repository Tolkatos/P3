#! /usr/bin/python3
# coding : utf-8

from gameboard import *
from item import *
from character import *

level = Gameboard('config.json')
character = Character()

i = 0
while i < 3:
    item_i = Item()
    item_i.pos_x = item_i.random_position(level.gameboard, item_i.pos_y)
    level.pos_item_i_x = item_i.pos_x
    level.pos_item_i_y = item_i.pos_y
    level.gameboard[level.pos_item_i_y][level.pos_item_i_x] = "I"
    i += 1


level.display(level.gameboard)
j = 0
while j < 2000:
    print("\n")
    move = input("Déplacement : z (haut), s (bas), q (gauche), d (droite) \n")
    character.move(move, character, level)
    character.check_item(level, character)
    level.display(level.gameboard)
    print("\n")
    print("Nombre d'objet : ", character.nbr_item)

