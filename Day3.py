# Advent of Code 2022 Day 3
def main():
    infile = open("DayThree.txt", "r")
    running = 0
    priority = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ruck1 = str(infile.readline()).replace(" ", "").strip()
    while ruck1 != '':
        points = 0
        i = 0
        ruck2 = str(infile.readline()).replace(" ", "").strip()
        ruck3 = str(infile.readline()).replace(" ", "").strip()
        packsize = int(max(len(ruck1), len(ruck2), len(ruck3)))
        if packsize == len(ruck1):
            while i < packsize:
                match = str(ruck2.find(ruck1[i]))
                if match == "-1":
                    i += 1
                else:
                    match = str(ruck3.find(ruck1[i]))
                    if match == "-1":
                        i +=1
                    else:
                        points = priority.index(ruck1[i])
                        break
        elif packsize == len(ruck2):
            while i < packsize:
                match = str(ruck1.find(ruck2[i]))
                if match == "-1":
                    i += 1
                else:
                    match = str(ruck3.find(ruck2[i]))
                    if match == "-1":
                        i +=1
                    else:
                        points = priority.index(ruck2[i])
                        break
        elif packsize == len(ruck3):
            while i < packsize:
                match = str(ruck2.find(ruck3[i]))
                if match == "-1":
                    i += 1
                else:
                    match = str(ruck1.find(ruck3[i]))
                    if match == "-1":
                        i +=1
                    else:
                        points = priority.index(ruck3[i])
                        break
        running = running + int(points)
        ruck1 = str(infile.readline()).replace(" ", "").strip()
    infile.close()
    print(running)


main()
