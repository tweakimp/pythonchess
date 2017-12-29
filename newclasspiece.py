import board
import helper


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
            self.color = ""
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

    def move(self, target):
        if(board.isEmpty(target)):
            start = self.position
            self.updateBoard(target)
            print(f"{self.name} moves from {start.upper()} to {target.upper()}")
        else:
            file = helper.let2num((target[0]).upper())
            rank = int(target[1:])
            print("square is occupied, cant move")
            if(self.color == "w" and board.matrix[file - 1][rank - 1][:1] == "b"):
                print("but can attack the black piece")
            if(self.color == "b" and board.matrix[file - 1][rank - 1][:1] == "w"):
                print("but can attack the white piece")


class Knight(piece):
    def __init__(self, color, position):
        self.name = "Knight"
        self.short = color + "N"
        super().__init__(color, position)


n1 = Knight("w", "e4")
n2 = Knight("b", "a1")
helper.inspect(n1)
n1.move("f6")
helper.inspect(n1)
n1.move("A1")
helper.inspect(n1)

"""for line in board.matrix:
    print(line)"""
