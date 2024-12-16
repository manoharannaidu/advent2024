import numpy as np

with open("./inputs/15input.txt") as file:
    input_str = file.read()

input_grid,input_dir = input_str.split("\n\n")

grid = []
for elem in input_grid.splitlines():
    grid.append(list(elem))


directions = list(input_dir.replace("\n",""))

# start point of robot
start_point = tuple(np.argwhere(np.array(grid) == '@')[0])

dir_dict = {
    "<" : (0,-1),
    ">" : (0,1),
    "^" : (-1,0),
    "v" : (1,0)
}

def next_point(i,j,dir):
    i_next = i + dir_dict[dir][0]
    j_next = j + dir_dict[dir][1]     
    return i_next, j_next



def traversal(start_point,grid,directions):
    i,j = start_point

    for dir in directions:
        # stops when? when direction stop

        # what is expected next point
        should_go = next_point(i,j,dir)

        # when can it go ahead 
        if grid[should_go[0]][should_go[1]] == "#":
            # don't move
            continue

        elif grid[should_go[0]][should_go[1]] == "O":
            if dir == "<":
                for v in range(j-1,0,-1):
                    if (grid[i][v] == "#"):
                        break
                    if grid[i][v] == ".":
                        grid[i][v] = "O"
                        grid[i][j-1] = "."
                        grid[i][j] = "."
                        i,j = should_go
                        grid[i][j] = "@"                        
                        break


            if dir == ">":
                for v in range(j+1,len(grid)):
                    if grid[i][v] == "#":
                        break
                    if grid[i][v] == ".":
                        grid[i][v] = "O"
                        grid[i][j+1] = "."
                        grid[i][j] = "."
                        i,j = should_go
                        grid[i][j] = "@"
                        break
                        
                    
            if dir == "^":                
                for v in range(i-1,0,-1):
                    if (grid[v][j] == "#"):
                        break
                    if grid[v][j] == ".":
                        grid[v][j] = "O"
                        grid[i-1][j] = "."
                        grid[i][j] = "."
                        i,j = should_go
                        grid[i][j] = "@"
                        break

            if dir == "v":
                for v in range(i+1,len(grid)):
                    if (grid[v][j] == "#"):
                        break
                    if grid[v][j] == ".":
                        grid[v][j] = "O"
                        grid[i+1][j] = "."
                        grid[i][j] = "."
                        i,j = should_go
                        grid[i][j] = "@"  
                        break                  

        # when can it not go ahead

        else:                
            # update grid, i ,j
            grid[i][j] = "."
            i,j = should_go
            grid[i][j] = "@"


    return grid


ans = traversal(start_point,grid,directions)

print(sum([(100*k + v) for k,v in np.argwhere(np.array(ans) == "O")]))

