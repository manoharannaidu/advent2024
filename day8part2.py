import numpy as np

from collections import defaultdict
from itertools import combinations

with open("./inputs/day8in.txt", "r") as f:
    data = f.read()

grid = [list(line) for line in data.splitlines()]

def getAntiNodesNew(coord1, coord2):
    antinodes = []
    
    antinodes.append((coord1[0], coord1[1]))

    ystep = coord2[1]  - coord1[1]; xstep = coord2[0] - coord1[0]
    x0, y0 = coord1[0], coord1[1]
    xhat, yhat = coord1[0], coord1[1]
    
    while True:
        xant1 = x0 + xstep; yant1 = y0 + ystep

        if (0 <= xant1 < len(grid)) and (0 <= yant1 < len(grid)):
            antinodes.append((xant1, yant1))
        else:
            break
        
        x0, y0 = xant1, yant1

    while True:
        xant2 = xhat - xstep; yant2 = yhat - ystep

        if (0 <= xant2 < len(grid)) and (0 <= yant2 < len(grid)):
            antinodes.append((xant2, yant2))
        else:
            break

        xhat, yhat = xant2, yant2


    
    return antinodes


antenaCoords = defaultdict(list)

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col != ".":
            antenaCoords[col].append((r,c))

antinodes = []
for key in antenaCoords:
    for coord1, coord2 in combinations(antenaCoords[key], 2):
        antinodes.extend(getAntiNodesNew(coord1, coord2))

print(len(set(antinodes)))
