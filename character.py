class Character:

    def __init__(self):
        self.pos_y = 0
        self.pos_x = 0
        self.nbr_item = 0


    def move(self, move_input, level):
        if move_input == "z":
            if level.gameboard[self.pos_y - 1][self.pos_x] != 1:
                if level.gameboard[self.pos_y - 1][self.pos_x] == "I":
                    self.nbr_item += 1
                level.gameboard[self.pos_y][self.pos_x] = 0
                self.pos_y -= 1
                level.gameboard[self.pos_y][self.pos_x] = "M"
            else:
                print("Mouvement impossible")
        if move_input == "s":
            if level.gameboard[self.pos_y + 1][self.pos_x] != 1:
                if level.gameboard[self.pos_y + 1][self.pos_x] == "I":
                    self.nbr_item += 1
                level.gameboard[self.pos_y][self.pos_x] = 0
                self.pos_y += 1
                level.gameboard[self.pos_y][self.pos_x] = "M"
            else:
                print("Mouvement impossible")
        if move_input == "q":
            if level.gameboard[self.pos_y][self.pos_x - 1] != 1:
                if level.gameboard[self.pos_y][self.pos_x - 1] == "I":
                    self.nbr_item += 1
                level.gameboard[self.pos_y][self.pos_x] = 0
                self.pos_x -= 1
                level.gameboard[self.pos_y][self.pos_x] = "M"
            else:
                print("Mouvement impossible")
        if move_input == "d":
            if level.gameboard[self.pos_y][self.pos_x + 1] != 1:
                if level.gameboard[self.pos_y][self.pos_x + 1] == "I":
                    self.nbr_item += 1
                level.gameboard[self.pos_y][self.pos_x] = 0
                self.pos_x += 1
                level.gameboard[self.pos_y][self.pos_x] = "M"
            else:
                print("Mouvement impossible")

    def check_item(self, level, keeper):
        if self.pos_y == keeper.pos_y:
            if self.pos_x == keeper.pos_x:
                if level.nbr_total_item == self.nbr_item:
                    print("Victoire")
                    return False
                else:
                    print("Defaite")
                    return False
            return True
        else:
            return True
