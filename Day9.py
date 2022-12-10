# Advent of Code 2022 Day 9
# Written with assistance from https://wooledge.org/~greg/advent/2022/9b

def main():
    rope = []
    for i in range(10):
        rope.append([0, 0])
    tailloc = {(0, 0)}
    infile = open("DayNine.txt", "r")
    ropeinput = infile.read().splitlines()
    infile.close()

    def move(hi, ti, direction, rope):
        hx, hy = rope[hi]
        tx, ty = rope[ti]
        # Moving each knot of the rope, followed by the next
        if direction == "L":
            hx -= 1
        elif direction == "R":
            hx += 1
        elif direction == "U":
            hy += 1
        elif direction == "D":
            hy -= 1
        if abs(tx - hx) <= 1 and (abs(ty - hy)) <= 1:
            pass
        elif tx == hx:
            if ty > hy:
                ty -= 1
            else:
                ty += 1
        elif ty == hy:
            if tx > hx:
                tx -= 1
            else:
                tx += 1
        else:
            if tx > hx:
                tx -= 1
            else:
                tx += 1
            if ty > hy:
                ty -= 1
            else:
                ty += 1
        # Change knot locations
        rope[hi] = [hx, hy]
        rope[ti] = [tx, ty]

    for moves in ropeinput:
        direct = moves.split(" ")[0]
        dis = int(moves.split(" ")[1])
        for i in range(int(dis)):
            move(0, 1, direct, rope)
            for n in range(1, len(rope) - 1):
                move(n, n+1, "", rope)
                tailloc.add(tuple(rope[-1]))

    count = 0
    for i in tailloc:
        count += 1
    print(count)


main()
