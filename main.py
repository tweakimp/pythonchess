import importlib
import os
import re

from gui import gui
from ressources import chessboard, pieces
from ressources.standard import start


class Game():
    def __init__(self):
        # self.playWithGui()
        self.testCheck()
        # self.playFromTurnlist("game2")

    def playWithGui(self):
        board = chessboard.Chessboard(8, 8)
        board.initTest()
        gui.GUI(board)

    def testMoves(self):
        board = chessboard.Chessboard(8, 8)
        board.initTest()
        board.drawBoard()
        for i in board.getAllMoves("b"):
            print(i)

    def testCheck(self):
        for _ in range(0, 1):
            print("=== NEW TEST ===")
            board = chessboard.Chessboard(8, 8)
            board.initTest()
            if board.inCheck("w"):
                print("CHECK")
                pass
            else:
                print("King is safe for now.")
                pass
            board.showAllMoves("w")
            # board.drawBoard()
        print("=== END OF TEST ===")

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
        path = os.getcwd() + f"/ressources/replays/{logfile}.txt"
        with open(path, "r", encoding="utf8") as log:
            text = log.read()
        # split between spaces and new lines
        # [:-1] removes newline at the end of files
        splitted = (re.split("[\s|\n]", text))[:-1]
        if len(splitted) % 2 == 1:
            raise ValueError(f"Something wrong with {logfile} file length")
        turnlist = []
        for i in range(len(splitted)):
            if i % 2 == 0:
                turnlist.append([splitted[i], splitted[i + 1]])
        # loglist now list of [position, target] - lists moves
        return text, turnlist

    def playFromTurnlist(self, logfile):
        text, turnlist = self.importTurnlist(logfile)
        board = chessboard.Chessboard(8, 8)
        board.initPieces()
        board.drawBoard()
        for move in turnlist:
            print(*move)
            board.movePiece(move[0], move[1])
            board.drawBoard()


if __name__ == '__main__':
    importlib.reload(chessboard)
    importlib.reload(pieces)
    importlib.reload(start)
    importlib.reload(gui)
    game = Game()
