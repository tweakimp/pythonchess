from random import randint


def missingcalc(entries, columns):
    missingentries = columns - entries % columns
    columnlength = (entries + missingentries) // columns
    if columnlength * columns == entries + missingentries:
        print("PASS: ", entries, columnlength, columns)
    else:
        print("FAIL: ", entries, columnlength, columns)


for _ in range(40):
    missingcalc(randint(10, 100), randint(2, 11))
missingcalc(4, 40)
