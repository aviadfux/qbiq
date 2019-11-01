from grid import Grid
from rectangle import Object, Item

RECT_SIZE = 10

grid = Grid(10, 10, RECT_SIZE)

item1 = Item(RECT_SIZE, X=2, Y=2)
item2 = Item(RECT_SIZE, X=4, Y=5)
item3 = Item(RECT_SIZE, X=6, Y=3)
item4 = Item(RECT_SIZE, X=7, Y=8)

grid.add_item(item1)
grid.add_item(item2)
grid.add_item(item3)
grid.add_item(item4)

object1 = Object(RECT_SIZE, w1=3, w2=6, w3=2, w4=5)
object2 = Object(RECT_SIZE, w1=1, w2=5, w3=8, w4=2)
object3 = Object(RECT_SIZE, w1=6, w2=12, w3=4, w4=10)

grid.add_object(object1)
grid.add_object(object2)
grid.add_object(object3)

grid.print()