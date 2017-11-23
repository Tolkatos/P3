import random

class Item:

	def __init__(self):
            self.pos_y = random.randint(0, 13)
            self.pos_x = 0

	def random_position(self, position, y):
            i = 0
            while i == 0:
                x = random.randint(0, 13)
                if position[y][x] == 0:
                    i += 1
            return x


