import board


def let2num(x):
    return board.files.index(x)


def num2let(x):
    return board.files[x]


if (board.width in (8, 11)):
    # a or an depending on board.width
    aORan = "an"
else:
    aORan = "a"


def inspect(x):
    print(vars(x))
