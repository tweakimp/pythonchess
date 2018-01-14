import chessboard


class Game():
    def __init__(self):
        board = chessboard.Board(8, 8)
        board.printInfo()


if __name__ == '__main__':
    game = Game()
