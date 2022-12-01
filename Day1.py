# Advent of Code 2022 Day 1
def main():
    infile = open("DayOne.txt", "r")
    cals_list = list((1, 2, 3))
    cals_list.clear()
    cals = "a"
    running = 0
    while cals != '':
        try:
            running = 0
            cals = str(infile.readline())
        except ValueError:
            print("EOF")
        while cals != '\n':
            try:
                running = running + int(cals)
                cals = str(infile.readline())
            except ValueError:
                break
        cals_list.append(running)
    infile.close()
    cals_list.sort(reverse=True)
    print(cals_list[0], " ", cals_list[1], " ", cals_list[2])
    print(cals_list[0] + cals_list[1] + cals_list[2])


main()
