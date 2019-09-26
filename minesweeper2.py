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

    choice = input('Type here ').upper()

    if choice == 'I':

        print(open('instructions.txt', 'r').read())

        input('press [enter] when ready to play. ')
    elif choice != 'P':

        reset()

    b = [[0 for n in range(9)] for n in range (9)]

    for n in range(0, 10):
        place_bomb(b)
    
    print(b)

def place_bomb(b):
    r = randint(0, 8)
    c = randint(0, 8)
    current_row = b[r]
    if not current_row[c] == '*':
        current_row[c] == '*'
    else:
        place_bomb(b)


reset()