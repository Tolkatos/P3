class Character:

    def __init__(self):
        self.pos_y = 0
        self.pos_x = 0
        self.nbr_item = 0


    def move(self, move_input, character, level):
        if move_input == "z":
            if level.gameboard[level.pos_character_y - 1][level.pos_character_x] != 1:
                if level.gameboard[level.pos_character_y - 1][level.pos_character_x] == "I":
                    character.nbr_item += 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = 0
                character.pos_y -= 1
                level.pos_character_y -= 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = "M"
            else:
                print("Mouvement impossible")
        if move_input == "s":
            if level.gameboard[level.pos_character_y + 1][level.pos_character_x] != 1:
                if level.gameboard[level.pos_character_y + 1][level.pos_character_x] == "I":
                    character.nbr_item += 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = 0
                character.pos_y += 1
                level.pos_character_y += 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = "M"
            else:
                print("Mouvement impossible")
        if move_input == "q":
            if level.gameboard[level.pos_character_y][level.pos_character_x - 1] != 1:
                if level.gameboard[level.pos_character_y][level.pos_character_x - 1] == "I":
                    character.nbr_item += 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = 0
                character.pos_x -= 1
                level.pos_character_x -= 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = "M"
            else:
                print("Mouvement impossible")
        if move_input == "d":
            if level.gameboard[level.pos_character_y][level.pos_character_x + 1] != 1:
                if level.gameboard[level.pos_character_y][level.pos_character_x + 1] == "I":
                    character.nbr_item += 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = 0
                character.pos_x += 1
                level.pos_character_x += 1
                level.gameboard[level.pos_character_y][level.pos_character_x] = "M"
            else:
                print("Mouvement impossible")

    def check_item(self, level, character):
        if level.pos_character_y == level.pos_keeper_y:
            if level.pos_character_x == level.pos_keeper_x:
                if level.nbr_total_item == character.nbr_item:
                    print("Victoire")
                else:
                    print("Defaite")
