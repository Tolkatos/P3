#! /usr/bin/python3
# coding : utf-8

from gameboard import *
from item import *
from character import *
from keeper import *


class TextApplication:

    def __init__(self, config_file, nbr_total_item):
        self.level = Gameboard(config_file, nbr_total_item)
        self.character = Character(self.level)
        self.keeper = Keeper()
        i = 0
        while i < nbr_total_item:
            self.item_i = Item()
            self.item_i.pos_x = self.item_i.random_pos(self.level.gameboard)
            self.level.gameboard[self.item_i.pos_y][self.item_i.pos_x] = "I"
            i += 1

    def display_text(self):
        """Methode gère l'affichage text"""
        for liste in self.level.gameboard:
            for element in liste:
                print(element, end="")
            print("")

    def run(self):
        self.display_text()
        while self.character.check_item(self.keeper):
            print("Objet rammassé : ", self.character.nbr_item)
            move = input("Déplacement : z/s/q/d \n")
            self.character.move(move)
            self.character.check_item(self.keeper)
            self.display_text()
            print("\n")


def main():
    play = TextApplication('config.json', 3)
    play.run()

if __name__ == "__main__":
    main()
