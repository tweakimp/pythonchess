from random import choice

import bishop
import board
import king
import knight
import queen
import rook

randomStart = str(choice(board.files[1:])) + str(choice(board.ranks))
knight.knightMoves(randomStart)
print(" ")
print(" ")
bishop.bishopMoves(randomStart)
print(" ")
print(" ")
rook.rookMoves(randomStart)
print(" ")
print(" ")
king.kingMoves(randomStart)
print(" ")
print(" ")
queen.queenMoves(randomStart)
print(" ")
print(" ")
square = board.squareColor(randomStart)
print(f"The square {randomStart} is {square}.")
