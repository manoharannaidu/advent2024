import numpy as np

with open("./inputs/day6input.txt", "r") as f:
    data = f.read()

grid = np.array([list(line) for line in data.splitlines()])

def findCurrDirStart(grid):
    if np.where(grid == "^"):
        currDir = (-1,0)
        currStart = np.where(grid == "^")
    elif np.where(grid == ">"):
        currDir = (0,1)
        currStart = np.where(grid == ">")
    elif np.where(grid == "<"):
        currDir = (0,-1)
        currStart = np.where(grid == "<")
    elif np.where(grid == "v"):
        currDir = (1,0)
        currStart = np.where(grid == "v")

    return currDir, (int(currStart[0][0]), int(currStart[1][0]))


def calcNewPos(currStart, currDir):
    return (currStart[0] + currDir[0], currStart[1] + currDir[1])

def withinBounds(var, grid):
    return (0 <= var[0] < grid.shape[0]) and (0 <= var[1] < grid.shape[1])

def turnGurard(currDir):
    if currDir == (-1,0):
        return (0,1)
    if currDir == (0,1):
        return (1,0)
    if currDir == (1,0):
        return (0,-1)
    if currDir == (0,-1):
        return (-1,0)

currDir, currStart = findCurrDirStart(grid)

while True:
    grid[currStart[0]][currStart[1]] = "X"
    newPos = calcNewPos(currStart, currDir)
    if withinBounds(newPos, grid):
        if grid[newPos[0]][newPos[1]] != "#":
            currStart = newPos
        else:
            currDir = turnGurard(currDir)
            # currStart = calcNewPos(currStart, currDir)
    else:
        break

print(len(np.where(grid == "X")[0]))
