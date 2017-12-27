from random import choice

import bishop
import board
import draw
import help
import king
import knight
import queen
import rook
import status

randomStart = str(choice(board.files[1:])) + str(choice(board.ranks[1:]))

choice([knight.knightMoves, bishop.bishopMoves, rook.rookMoves,
        queen.queenMoves, king.kingMoves])(randomStart)
