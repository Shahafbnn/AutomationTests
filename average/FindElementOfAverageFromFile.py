with open(r"data.txt", encoding='UTF8') as rawFile:
    rawText = rawFile.read()
    textSplitToGroups = rawText.split("[")
# print(textSplitToGroups[1])
textSplitToGroupsAndLines = [i.splitlines() for i in textSplitToGroups]
# ^ creates a 2D array consisting of every group seperated by '[' and every group is seperated to newlines.
textSplitToGroupsAndLines.pop(0)
# print(textSplitToGroupsAndLines)
for group in textSplitToGroupsAndLines:
    calc = float(group[1][group[1].find(':') + 2:]) * (len(group) - 3 + 1)
    # print(calc)
    for splitlines in group:
        if '=' in splitlines:
            print("group " + splitlines[splitlines.find('=') + 1:-1] + ":")
        elif "Average:" in splitlines.lower():
            pass
        elif ":" in splitlines:
            print(splitlines[splitlines.find(':') + 2:])

