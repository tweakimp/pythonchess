from string import ascii_uppercase

width = 8  # up to 15
height = 8  # up to 15

files = "0" + ascii_uppercase[:width]
ranks = range(0, height + 1)

matrix = [["  " for x in range(0, height)]
          for y in range(0, width)]


def reset(setting):
    global matrix
    if setting == "empty":
        matrix = [["  " for x in range(0, height)]
                  for y in range(0, width)]
    elif setting == "start":
        # initialize all pieces
        matrix = [["  " for x in range(0, height)]
                  for y in range(0, width)]

    else:
        print("Something failebghfghfghfghcbgd.")


def checkSquare(position):
    readPos(position)
    if(matrix[int(file) - 1][int(rank) - 1] == "  "):
        return "free square"
    else:
        return str(matrix[int(file) - 1][int(rank) - 1])


def isEmpty(position):
    readPos(position)
    if(matrix[int(file) - 1][int(rank) - 1] == "  "):
        return True
    else:
        return False


def squareColor(position):
    readPos(position)
    if ((file + int(rank)) % 2 == 0):
        return "black"
    else:
        return "white"


def readPos(position):
    global file, rank
    file = files.index((position[0]).upper())
    rank = position[1:]
    return file,


"""for line in matrix:
    print(line)
print("=====================================================================")
matrix[0][0] = "wK"

for line in matrix:
    print(line)

print(isEmpty("A1"))"""
