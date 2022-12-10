# Advent of Code 2022 Day 9

def main():
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    length = 1
    headloc = {(0, 0)}
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
                headloc.add((hx, hy))
                print("Head Move: ", hx, hy)
                taut = tx - hx
                if (abs(taut)) > length:
                    for t in range(abs(abs(taut) - length)):
                        tx -= 1
                        if ty > hy:
                            ty -= 1
                        elif ty < hy:
                            ty += 1
                        tailloc.add((tx, ty))
                        print("Tail Move: ", tx, ty)
        elif direction == "R":
            for i in range(distance):
                hx += 1
                headloc.add((hx, hy))
                print("Head Move: ", hx, hy)
                taut = hx - tx
                if (abs(taut)) > length:
                    for t in range(abs(taut) - length):
                        tx += 1
                        if ty > hy:
                            ty -= 1
                        elif ty < hy:
                            ty += 1
                        tailloc.add((tx, ty))
                        print("Tail Move: ", tx, ty)
        elif direction == "U":
            for i in range(distance):
                hy += 1
                headloc.add((hx, hy))
                print("Head Move: ", hx, hy)
                taut = hy - ty
                if abs(taut) > length:
                    for t in range(abs(taut) - length):
                        ty += 1
                        if tx > hx:
                            tx -= 1
                        elif tx < hx:
                            tx += 1
                        tailloc.add((tx, ty))
                        print("Tail Move: ", tx, ty)
        elif direction == "D":
            for i in range(distance):
                hy -= 1
                headloc.add((hx, hy))
                print("Head Move: ", hx, hy)
                taut = ty - hy
                if (abs(taut)) > length:
                    for t in range(abs(taut) - length):
                        ty -= 1
                        if tx > hx:
                            tx -= 1
                        elif tx < hx:
                            tx += 1
                        tailloc.add((tx, ty))
                        print("Tail Move: ", tx, ty)
    count = 0
    for i in tailloc:
        count += 1
    print(count)


main()
