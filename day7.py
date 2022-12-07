from collections import defaultdict

directory = open("day7.txt", "r").read().strip()

size = defaultdict(int)

#find the directories with AT MOST 100,000 file size.
#find the sum of all directories with a filesize of at most 100,000.

path = []

for line in directory.split("\n"):
    if line.startswith("$ cd"):
        d = line.split()[2]
        if d == "/":
            path.append("/")
        elif d == "..":
            last = path.pop()
        else:
            path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{d}")

    if line[0].isdigit():
        for p in path:
            size[p] += int(line.split()[0])

print(f"Part 1:{sum(s for s in size.values() if s <= 100000)}")
print(f"Part 2:{min(s for s in size.values() if s >= 30000000 - (70000000 - size['/']))}")

