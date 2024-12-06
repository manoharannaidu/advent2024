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
def newGrid(currStart, currDir, grid):
    retGrid = grid.copy()
    newPos = calcNewPos(currStart, currDir)
    if withinBounds(newPos, grid):
        retGrid[newPos[0]][newPos[1]] = "#"
    else:
        return []

    return retGrid

def turnGurard(currDir):
    if currDir == (-1,0):
        return (0,1)
    if currDir == (0,1):
        return (1,0)
    if currDir == (1,0):
        return (0,-1)
    if currDir == (0,-1):
        return (-1,0)

def findLoop(Start, Dir, grid):
    retGrid = grid.copy()
    posSeen = []
    posSeen.append((Start, Dir))
    while True:
        # retGrid[Start[0]][Start[1]] = "X"
        newPos = calcNewPos(Start, Dir)
        if (newPos, Dir) not in posSeen:
            posSeen.append((newPos, Dir))
        else:
            return True
        if withinBounds(newPos, retGrid):
            if retGrid[newPos[0]][newPos[1]] != "#":
                Start = newPos
            else:
                Dir = turnGurard(Dir)
        else:
            return False

currDir, currStart = findCurrDirStart(grid)

initS = (currStart[0], currStart[1])
initD = (currDir[0], currDir[1])

loopCounter = 0
newObsPos = []

while True:
    newPos = calcNewPos(currStart, currDir)
    newgrid = newGrid(currStart, currDir, grid)
    if len(newgrid) != 0:
        if newPos in newObsPos:
            pass
        else:
            if findLoop(initS, initD, newgrid):
                loopCounter += 1
                newObsPos.append(newPos)
    if withinBounds(newPos, grid):
        if grid[newPos[0]][newPos[1]] != "#":
            currStart = newPos
        else:
            currDir = turnGurard(currDir)
    else:
        break
