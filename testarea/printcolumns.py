from random import choice, randint
from string import ascii_letters


def printColumns(alist, columns, padding, separator):

    # make it rectangualar by filling empty list entries
    missingentries = columns - len(alist) % columns
    xlist = alist[:]  # copy list!
    for i in range(missingentries):
        xlist.append(":")
    # get widths for each column
    columnwidths = [0 for _ in range(columns)]
    columnlength = len(xlist) // columns
    for i in range(len(xlist)):
        if columnwidths[i // columnlength] < len(xlist[i]) + padding:
            columnwidths[i // columnlength] = len(xlist[i]) + padding
    for i in range(len(xlist)):
        xlist[i] = f"{xlist[i]: <{columnwidths[i // columnlength]}}"
    columnlength = len(xlist) // columns
    for i in range(columnlength):
        for j in range(columns):
            print(xlist[i + (j * columnlength)], end="")
        print("")


def createRandomList(lowerBound, upperBound, length):
    output = []
    for i in range(length):
        output.append("".join((choice(ascii_letters))
                              for x in range(randint(lowerBound, upperBound))))
    return output


numberlist = 4
testlist = createRandomList(1, 8, randint(25, 35))


def alphabetical(listToPrint):
    return sorted(listToPrint, key=str.lower)


def lengthwise(listToPrint):
    return sorted(listToPrint, key=len)


def testThis(listToPrint, columns, padding):
    print("==============================================================")
    printColumns(listToPrint, columns, padding, " ")
    print("==============================================================")
    printColumns(alphabetical(listToPrint), columns, padding, " ")
    print("==============================================================")
    printColumns(lengthwise(listToPrint), columns, padding, " ")


if __name__ == '__main__':
    testThis(testlist, randint(2, 4), 3)
