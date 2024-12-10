import numpy as np

with open("./inputs/10input.txt", "r") as f:
    data = f.read()

grid = np.array([[int(num) for num in line] for line in data.splitlines()])
directions = [np.array((-1, 0)), np.array((0, 1)), np.array((1, 0)), np.array((0, -1))]

zeroes = np.argwhere(grid == 0)

nines = np.argwhere(grid == 9)

def findInBounds(G, coord):
    return (0 <= coord[0] < G.shape[0]) and (0 <= coord[1] < G.shape[1]) 

def walkInDir(startCoord, DIR, directions):
    return startCoord + directions[DIR]

def reach9(G, start, end):
    nextSteps = []
    for DIR in range(4):
        nStepX, nStepY = walkInDir(start, DIR, directions)
        if findInBounds(grid, (nStepX, nStepY)):
            if G[nStepX][nStepY] == G[start[0]][start[1]] + 1:
                nextSteps.append(np.array([nStepX, nStepY]))
    if nextSteps == []:
        return False
    for step in nextSteps:
        if all(step == end):
            return True
    return any([reach9(G, s, end) for s in nextSteps])

score = 0
for start in zeroes:
    for end in nines:
        if reach9(grid, start, end):
            score += 1

print(score)
