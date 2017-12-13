import pieces.knight
from random import choice

randomStart = str(choice(pieces.knight.boardFiles[1:])) + str(choice(pieces.knight.boardRanks))
pieces.knight.knightMoves(randomStart)
