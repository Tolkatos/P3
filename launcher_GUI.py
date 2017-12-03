import pygame
from character import *
from gameboard import *
from item import *
from keeper import *

class GUIApplication:

    def __init__(self, config_file, nbr_total_item):
        pygame.init()
        self.window = pygame.display.set_mode((480, 480))
        self.level = Gameboard(config_file, nbr_total_item)
        self.character = Character(self.level)
        self.keeper = Keeper()
        i = 0
        while i < nbr_total_item:
            self.item_i = Item()
            self.item_i.pos_x = self.item_i.random_pos(self.level.gameboard)
            self.level.gameboard[self.item_i.pos_y][self.item_i.pos_x] = "I"
            i += 1

    def event_keyboard(self):
        for event in pygame.event.get():
            if event == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.character.move("z", self.level)
                if event.key == pygame.K_DOWN:
                    self.character.move("s", self.level)
                if event.key == pygame.K_RIGHT:
                    self.character.move("d", self.level)
                if event.key == pygame.K_LEFT:
                    self.character.move("q", self.level)

    def display_GUI(self, img):
        y = 0
        x = 0
        while y <= 14:
            while x <= 14:
                if self.level.gameboard[y][x] == 0:
                    self.window.blit(img[0], (y * 32, x * 32))
                if self.level.gameboard[y][x] == 1:
                    self.window.blit(img[1], (y * 32, x * 32))
                if self.level.gameboard[y][x] == "M":
                    self.window.blit(img[0], (y * 32, x * 32))
                    self.window.blit(img["M"], (y * 32, x * 32))
                if self.level.gameboard[y][x] == "G":
                    self.window.blit(img[0], (y * 32, x *32))
                    self.window.blit(img["G"], (y * 32, x * 32))
                if self.level.gameboard[y][x] == "I":
                    self.window.blit(img[0], (y * 32, x * 32))
                    self.window.blit(img["I"], (y * 32, x * 32))
                x += 1
            x = 0
            y += 1
        pygame.display.flip()

    def run(self, img):
        self.display_GUI(img)
        while self.character.check_item(self.keeper):
            self.event_keyboard()
            self.character.check_item(self.keeper)
            self.display_GUI(img)


def main():
    play = GUIApplication('config.json', 3)
    img = {
    "M" : pygame.image.load("img/character.png").convert_alpha(),
    "G" : pygame.image.load("img/keeper.png").convert_alpha(),
    "I" : pygame.image.load("img/item.png").convert_alpha(),
    1 : pygame.image.load("img/wall.png").convert_alpha(),
    0 : pygame.image.load("img/floor.png").convert_alpha()
    }
    play.run(img)

if __name__ == "__main__":
    main()
