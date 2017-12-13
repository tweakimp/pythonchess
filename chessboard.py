import knight
from random import choice

randomStart = str(choice(knight.boardFiles[1:])) + str(choice(knight.boardRanks))
knight.knightMoves(randomStart)
