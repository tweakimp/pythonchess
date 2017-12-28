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
        print("Something failed.")
