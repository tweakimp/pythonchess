import board


def letterToNumber(x):
    """Change letter to number."""
    return board.files.index(x)


def numberToLetter(x):
    """Change number to letter."""
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
