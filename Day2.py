# Advent of Code 2022 Day 2
def main():
    infile = open("DayTwo.txt", "r")
    running = 0
    result = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    shape = {
        "AX": 3,
        "BY": 2,
        "CZ": 1,
        "AY": 1,
        "AZ": 2,
        "BX": 1,
        "BZ": 3,
        "CX": 2,
        "CY": 3
    }
    rps = str(infile.readline()).replace(" ", "").strip()
    while rps != '':
        points = 0
        you = rps[1:2]
        points = shape.get(rps, 0)
        points = points + result.get(you, 0)
        running = running + int(points)
        rps = str(infile.readline()).replace(" ", "").strip()
    infile.close()
    print(running)


main()
