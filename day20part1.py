from numpy import array, argwhere, unique, sum
from networkx import DiGraph, shortest_path
from copy import deepcopy

with open("./inputs/20input.txt", "r") as f:
    sample = f.read()

G = array([list(line) for line in sample.splitlines()])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

startXY = argwhere(G == "S")[0]
start = (int(startXY[0]), int(startXY[1]))

endXY = argwhere(G == "E")[0]
end = (int(endXY[0]), int(endXY[1]))

def getNextSteps(start, grid, directions):
    return [
        nextStep
         for d in directions
         if (nextStep := (start[0] + d[0], start[1] + d[1]))
         if 0 <= nextStep[0] < grid.shape[0]
         if 0 <= nextStep[1] < grid.shape[1]
    ]

def buildGraph(grid, directions):
    DiG = DiGraph()
    
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            nextSteps = getNextSteps((r,c), grid, directions)
            nextSteps = [
                nextStep
                 for nextStep in nextSteps
                 if grid[nextStep] != "#" 
            ]
            DiG.add_edges_from([((r,c), step) for step in nextSteps])

    return DiG

DiG = buildGraph(G, directions)

shortestPath = shortest_path(DiG, source=start, target=end)

hashLocations = []

for tile in shortestPath:
    steps = getNextSteps(tile, G, directions)
    steps = [step for step in steps if G[step] == "#"]
    hashLocations.extend(steps)

hashes = set(hashLocations)

saves = []
for hashLoc in hashes:
    newDG = deepcopy(DiG)
    steps = [step for step in getNextSteps((int(hashLoc[0]), int(hashLoc[1])), G, directions) if G[step] != "#"]
    newDG.add_edges_from([(step, (int(hashLoc[0]), int(hashLoc[1]))) for step in steps])
    saves.append(len(shortestPath) -  len(shortest_path(newDG, source=start, target=end)))

saves = array(saves)

print(len(saves[(saves > 99)]))
