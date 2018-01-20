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
        # board.initiatePieces()
        board.initTest()
        board.pieceShowMoves("test1")
        board.drawBoard()
        # board.printInfo()
        # print("wBbishop: ", board.piecelist["wBbishop"].position)
        # print(board.piecelist["wBbishop"].move(board))
        # print("bBbishop: ", board.piecelist["bBbishop"].position)
        # print(board.piecelist["bBbishop"].move(board))

    def movePiece(self, board, name, newposition):
        pass


if __name__ == '__main__':
    importlib.reload(chessboard)
    importlib.reload(pieces)
    importlib.reload(lists)
    game = Game()
