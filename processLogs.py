import os
import re


def importTurnlist(file):
    # get file content
    path = os.getcwd() + f"\history\{file}.txt"
    with open(path, "r", encoding="utf8") as log:
        text = log.read()
    # split between spaces and new lines
    # [:-1] removes newline at the end of files
    splitted = (re.split("[\s|\n]", text))[:-1]
    print(text)
    loglist = []
    for i in range(len(splitted)):
        if i % 2 == 0:
            loglist.append([splitted[i], splitted[i + 1]])
    # loglist now list of [position, target] - lists moves
    return loglist


importTurnlist("game2")
