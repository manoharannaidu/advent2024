import networkx as nx
from numpy import array, argwhere

with open("./inputs/16input.txt", "r") as f:
    data = f.read()

G = [list(line) for line in data.splitlines()]

npG = array(G)
start = int(argwhere(npG == "S")[0][0]), int(argwhere(npG == "S")[0][1])
end = int(argwhere(npG == "E")[0][0]), int(argwhere(npG == "E")[0][1])

def nextSteps(grid, pos, facing):
    result = []
    if facing == (0,1):
        for dir in [(-1,0), (0,1), (1,0)]:    
            if dir == facing:
                result.append((1,dir,(pos[0] + dir[0], pos[1] + dir[1])))
            else:
                result.append((1000,dir,(pos[0] + dir[0], pos[1] + dir[1])))
    elif facing == (-1,0):
        for dir in [(-1,0), (0,1), (0,-1)]:
            if dir == facing:
                result.append((1,dir,(pos[0] + dir[0], pos[1] + dir[1])))
            else:
                result.append((1000,dir,(pos[0] + dir[0], pos[1] + dir[1])))
    elif facing == (0,-1):
        for dir in [(0,-1), (1,0), (-1,0)]:
            if dir == facing:
                result.append((1,dir,(pos[0] + dir[0], pos[1] + dir[1])))
            else:
                result.append((1000,dir,(pos[0] + dir[0], pos[1] + dir[1])))
    elif facing == (1,0):
        for dir in [(0,-1), (0,1), (1,0)]:
            if dir == facing:
                result.append((1,dir,(pos[0] + dir[0], pos[1] + dir[1])))
            else:
                result.append((1000,dir,(pos[0] + dir[0], pos[1] + dir[1])))
    else:
        raise ValueError()

    result = [t for t in result if G[t[2][0]][t[2][1]] != "#"]

    if result == []:
        if facing == (-1,0):
            result.append((2000, (1,0), pos))
        if facing == (1,0):
            result.append((2000, (-1,0), pos))
        if facing == (0,1):
            result.append((2000, (0,-1), pos))
        if facing == (0,-1):
            result.append((2000, (0,1), pos))
    
    return result

DiG = nx.DiGraph()
for r, row in enumerate(G):
    for c, col in enumerate(row):
        if col != "#":
            for d in [(-1,0), (0,1), (1,0), (0,-1)]:
                steps = nextSteps(G, (r,c), d)
                for step in steps:
                    DiG.add_weighted_edges_from([(((r,c), d), (step[2], step[1]), step[0])])

paths = nx.all_shortest_paths(DiG, source=(start, (0,1)), target=(end, (-1,0)), weight="weight")

paths = [path for path in paths]

tiles = []
for path in paths:
    for tile, d in path:
        tiles.append(tile)

print(len(set(tiles)))
