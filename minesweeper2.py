# Bomb: represented by *
# Marker: flag to remember locations of bomb
# Solution grid: contains location of all bombs and numbered cells
# known grid: contains the squares that the player knows about
# to open: move data from the solution grid to the known grid when the user makes their selection

import random, time, copy
from termcolor import cprint
from random import randint

#intro

print()
cprint('Welcome to Minesweeper!', 'red')
cprint('################################', 'red')
print()







def reset():
    print("""
    MAIN MENU
    ==========

    For instuctions on how to play type 'I'
    to just play type 'P'

    """)

    choice = input('Type here '),upper()

    if choice == 'I':
        clear()
        print(open('instructions.txt', 'r').read())

        input('press [enter] when ready to play. ')
    elif choice != 'P':
        clear()
        reset()

    grid = [[0 for n in range(columns)] for n in range (rows)]

    for n in range(0, 10):
        placeBomb(b)

def placeBomb(b):
    r = randomint(0, 8)
    c = randomint(0, 8)
    

reset()