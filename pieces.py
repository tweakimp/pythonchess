class Piece():
    def __init__(self, color, position):
        if color == "w" or "b":
            self.color = color
        else:
            raise Exception("Wrong color (\"w\" or \"b\")")
        # place on board
        self.position = position.upper()
        self.unmoved = True
        self.piece = self.__class__.__name__
        self.name = "White " + self.piece if color == "w" else \
                    "Black " + self.piece

    def freePath(self, board, target):
        if board.checkSquare(target) is None:
            return True
        elif board.checkSquare(target) == self.color:
            return False
        else:
            return "capture"

    def validate(self, board, target, notifications=False):
        valid = []
        pathblocked = False
        if board.checkSquare(target) is None:
            valid.append(target)
        elif board.checkSquare(target) == self.color:
            if notifications is True:
                print(f"{self.name} path blocked at {target}.")
            pathblocked = True
        else:
            valid.append(target)
            if notifications is True:
                print(f"{self.name} can capture at {target}.")
            pathblocked = True
        if self.__class__.__name__ in ["Bishop", "Rook", "Queen"]:
            return valid, pathblocked
        else:
            return valid


class Pawn(Piece):
    def __init__(self, color, position):
        self.short = color + "P"
        super().__init__(color, position)

    def move(self, board, notifications=False):

        # calculate all rook moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = board.ranks.index(int(self.position[1:]))
        f, r = int(boardfile), int(boardrank)
        moves = []
        # move without capture
        if(self.color == "w"):
            directions = ((0, 1),)
            if(boardrank == 1):
                directions = directions + ((0, 2),)
        else:
            directions = ((0, -1),)
            if(boardrank == 6):
                directions = directions + ((0, -2),)
        for direction in directions:
            newf = f + direction[0]
            newr = r + direction[1]
            if newf in range(0, board.width):
                if newr in range(0, board.height):
                    square = f"{board.files[newf]}{board.ranks[newr]}"
                    if board.checkSquare(square) is None:
                        moves.append(square)
                    else:
                        if notifications is True:
                            print(f"{self.name} path blocked at {square}.")
                        break
        # move with capture
        if(self.color == "w"):
            directions = ((-1, 1), (1, 1))
        else:
            directions = ((-1, -1), (1, -1))
        for direction in directions:
            newf = f + direction[0]
            newr = r + direction[1]
            if newf in range(0, board.width):
                if newr in range(0, board.height):
                    square = f"{board.files[newf]}{board.ranks[newr]}"
                    check = board.checkSquare(square)
                    if check is not None and check != self.color:
                        if notifications is True:
                            print(f"{self.name} can capture at {square}.")
                        moves.append(square)
        return moves


class Knight(Piece):
    def __init__(self, color, position):
        self.short = color + "N"
        super().__init__(color,  position)

    def move(self, board):
        # calculate all knight moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = int(board.ranks.index(int(self.position[1:])))
        directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2),
                      (2, -1), (2, 1))
        moves = []
        for direction in directions:
            newf = boardfile + direction[0]
            newr = boardrank + direction[1]
            if newf in range(0, board.width):
                if newr in range(0, board.height):
                    square = f"{board.files[newf]}{board.ranks[newr]}"
                    valid = self.validate(board, square, False)
                    moves += valid
        return moves


class Bishop(Piece):
    def __init__(self, color, position):
        self.short = color + "B"
        super().__init__(color, position)

    def move(self, board):
        # calculate all bishop moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = int(board.ranks.index(int(self.position[1:])))
        f, r = boardfile, boardrank
        moves = []
        # down and left
        if f != 0 and r != 0:
            for i in range(1,  1 + min(f, r)):
                square = f"{board.files[f - i]}{board.ranks[r - i]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # up and left
        if f != 0 and r != board.height - 1:
            for j in range(1, 1 + min(f, board.height - 1 - r)):
                square = f"{board.files[f - j]}{board.ranks[r + j]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # up and right
        if f != board.width - 1 and r != board.height - 1:
            for k in range(1, min(board.width - f, board.height - r)):
                square = f"{board.files[f + k]}{board.ranks[r + k]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # down and right
        if f != board.width - 1 and r != 0:
            for l in range(1, 1 + min(board.width - 1 - f, r)):
                square = f"{board.files[f +l]}{board.ranks[r - l]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        return moves


class Rook(Piece):
    def __init__(self, color, position):
        self.short = color + "R"
        super().__init__(color, position)

    def move(self, board):
        # calculate all rook moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = int(board.ranks.index(int(self.position[1:])))
        f, r = boardfile, boardrank
        moves = []
        # left
        if f != 0:
            for i in range(1, f + 1):
                square = f"{board.files[f - i]}{board.ranks[r]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # up
        if r != board.height - 1:
            for j in range(1, board.height - r):
                square = f"{board.files[f]}{board.ranks[r+j]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # right
        if f != board.width - 1:
            for k in range(1, board.width - f):
                square = f"{board.files[f +k]}{board.ranks[r]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # down
        if r != 0:
            for l in range(1, r + 1):
                square = f"{board.files[f]}{board.ranks[r-l]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        return moves


class Queen(Piece):
    def __init__(self, color, position):
        self.short = color + "Q"
        super().__init__(color, position)

    def move(self, board):
        # calculate all queen moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = int(board.ranks.index(int(self.position[1:])))
        f, r = boardfile, boardrank
        moves = []
        # down and left
        if f != 0 and r != 0:
            for i in range(1,  1 + min(f, r)):
                square = f"{board.files[f -i]}{board.ranks[r-i]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # left
        if f != 0:
            for i in range(1, f + 1):
                square = f"{board.files[f -i]}{board.ranks[r]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # up and left
        if f != 0 and r != board.height - 1:
            for j in range(1, 1 + min(f, board.height - 1 - r)):
                square = f"{board.files[f -j]}{board.ranks[r+j]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # up
        if r != board.height - 1:
            for j in range(1, board.height - r):
                square = f"{board.files[f]}{board.ranks[r+j]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # up and right
        if f != board.width - 1 and r != board.height - 1:
            for k in range(1, min(board.width - f, board.height - r)):
                square = f"{board.files[f +k]}{board.ranks[r+k]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # right
        if f != board.width - 1:
            for k in range(1, board.width - f):
                square = f"{board.files[f +k]}{board.ranks[r]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # down and right
        if f != board.width - 1 and r != 0:
            for l in range(1, 1 + min(board.width - 1 - f, r)):
                square = f"{board.files[f +l]}{board.ranks[r-l]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        # down
        if r != 0:
            for l in range(1, r + 1):
                square = f"{board.files[f]}{board.ranks[r-l]}"
                valid, pathblocked = self.validate(board, square, False)
                moves += valid
                if pathblocked is True:
                    break
        return moves


class King(Piece):
    def __init__(self, color, position):
        self.short = color + "K"
        super().__init__(color, position)

    def move(self, board):
        # calculate all king moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = int(board.ranks.index(int(self.position[1:])))
        f, r = boardfile, boardrank
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1))
        moves = []
        for direction in directions:
            newf = f + direction[0]
            newr = r + direction[1]
            if newf in range(0, board.width):
                if newr in range(0, board.height):
                    square = f"{board.files[newf]}{board.ranks[newr]}"
                    valid = self.validate(board, square, False)
                    moves += valid
        return moves
