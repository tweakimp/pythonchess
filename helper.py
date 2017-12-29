import board


def letterToNumber(x):
    return board.files.index(x)


def numberToLetter(x):
    return board.files[x]


if (board.width in (8, 11)):
    # a or an depending on board.width
    aORan = "an"
else:
    aORan = "a"


def squareColor(position):
    file = board.files.index(((position[0]).upper()))
    rank = position[1:]
    if ((file + int(rank)) % 2 == 0):
        return "black"
    else:
        return "white"


def inspect(x):
    print(vars(x))


def isFree(square):
    file = letterToNumber((square[0]).upper())
    rank = square[1:]
    if(board.matrix[int(file) - 1][int(rank) - 1] == "  "):
        return "free square"
    else:
        return str(board.matrix[int(file) - 1][int(rank) - 1])
