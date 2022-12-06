# Advent of Code 2022 Day 6
def main():
    i = 0
    running = 0
    search = []
    infile = open("DaySix.txt", "r")
    datastream = infile.read()
    while i < len(datastream):
        if len(search) < 14:
            search.append(datastream[i])
            i += 1
        else:
            bite = 0
            while bite < 14:
                running += search.count(search[bite])
                bite += 1
            if running > 14:
                search.pop(0)
            else:
                print("Found Start at:", i)
                break
            running = 0
    infile.close()


main()
