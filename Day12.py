# Advent of Code 2022 Day 12
class PathNode:
    def __init__(self, loc, parent):
        self.loc = tuple(loc)
        self.parent = parent
        self.children = []

    def add_child(self, c):
        self.children.append(c)


def main():
    # Initialize map, find start point, end point
    topofile = [[]]
    byte = " "
    elevation = "SabcdefghijklmnopqrstuvwxyzE"
    y = 0
    sx = 0
    sy = 0
    ex = 0
    ey = 0
    infile = open("DayTwelve.txt", "r")
    while byte != "":
        byte = infile.read(1)
        if byte != "\n":
            if byte == "S":
                sx = len(topofile[y])
                sy = y
            if byte == "E":
                ex = len(topofile[y])
                ey = y
            topofile[y].append(elevation.find(byte))
        else:
            topofile.append([])
            y += 1
    infile.close()
    topofile.pop()
    # Initialize node variables
    maxx = len(topofile[sy]) - 1
    maxy = len(topofile) - 1
    start = PathNode((sy, sx), None)
    current = start
    pathqueue = []
    seen = [(sy, sx)]

    # Check available moves down, right, up or left,
    # building path nodes if we aren't backtracking
    def get_children(self):
        cy = int(self.loc[0])
        cx = int(self.loc[1])
        cvalue = int(topofile[cy][cx])
        if maxy > cy and ((cy + 1), cx) not in seen:
            down = int(topofile[cy + 1][cx])
            if cvalue >= down - 1:
                self.add_child(PathNode((cy + 1, cx), self))
                seen.append(((cy + 1), cx))
        if maxx > cx and (cy, (cx + 1)) not in seen:
            right = int(topofile[cy][cx + 1])
            if cvalue >= right - 1:
                self.add_child(PathNode((cy, cx + 1), self))
                seen.append((cy, (cx + 1)))
        if 0 < cy and ((cy - 1), cx) not in seen:
            up = int(topofile[cy - 1][cx])
            if cvalue >= up - 1:
                self.add_child(PathNode((cy - 1, cx), self))
                seen.append(((cy - 1), cx))
        if 0 < cx and (cy, (cx - 1)) not in seen:
            left = int(topofile[cy][cx - 1])
            if cvalue >= left - 1:
                self.add_child(PathNode((cy, cx - 1), self))
                seen.append((cy, (cx - 1)))
        return self.children

    while current.loc[0] != ey or current.loc[1] != ex:
        print(current.loc[0], current.loc[1], ey, ex)
        get_children(current)
        for p in current.children:
            pathqueue.append(p)
        current = pathqueue.pop()
    running = 0
    while current.parent is not None:
        running += 1
        current = current.parent
    print(running)


main()
