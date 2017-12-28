import board


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


class Knight(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.short = color + "K"

        # position
        file = board.files.index(((self.position[0]).upper()))
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
        self.position = position

    def move(self, target):
        print(f"go to {target}")


k1 = Knight("w", "e4")
k1.move("f6")
