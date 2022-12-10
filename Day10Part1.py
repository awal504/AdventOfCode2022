# Advent of Code 2022 Day 10

def main():

    infile = open("DayTen.txt", "r")
    crtinput = infile.read().splitlines()
    infile.close()
    register = 1
    cycle = 0
    signalsum = 0
    queue = []
    # Build the queue of instructions
    for command in crtinput:
        cmd = command.split(" ")[0]
        if cmd == "noop":
            queue.append(0)
        else:
            value = command.split(" ")[1]
            queue.append(0)
            queue.append(int(value))
    # Read the queue and print signal strength during each cycle
    for i in range(len(queue)):
        cycle += 1
        if queue[i - 1] != 0:
            register += queue[i - 1]
        signal = register * cycle
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            print(cycle, register, signal)
            signalsum += signal
    print(signalsum)


main()
