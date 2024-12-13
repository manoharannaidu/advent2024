with open("./inputs/12input.txt", "r") as f:
    data = f.read()

grid = [list(line) for line in data.splitlines()]

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def inBounds(G, coord: tuple) -> bool:
    return (0 <= coord[0] < len(G)) and (0 <= coord[1] < len(G[0]))

def getNextSteps(start, directions, G):
    return [
        (start[0] + direc[0], start[1] + direc[1])
         for direc in directions
         if inBounds(G, (start[0] + direc[0], start[1] + direc[1]))
    ]

def getArea(start, G, char, visited=[], neighbours={}):
    visited.append(start)
    neighbours[start] = []
    nextSteps = getNextSteps(start, directions, G)
    if nextSteps != []:
        if not any(char == G[step[0]][step[1]] for step in nextSteps):
            return visited, neighbours
        else:
            for step in nextSteps:
                if char == G[step[0]][step[1]]:
                    neighbours[start].append(step)
                    if step not in visited:
                        # print(f"{neighbours} next step found")
                        getArea(step, G, char, visited, neighbours= neighbours)
            return visited, neighbours
    else:
        return visited, neighbours

cost = 0
foundAreas = []
for r,row in enumerate(grid):
    for c, col in enumerate(row):
        if (r,c) not in foundAreas:
            currChar = col
            visits, ns = getArea((r,c), grid, currChar, visited=[], neighbours={})
            cost += (len(visits) * (sum(4 - len(val) for key, val in ns.items())))
            foundAreas.extend(visits)
        
print(cost)
