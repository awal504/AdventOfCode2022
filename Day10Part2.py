# Advent of Code 2022 Day 10

def main():

    infile = open("DayTen.txt", "r")
    crtinput = infile.read().splitlines()
    infile.close()
    register = 1
    cycle = 0
    queue = []
    crtstring = ""
    # Build the queue of instructions
    for command in crtinput:
        cmd = command.split(" ")[0]
        if cmd == "noop":
            queue.append(0)
        else:
            value = command.split(" ")[1]
            queue.append(0)
            queue.append(int(value))

    # Read the queue and print image
    for i in range(len(queue)):
        if cycle > 39:
            cycle = 0
            crtstring = crtstring + "\n"
        if abs(cycle - register) <= 1:
            crtstring = crtstring + "#"
        else:
            crtstring = crtstring + "."
        if queue[i] != 0:
            register += queue[i]
        cycle += 1
    print(crtstring)


main()
