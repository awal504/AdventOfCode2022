# Advent of Code 2022 Day 7
# Written with assistance from HexTree

def main():
    class FileNode:
        def __init__(self, name, parent, is_dir, size):
            self.name = name
            self.parent = parent
            self.contains = []
            self.is_dir = is_dir
            self.size = size

        def add_file(self, newfile):
            self.contains.append(newfile)

    root = FileNode("/", None, True, int(0))
    current = root
    total = 0
    infile = open("DaySeven.txt", "r")
    commandlist = infile.read().splitlines()
    for command in commandlist:
        if command == "":
            break
        elif command[0] == "$":
            if command == "$ cd /":
                current = root
            elif command == "$ cd ..":
                if current.parent is not None:
                    current = current.parent
                else:
                    print("Trying to go to non-existent parent")
            else:
                newdir = command[5:]
                for child in current.contains:
                    if newdir == child.name:
                        current = child
                        break
        elif command[0] == "d":
            newdir = command[4:]
            match = False
            for child in current.contains:
                if newdir == child.name:
                    match = True
                    break
            if not match:
                current.add_file(FileNode(newdir, current, True, int(0)))
        else:
            file = command.split(" ")
            filename = file[1]
            filesize = int(file[0])
            match = False
            for child in current.contains:
                if filename == child.name:
                    match = True
                    break
            if not match:
                current.add_file(FileNode(filename, current, False, filesize))
                total += filesize
    infile.close()
    global goldilocks
    goldilocks = 30000000 - (70000000 - total)

    def get_size(self):
        running = 0
        for c in self.contains:
            if c.is_dir:
                running += get_size(c)
            else:
                running += c.size
        if goldilocks < running < 4000000:
            print(self.name, running)
        return running

    get_size(root)


main()
