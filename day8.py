from functools import reduce
import numpy as np

with open("day8.txt", "r") as f:
    forestGrid = np.array([[int(c) for c in x.strip()] for x in f])

origMask = np.zeros_like(forestGrid)
distance = [np.zeros_like(forestGrid) for _ in range(4)]

for k, dist in enumerate(distance):
    grid, mask = np.rot90(forestGrid, k=k), np.rot90(origMask, k =k)

    for row, (g,m,d) in enumerate(zip(grid,mask,dist)):
        current = 0
        for col, h in enumerate(g):
            if col == 0 or h > current:
                m[col] =1
                current = h
            currentHeight = h
            counter = 0
            for i in g[col + 1:]:
                counter += 1
                if i >= currentHeight:
                    break

            d[col] = counter

print("Part 1:", np.sum(mask))

distance = [np.rot90(d,k=-k) for k,d in enumerate(distance)]

print("Part 2:", np.max(reduce(np.multiply,distance)))
