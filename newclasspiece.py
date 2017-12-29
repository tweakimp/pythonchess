import board
import helper


class piece:
    # Summons a piece of given color and position
    def __init__(self, color, position):
        # position
        self.position = position.upper()
        # color
        if color == "w":
            self.color = "white"
        elif color == "b":
            self.color = "black"
        else:
            self.color = "none"
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

    def attacking(self):
        list = ["A1", "B2", "C6"]
        return list


class Knight(piece):
    def __init__(self, color, position):
        self.name = "Knight"
        self.short = color + "N"
        super().__init__(color, position)

    def move(self, target):
        # check if square is empty
        # if not: check if
        # if print("square is occupied, cant move")
        start = self.position
        self.updateBoard(target)
        print(f"{self.name} goes from {start.upper()} to {target.upper()}")


n1 = Knight("w", "e4")
helper.inspect(n1)
n1.move("f6")
helper.inspect(n1)
n1.move("a1")
helper.inspect(n1)

for i in n1.attacking():
    print(i, end=" ")
