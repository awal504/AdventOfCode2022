# Advent of Code 2022 Day 5
def main():
    stack = [[], [], [], [], [], [], [], [], []]
    x = 0
    y = 1
    i = 0
    infile = open("DayFive.txt", "r")
    cratelist = infile.read().splitlines()
    for crate in cratelist:
        if crate == "":
            break
        while y < len(crate):
            if crate[y] != " ":
                stack[x].insert(0, crate[y])
            x += 1
            y += 4
        x = 0
        y = 1
        i += 1
    i += 1
    while i != 0:
        cratelist.pop(0)
        i -= 1
    for move in cratelist:
        moves = move.split(" ")
        moveamt = int(moves[1])
        movefrom = int(moves[3]) - 1
        moveto = int(moves[5]) - 1
        while moveamt != 0:
            stack[moveto].append(stack[movefrom][-1])
            stack[movefrom].pop()
            moveamt -= 1
    print(stack[0][-1], stack[1][-1], stack[2][-1], stack[3][-1], stack[4][-1], stack[5][-1], stack[6][-1], stack[7][-1], stack[8][-1], )
    infile.close()


main()
