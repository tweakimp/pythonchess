import importlib
from datetime import datetime

import chessboard
import lists
import pieces


def stopwatch(f):
    def wrap(*args, **kw):
        start = datetime.now()
        result = f(*args, **kw)
        end = datetime.now()
        print(end - start)
        return result
    return wrap

# TODO: count number of moves
# TODO: track captured pieces
# TODO: track time since move


class Game():
    def __init__(self):
        self.testMate()

    def testMoves(self):
        board = chessboard.Chessboard(8, 8)
        board.initTest()
        board.drawBoard()
        for i in board.getAllMoves("b"):
            print(i)

    def testCheck(self):
        board = chessboard.Chessboard(8, 8)
        board.initTest()
        board.drawBoard()
        board.inCheck("w")

    @stopwatch
    def testMate(self):
        for _ in range(0, 1000):
            # print("=== NEW TEST ===")
            board = chessboard.Chessboard(8, 8)
            board.initTest()
            # board.drawBoard()
            if board.inCheckmate("w"):
                print("=== NEW TEST ===")
                print("CHECKMATE")
                board.drawBoard()
            elif board.inCheck("w"):
                # print("CHECK")
                pass
            else:
                # print("King is safe for now.")
                pass
        print("=== END OF TEST ===")

    def testKingPositions(self):
        for _ in range(0, 10):
            board = chessboard.Chessboard(8, 8)
            board.initTest()
            board.drawBoard()


if __name__ == '__main__':
    importlib.reload(chessboard)
    importlib.reload(pieces)
    importlib.reload(lists)
    game = Game()
