from random import randint

# global constants
width = 40
num_bombs = 10
rows = 9
columns = 9

class Tile:
    def __init__(self):
        self.bomb = False
        
grid = [[Tile() for n in range(columns)] for n in range (rows)]

#Place 10 bombs at random tiles
for n in range(num_bombs):

    while True:
        x = randint(0, 8)
        y = randint(0, 8)
        if grid[y][x].bomb == False:
            grid[y][x].bomb = True
            break

def setup():
    size(360,360)

# Build our grid
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

draw()

def mousePressed:
    x = mouseX/width
    y = mouseY/width

    s = 0
    for (dx, dy) in [(0, 1), (0,-1), (1,0), (-1,0), (1, 1), (1,-1), (-1, -1), (-1, 1)]: 
        if inbounds(x + dx, y + dy)  and grid[y + dy][x + dx].bomb:
            s += 1
    print s

def inbounds(x, y):
    if x >= 0 and x < columns and y > 0 and y < rows:
        return True
    return False