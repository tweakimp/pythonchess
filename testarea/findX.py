import tkinter
from tkinter import font as tkFont


def measure(x):
    tkinter.Frame().destroy()  # Enough to initialize resources
    test = tkFont.Font(family='Fira Mono', size=14)
    width = test.measure(f"{chr(x)}")
    return width


for x in range(0, 10000):
    try:
        if measure(x) == 19:
            print(x)
            print("...[　]...|")
            print(f"...[{chr(x)}]...|")
            print("")
            print("*********************")
    except:
        pass


# codedict = {"X": 4510, " ": 4447, "K": 9812, "Q": 9813,
#             "R": 9820, "B": 9821, "N": 9822, "P": 9823}
#
# for i in codedict:
#     print(chr(codedict[i]))
