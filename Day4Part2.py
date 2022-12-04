# Advent of Code 2022 Day 4
def main():
    infile = open("DayFour.txt", "r")
    running = 0
    joblist = infile.read().splitlines()
    for job in joblist:
        job = job.split(",")
        elf1 = job[0].split("-")
        elf1set = set(range(int(elf1[0]),int(elf1[1])+1))
        print(elf1set)
        elf2 = job[1].split("-")
        elf2set = set(range(int(elf2[0]),int(elf2[1])+1))
        print(elf2set)
        if elf1set.isdisjoint(elf2set) == False:
            running += 1
    infile.close()
    print(running)


main()
