import importlib

import chessboard
import lists
import pieces

# TODO: count number of moves
# TODO: track captured pieces
# TODO: track time since move


class Game():
    def __init__(self):
        board = chessboard.Chessboard(8, 8)
        self.start(board)
        board.printInfo()
        print("wQknight: ", end="")
        board.piecelist["wQknight"].move(board)
        print("wKknight: ", end="")
        board.piecelist["wKknight"].move(board)
        print("bQknight: ", end="")
        board.piecelist["bQknight"].move(board)
        print("bKknight: ", end="")
        board.piecelist["bKknight"].move(board)

    def start(self, board):
        # empty old piecelist
        board.pieceList = {}

        # initiate pieces and update piecelist
        board.piecelist.update({name: pieces.Pawn(color, position)
                                for name, color, position in lists.pawns})
        board.piecelist.update({name: pieces.Knight(color, position)
                                for name, color, position in lists.knights})
        board.piecelist.update({name: pieces.Bishop(color, position)
                                for name, color, position in lists.bishops})
        board.piecelist.update({name: pieces.Rook(color, position)
                                for name, color, position in lists.rooks})
        board.piecelist.update({name: pieces.Queen(color, position)
                                for name, color, position in lists.queens})
        board.piecelist.update({name: pieces.King(color, position)
                                for name, color, position in lists.kings})

        # update matrix
        board.updateMatrix()

    def movePiece(self, board, name, newposition):
        pass


if __name__ == '__main__':
    importlib.reload(chessboard)
    importlib.reload(pieces)
    game = Game()
