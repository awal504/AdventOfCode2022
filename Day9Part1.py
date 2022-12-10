# Advent of Code 2022 Day 9

def main():
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    tailloc = {(0, 0)}
    infile = open("DayNine.txt", "r")
    ropeinput = infile.read().splitlines()
    infile.close()
    for move in ropeinput:
        direction = move.split(" ")[0]
        distance = int(move.split(" ")[1])
        # Moving the head of the rope, followed by the tail
        if direction == "L":
            for h in range(distance):
                hx -= 1
                taut = tx - hx
                if (abs(taut)) > 1:
                    for t in range(abs(abs(taut) - 1)):
                        tx -= 1
                        if ty > hy:
                            ty -= 1
                        elif ty < hy:
                            ty += 1
                        tailloc.add((tx, ty))
        elif direction == "R":
            for i in range(distance):
                hx += 1
                taut = hx - tx
                if (abs(taut)) > 1:
                    for t in range(abs(taut) - 1):
                        tx += 1
                        if ty > hy:
                            ty -= 1
                        elif ty < hy:
                            ty += 1
                        tailloc.add((tx, ty))
        elif direction == "U":
            for i in range(distance):
                hy += 1
                taut = hy - ty
                if abs(taut) > 1:
                    for t in range(abs(taut) - 1):
                        ty += 1
                        if tx > hx:
                            tx -= 1
                        elif tx < hx:
                            tx += 1
                        tailloc.add((tx, ty))
        elif direction == "D":
            for i in range(distance):
                hy -= 1
                taut = ty - hy
                if (abs(taut)) > 1:
                    for t in range(abs(taut) - 1):
                        ty -= 1
                        if tx > hx:
                            tx -= 1
                        elif tx < hx:
                            tx += 1
                        tailloc.add((tx, ty))
    count = 0
    for i in tailloc:
        count += 1
    print(count)


main()
