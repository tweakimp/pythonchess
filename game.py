from random import choice

import bishop
import board
import king
import knight
import queen
import rook

randomStart = str(choice(board.files[1:])) + str(choice(board.ranks[1:]))

choice([knight.knightMoves, bishop.bishopMoves, rook.rookMoves,
        queen.queenMoves, king.kingMoves])(randomStart)
