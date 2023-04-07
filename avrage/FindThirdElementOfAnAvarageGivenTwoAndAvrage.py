from typing import List

if __name__ == '__main__':
    done = False
    args: list[float] = []

    average = float(input("Please type the average: "))
#    slicingAvg = average.split(".")
#   average = float(slicingAvg[0]) + float(slicingAvg[1]) / (10 * len(slicingAvg[1]))

    count = 0
    while not done:
        inp = input("Please type another argument or type FINISH to finish: ")
        if inp.lower() == "finish":
            done = True
        else:
            args.append(float(inp))
            count += 1

calc: float = average*(count+1)
for i in args:
    #slicing = args[i].split(".")
    calc -= i
print(f"The other number is: {calc}")