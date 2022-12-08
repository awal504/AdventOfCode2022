# Advent of Code 2022 Day 8

def main():
    y = 0
    treematrix = [[]]
    infile = open("DayEight.txt", "r")
    treeinput = infile.read().splitlines()
    infile.close()
    for tree in treeinput:
        x = 0
        while len(tree) > x:
            treematrix[y].append(int(tree[x]))
            x += 1
        treematrix.append([])
        y += 1

    # Check for visibility
    edge1 = len(treeinput[0])
    edge2 = y
    y = 0
    viscount = 0
    maxscene = 0
    for t in treematrix:
        x = 0
        while len(t) > x:
            scenicl = 0
            scenicr = 0
            scenicu = 0
            scenicd = 0
            if x == 0:
                viscount += 1
            elif y == 0:
                viscount += 1
            elif x == edge1 - 1:
                viscount += 1
            elif y == edge2 - 1:
                viscount += 1
            else:
                # Look left, right, up, and down for trees that are taller or of equal height
                visl = True
                visr = True
                visu = True
                visd = True
                scenicl = 0
                scenicr = 0
                scenicu = 0
                scenicd = 0
                z = x - 1
                while z >= 0:
                    if treematrix[y][z] >= t[x]:
                        visl = False
                        scenicl += 1
                        break
                    z -= 1
                    scenicl += 1
                z = x + 1
                while z < edge1:
                    if treematrix[y][z] >= t[x]:
                        visr = False
                        scenicr += 1
                        break
                    z += 1
                    scenicr += 1
                z = y - 1
                while z >= 0:
                    if treematrix[z][x] >= t[x]:
                        visu = False
                        scenicu += 1
                        break
                    z -= 1
                    scenicu += 1
                z = y + 1
                while z < edge2:
                    if treematrix[z][x] >= t[x]:
                        visd = False
                        scenicd += 1
                        break
                    z += 1
                    scenicd += 1
                if visl or visr or visu or visd:
                    viscount += 1
            x += 1
            if (scenicl * scenicr * scenicu * scenicd) > maxscene:
                maxscene = scenicl * scenicr * scenicu * scenicd
        y += 1
    print(viscount)
    print(maxscene)


main()
