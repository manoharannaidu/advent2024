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

def find9(G, start):
    if G[start[0]][start[1]] == 9:
        return 1
    nextSteps = []
    for DIR in range(4):
        nStepX, nStepY = walkInDir(start, DIR, directions)
        if findInBounds(grid, (nStepX, nStepY)):
            if grid[nStepX][nStepY] == grid[start[0]][start[1]] + 1:
                nextSteps.append(np.array([nStepX, nStepY]))
    if nextSteps == []:
        return 0
    return sum([find9(G, s) for s in nextSteps])

score = 0
for start in zeroes:
    score += find9(grid, start)

print(score)
