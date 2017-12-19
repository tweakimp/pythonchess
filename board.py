from string import ascii_uppercase

width = 8  # up to 15
height = 8  # up to 15

files = "0" + ascii_uppercase[:width]
ranks = range(1, height + 1)


def squareColor(position):
    file = files.index(((position[0]).upper()))
    rank = position[1:]
    if ((file + int(rank)) % 2 == 0):
        return "black"
    else:
        return "white"
