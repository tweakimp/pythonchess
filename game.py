from random import choice
import board
import knight
import king


randomStart = str(choice(board.files[1:])) + str(choice(board.ranks))
knight.knightMoves(randomStart)
print(" ")
print(" ")
king.kingMoves(randomStart)
print(" ")
print(" ")
square = board.squareColor(randomStart)
print(f"The square {randomStart} is {square}.")
print(" ")
print(" ")
