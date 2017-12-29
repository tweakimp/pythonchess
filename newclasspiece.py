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

    def pos(self):
        print(self.position)


class Knight(piece):
    def __init__(self, color, position):

        self.name = "Knight"
        super().__init__(color, position)
        self.short = color + "N"

        # position
        file = board.files.index(self.position[0])
        rank = self.position[1:]
        board.matrix[int(file) - 1][int(rank) - 1] = self.short

    def place(self, position=None):
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

        start = self.position
        self.place(target)
        print(f"{self.name} goes from {start.upper()} to {target.upper()}")


n1 = Knight("w", "e4")
helper.inspect(n1)
n1.move("f6")
helper.inspect(n1)
n1.move("a1")
helper.inspect(n1)
