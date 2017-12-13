from random import randint
from random import choice
from string import ascii_uppercase

boardWidth = 8
boardHeight = 8

boardFiles = "0" + ascii_uppercase[:boardWidth]
boardRanks = range(1, boardHeight + 1)

def letterNumberSwap(x):
    # change letter to number
    return boardFiles.index(x)

def numberLetterSwap(x):
    # change number to letter
    return boardFiles[x]

# a or an depending on boardWidth
if(boardWidth in (8,11)):
    aORan = "an"
else:
    aORan = "a"

def knightMoves(position):
    print(f"On {aORan} {boardWidth}*{boardHeight} board a Knight on {position.upper()} can go to:")
    # calculate all knight moves from position
    file = letterNumberSwap((position[0]).upper())
    rank = position[1:]
    f,r = int(file), int(rank)
    directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

    for direction in directions:
        testfile = f + direction[0]
        testrank = r + direction[1]
        if testfile in range(1,boardWidth+1) and testrank in boardRanks:
            print (f"{numberLetterSwap(testfile)}{testrank}",end=' ')

#TEST
#knightMoves("a8")
