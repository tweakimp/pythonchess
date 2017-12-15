import board

def letterToNumber(x):
    """Change letter to number."""
    return board.files.index(x)


def numberToLetter(x):
    """Change number to letter."""
    return board.files[x]


if(board.width in (8, 11)):
    # a or an depending on boardWidth
    aORan = "an"
else:
    aORan = "a"
