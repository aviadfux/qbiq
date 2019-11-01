import math

class Rectangle:
    def __init__(self, size_side):
        self.size_side = size_side

class Object(Rectangle):
    def __init__(self, size_side, w1, w2, w3, w4):
        Rectangle.__init__(self, size_side)
        self.wights = []
        self.wights.append(w1)
        self.wights.append(w2)
        self.wights.append(w3)
        self.wights.append(w4)

    def get_score(self, items, X, Y):
        score = []
        score += [W * self.calculate_dis(X, Y, item.X, item.Y) for item, W in zip(items, self.wights)]
        return sum(score)

    def calculate_dis(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

class Item(Rectangle):
    def __init__(self, size_side, X, Y, is_temp=False):
        Rectangle.__init__(self, size_side)
        self.X = X
        self.Y = Y
        self.is_temp = is_temp