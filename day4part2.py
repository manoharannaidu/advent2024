with open("./inputs/day4input.txt", "r") as f:
    data = f.read()

def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY

def findMASXShape(grid, x, y):
    n, m = len(grid), len(grid[0])

    positions = [
        (x, y), (x+2, y),
        (x + 1, y + 1), 
        (x, y + 2), (x + 2, y + 2)
    ]
    
    for px, py in positions:
        if not isValid(px, py, n, m):
            return False

    mas1 = [grid[x][y], grid[x + 1][y + 1], grid[x + 2][y + 2]]
    mas2 = [grid[x+2][y], grid[x + 1][y + 1], grid[x][y + 2]]

    
    return (mas1 == ['M', 'A', 'S'] or mas1 == ['S', 'A', 'M']) and \
           (mas2 == ['M', 'A', 'S'] or mas2 == ['S', 'A', 'M'])

def countMASXShapes(grid):
    count = 0
    n, m = len(grid), len(grid[0])

    for i in range(n - 2):
        for j in range(m - 2):  
            if findMASXShape(grid, i, j):
                count += 1
    return count

grid = [list(line) for line in data.splitlines()]
count = countMASXShapes(grid)

print(count)
