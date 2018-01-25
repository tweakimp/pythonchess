import importlib
import os
import re
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
        self.playFromTurnlist("game2")

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
        board.inCheck("w", True)

    def testMate(self):
        for _ in range(0, 10):
            print("=== NEW TEST ===")
            board = chessboard.Chessboard(8, 8)
            board.initTest()
            board.drawBoard()
            if board.inCheckmate("w"):
                # print("=== NEW TEST ===")
                print("CHECKMATE")
                # board.drawBoard()
            elif board.inCheck("w"):
                print("CHECK")
                pass
            else:
                print("King is safe for now.")
                pass
        print("=== END OF TEST ===")

    def testKingPositions(self):
        for _ in range(0, 10):
            board = chessboard.Chessboard(8, 8)
            board.initTest()
            board.drawBoard()

    def importTurnlist(self, logfile):
        # get file content
        path = os.getcwd() + f"\history\{logfile}.txt"
        with open(path, "r", encoding="utf8") as log:
            text = log.read()
        # split between spaces and new lines
        # [:-1] removes newline at the end of files
        splitted = (re.split("[\s|\n]", text))[:-1]
        if len(splitted) % 2 == 1:
            raise ValueError(f"Something wrong with {logfile} file")
        turnlist = []
        for i in range(len(splitted)):
            if i % 2 == 0:
                turnlist.append([splitted[i], splitted[i + 1]])
        # loglist now list of [position, target] - lists moves
        return text, turnlist

    def playFromTurnlist(self, logfile):
        text, turnlist = self.importTurnlist(logfile)
        print(text)
        board = chessboard.Chessboard(8, 8)
        board.initPieces()
        board.drawBoard()
        for move in turnlist:
            board.movePiece(move[0],move[1])
            board.drawBoard()




if __name__ == '__main__':
    importlib.reload(chessboard)
    importlib.reload(pieces)
    importlib.reload(lists)
    game = Game()
