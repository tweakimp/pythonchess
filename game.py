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

    def start(self, board):
        # empty old piecelist
        board.pieceList = {}

        # initiate pieces
        pdict = {name: pieces.Pawn(color,  position)
                 for name, color,  position in lists.pawns}
        ndict = {name: pieces.Knight(color,  position)
                 for name, color,  position in lists.knights}
        bdict = {name: pieces.Bishop(color,  position)
                 for name, color,  position in lists.bishops}
        rdict = {name: pieces.Rook(color,  position)
                 for name, color,  position in lists.rooks}
        qdict = {name: pieces.Queen(color, position)
                 for name, color,  position in lists.queens}
        kdict = {name: pieces.King(color, position)
                 for name, color, position in lists.kings}
        # update piecelist
        board.piecelist.update(pdict)
        board.piecelist.update(ndict)
        board.piecelist.update(bdict)
        board.piecelist.update(rdict)
        board.piecelist.update(qdict)
        board.piecelist.update(kdict)

        # update matrix
        board.updateMatrix()


if __name__ == '__main__':
    game = Game()
