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
        board.initTest()
        board.drawBoard()
        print(board.inCheck("w"))


if __name__ == '__main__':
    importlib.reload(chessboard)
    importlib.reload(pieces)
    importlib.reload(lists)
    game = Game()
