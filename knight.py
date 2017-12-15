from random import choice
from string import ascii_uppercase
import board
import help

def knightMoves(position):
    # calculate all knight moves from position
    print(f"On {help.aORan} {board.width}*{board.height} board a Knight on {position.upper()} can go to:")
    file = help.letterToNumber((position[0]).upper())
    rank = position[1:]
    f,r = int(file), int(rank)
    directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

    for direction in directions:
        testfile = f + direction[0]
        testrank = r + direction[1]
        if testfile in range(1,board.width+1) and testrank in board.ranks:
            print (f"{help.numberToLetter(testfile)}{testrank}",end=' ')

#TEST
# knightMoves("e5")
