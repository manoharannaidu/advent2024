import numpy as np

from collections import defaultdict
from itertools import combinations

with open("./inputs/day8in.txt", "r") as f:
    data = f.read()

grid = [list(line) for line in data.splitlines()]

antenaCoords = defaultdict(list)

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col != ".":
            antenaCoords[col].append((r,c))

def getAntiNodes(coord1, coord2):
    antinodes = []
    
    ystep = coord2[1]  - coord1[1]; xstep = coord2[0] - coord1[0]

    xant1 = coord1[0] + (2 * xstep); yant1 = coord1[1] + (2 * ystep)
    xant2 = coord2[0] - (2 * xstep); yant2 = coord2[1] - (2 * ystep)

    if (0 <= xant1 < len(grid)) and (0 <= yant1 < len(grid)):
        antinodes.append((xant1, yant1))
    if (0 <= xant2 < len(grid)) and (0 <= yant2 < len(grid)):
        antinodes.append((xant2, yant2))

    return antinodes

antinodes = []
for key in antenaCoords:
    for coord1, coord2 in combinations(antenaCoords[key], 2):
        antinodes.extend(getAntiNodes(coord1, coord2))

print(len(set(antinodes)))
