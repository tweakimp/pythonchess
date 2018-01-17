from random import choice
from string import ascii_uppercase


selffiles = ascii_uppercase[:8]
selfranks = range(1, 8 + 1)


def randomPos():
    position = str(choice(selffiles)) + str(choice(selfranks))
    return position


print(randomPos())
