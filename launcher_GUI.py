#! /usr/bin/python3
# coding : utf-8
import sys
import pygame
from character import Character
from gameboard import Gameboard
from item import Item
from keeper import Keeper
from config import *


class GUIApplication:
    """Class qui gère l'execution du jeux."""

    def __init__(self, config_file, nbr_total_item):
        """Constructeur.

        Argument(2):
        config_file : structure du labyrinthe
        nbr_total_item : nombre total d'objet présent dans la structure"""

        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
        pygame.display.set_caption("P3 : labyrinthe")
        font = pygame.font.Font(None, 64)
        self.text_victoire = font.render("Victoire !", 1, (0, 255, 0))
        self.text_defeat = font.render("Défaite !", 1, (255, 0, 0))
        self.level = Gameboard(config_file, nbr_total_item)
        self.character = Character(self.level)
        self.keeper = Keeper()
        i = 0
        while i < nbr_total_item:
            self.item = Item(self.level.gameboard)
            self.level.gameboard[self.item.pos_y][self.item.pos_x] = "I"
            i += 1

    def event_keyboard(self):
        """Methode qui lit l'entrée clavier"""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return "z"
                if event.key == pygame.K_DOWN:
                    return "s"
                if event.key == pygame.K_RIGHT:
                    return "d"
                if event.key == pygame.K_LEFT:
                    return "q"
            elif event.type == pygame.QUIT: sys.exit()

    def display_GUI(self, img):
        """Methoque qui affiche le gameboard de manière graphique

        Paramètre(1):
        img = dictionnaire contenant les images"""

        for pos_y in range(NBR_LIGNE):
            for pos_x in range(NBR_SPRITE):
                if self.level.is_a_floor(pos_x, pos_y):
                    self.window.blit(img[0], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
                elif self.level.is_a_wall(pos_x, pos_y):
                    self.window.blit(img[1], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
                elif self.level.is_a_item(pos_x, pos_y):
                    self.window.blit(img[0], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
                    self.window.blit(img["I"], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
                elif self.level.is_a_keeper(pos_x, pos_y):
                    self.window.blit(img[0], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
                    self.window.blit(img["G"], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
                elif self.level.is_a_character(pos_x, pos_y):
                    self.window.blit(img[0], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
                    self.window.blit(img["M"], (pos_y * SPRITE_SIZE, pos_x * SPRITE_SIZE))
        pygame.display.flip()

    def run(self, img):
        """Methode qui gère l'execution du programme

        Paramètre(1):
        img : dictionnaire contenant les images"""

        while self.character.check_item(self.keeper):
            move = self.event_keyboard()
            self.character.move(move)
            self.display_GUI(img)



def main():
    continuer = True
    while continuer:
        play = GUIApplication('structure.json', NBR_ITEM)
        img = {
            "M": pygame.image.load("img/character.png").convert_alpha(),
            "G": pygame.image.load("img/keeper.png").convert_alpha(),
            "I": pygame.image.load("img/item.png").convert_alpha(),
            1: pygame.image.load("img/wall.png").convert_alpha(),
            0: pygame.image.load("img/floor.png").convert_alpha()
        }
        play.run(img)
        if play.level.nbr_total_item == play.character.nbr_item:
            play.window.blit(play.text_victoire, (160, 240))
            pygame.display.flip()
            pygame.time.delay(2000)
            continuer = False
        else:
            play.window.blit(play.text_defeat, (160, 240))
            pygame.display.flip()
            pygame.time.delay(2000)
            continuer = True



if __name__ == "__main__":
    main()
