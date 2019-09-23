from random import randint

# global constants
width = 40
NUM_BOMBS = 10

class Tile:
    def __init__(self):
        self.bomb = False
        
grid = [[Tile() for n in range(9)] for n in range (9)]


#Place 10 bombs at random tiles
for n in range(NUM_BOMB):

    while True:
        x = randint(0, 8)
        y = randint(0, 8)
        if grid[y][x].bomb == False:
            grid[y][x].bomb = True
            break

def setup():
    size(360,360)

def draw():
    y = 0
    for row in grid:
        x = 0
        for tile in row:
            if tile.bomb == True:
                fill(255,0,0)
            else:
                fill(255)
            rect(x, y, width, width)
            x += width
        y+=width

