from copy import deepcopy
from random import choice
from string import ascii_uppercase

width = 8
height = 8
files = ascii_uppercase[:width]
ranks = range(1, height + 1)
listOfSquares = [x + str(y) for x in files for y in ranks]

firstKing = choice(listOfSquares)
print(firstKing)


def squaresToRemove(firstKing):
    boardfile = int(files.index(firstKing[0].upper()))
    boardrank = int(ranks.index(int(firstKing[1:])))
    f, r = boardfile, boardrank
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1))
    squares = []
    for direction in directions:
        newf = f + direction[0]
        newr = r + direction[1]
        if newf in range(0, width):
            if newr in range(0, height):
                squares.append(f"{files[newf]}{ranks[newr]}")
    return squares


listOfSquaresX = [
    x for x in listOfSquares if x not in squaresToRemove(firstKing)]
secondKing = choice(listOfSquares)
print(secondKing)
