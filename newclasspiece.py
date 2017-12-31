import board
import helper
import knight
import draw


class piece:
    # Summons a piece of given color and position
    def __init__(self, color, position):
        # position
        self.position = position.upper()
        # color
        if color == "w":
            self.color = "w"
        elif color == "b":
            self.color = "b"
        else:
            raise Exception("Wrong color (\"w\" or \"b\")")
        # place on board
        file = board.files.index(self.position[0])
        rank = self.position[1:]
        board.matrix[int(file) - 1][int(rank) - 1] = self.short

    def pos(self):
        print(self.position)

    def updateBoard(self, position=None):
        # remove old
        oldfile = board.files.index(((self.position[0]).upper()))
        oldrank = self.position[1:]
        board.matrix[int(oldfile) - 1][int(oldrank) - 1] = "  "
        # place new
        position = position or self.position
        file = board.files.index(((position[0]).upper()))
        rank = position[1:]
        board.matrix[int(file) - 1][int(rank) - 1] = self.short
        # update position
        self.position = position.upper()

    def move(self, target):
        if(self.checkTarget(target)):
            if(board.isEmpty(target)):
                start = (self.position).upper()
                self.updateBoard(target)
                print(f"{self.name} moves: {start} > {target.upper()}")
            else:
                self.capture(target)
        else:
            print("Cant go there")

    def capture(self, target):
        file = helper.let2num((target[0]).upper())
        rank = int(target[1:])
        if(board.puzzlemode):
            print("Capture in puzzlemode")
            start = (self.position).upper()
            self.updateBoard(target)
            print(f"{self.name} captures: {start} > {target.upper()}")
        else:
            opponent = board.matrix[file - 1][rank - 1]
            if(self.color != opponent[:1]):
                start = (self.position).upper()
                self.updateBoard(target)
                print(f"{self.name} captures: {start} > {target.upper()}")
            else:
                print(f"Can't capture piece of same color")

    def checkTarget(self, target):
        moves = knight.knightMoves(self.position)
        if target.upper() in moves:
            return True
        else:
            return False


class Knight(piece):
    def __init__(self, color, position):
        self.name = "Knight"
        self.short = color + "N"
        super().__init__(color, position)


n1 = Knight("w", "a1")
n2 = Knight("b", "c2")
draw.drawMatrix()
n1.move("c2")
draw.drawMatrix()
n1.move("d4")
draw.drawMatrix()
n2.move("e1")
draw.drawMatrix()
"""
helper.inspect(n1)
n1.move("f6")

helper.inspect(n1)
n1.move("A1")
helper.inspect(n1)"""
