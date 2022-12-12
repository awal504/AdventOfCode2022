# Advent of Code 2022 Day 11
# Written with assistance from https://chasingdings.com/2022/12/11/advent-of-code-day-11-monkey-in-the-middle/

def main():
    # Initialize Monkeys!
    class MonkeyNode:
        def __init__(self, itemlist, operation, test, tmonkey, fmonkey):
            self.itemlist = itemlist
            self.operation = operation
            self.test = test
            self.tmonkey = tmonkey
            self.fmonkey = fmonkey
            self.checked = 0

    # Populate our troop
    def readmonkey(mfilelist):
        mitems = mfilelist[1].replace(" ", "").split(":")[-1].split(",")
        moperation = mfilelist[2].split("=")[-1].strip()
        mtest = int(mfilelist[3].split(" ")[-1])
        tm = int(mfilelist[4].split(" ")[-1])
        tf = int(mfilelist[5].split(" ")[-1])
        return MonkeyNode(mitems, moperation, mtest, tm, tf)

    infile = open("DayEleven.txt", "r")
    monkeyfile = infile.read().splitlines()
    infile.close()
    # Read each section of the Monkey File
    monkeyfilelist = []
    monkeylist = []
    for m in monkeyfile:
        if m != "":
            monkeyfilelist.append(m)
        else:
            monkeylist.append(readmonkey(monkeyfilelist))
            monkeyfilelist.clear()
    monkeylist.append(readmonkey(monkeyfilelist))

    # Part 2 introduced me to some new number theory. Thanks, Tipa!
    maxworry = 0
    for a in monkeylist:
        if maxworry == 0:
            maxworry = a.test
        else:
            maxworry *= a.test

    # Start 10000 rounds of monkey business
    for b in range(10000):
        for s in monkeylist:
            for i in s.itemlist:
                old = int(i)
                new = int(eval(s.operation)) % maxworry
                if new % s.test == 0:
                    monkeylist[s.tmonkey].itemlist.append(new)
                else:
                    monkeylist[s.fmonkey].itemlist.append(new)
            s.checked += len(s.itemlist)
            s.itemlist.clear()
    mbusiness = []
    for o in monkeylist:
        mbusiness.append(o.checked)
    mbusiness.sort(reverse=True)
    print(mbusiness[0] * mbusiness[1])


main()
