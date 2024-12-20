from numpy import zeros
from networkx import DiGraph, shortest_path, has_path

with open("./inputs/18input.txt", "r") as f:
    data = f.read()

G = zeros((71,71))

dangerCoords = [
    tuple(int(num) for num in line.split(",")) 
     for idx, line in enumerate(data.splitlines()) 
     if idx < 1024
]

def nextStep(grid, start):
    
    directions = [(-1,0), (0,1), (1,0), (0,-1)]

    steps = [(start[0] + d[0], start[1] + d[1]) for d in directions]

    steps = [
        step 
         for step in steps 
         if 0 <= step[0] < len(grid)
         if 0 <= step[1] < len(grid)
    ]
    
    steps = [
        step 
         for step in steps 
         if grid[step[1], step[0]] != 1
    ]

    return steps

for coord in dangerCoords:
    G[coord[1], coord[0]] = 1


DiG = DiGraph()
for r, row in enumerate(G):
    for c, col in enumerate(row):
        if col != "1":
            steps = nextStep(G, (c,r))
            for step in steps:
                DiG.add_edges_from([((r,c), (step[1], step[0]))])

sPath = shortest_path(DiG, source=(0,0), target=(70,70))

print(len(sPath) - 1)
