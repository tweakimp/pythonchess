from random import choice, randint
from string import ascii_letters

# create a list of length "length" with strings of random length between
# "lowerBound" and "upperBound" that contain random "ascii_letters"


def createRandomList(lowerBound, upperBound, length):
    output = []
    for i in range(length):
        output.append("".join((choice(ascii_letters))
                              for x in range(randint(lowerBound, upperBound + 1))))
    return output


print(createRandomList)
