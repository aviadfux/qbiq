from rectangle import Object, Item, Rectangle
import numpy as np
import math

class Grid:
    def __init__(self, rows, cols, cell_size):
        self.cell_size = cell_size
        self.matrix = np.full((rows, cols), Rectangle(cell_size))
        self.items = []

    def add_item(self, item):
        self.matrix[item.X, item.Y] = item
        self.items.append(item)

    def add_object(self, object):
        min_score = math.inf
        x_final = 0
        y_final = 0

        for (x, y), value in np.ndenumerate(self.matrix):
            if isinstance(value, Item): continue
            score = object.get_score(self.items, x, y)
            if score < min_score:
                min_score = score
                x_final = x
                y_final = y

        if not isinstance(self.matrix[x_final][y_final], Object):
            self.matrix[x_final][y_final] = object
        else:
            self.collision(X=x_final, Y=y_final, object1=object, object2=self.matrix[x_final][y_final])

    def collision(self, X, Y, object1, object2):
        object1_score = object1.get_score(self.items, X, Y)
        object2_score = object2.get_score(self.items, X, Y)

        if object1_score > object2_score:
            self.matrix[X][Y] = Item(self.cell_size, X, Y, is_temp=True)
            self.add_object(object2)
            self.matrix[X][Y] = object1
        else:
            self.matrix[X][Y] = Item(self.cell_size, X, Y, is_temp=True)
            self.add_object(object1)
            self.matrix[X][Y] = object2

    def print(self):
        rows, cols = self.matrix.shape
        for i in range(rows):
            for j in range(cols):
                value = self.matrix[i][j]
                if isinstance(value, Item):
                    print("| I |", end="")
                elif isinstance(value, Object):
                    print("| O |", end="")
                else:
                    print("| R |", end="")
            print("\n")
