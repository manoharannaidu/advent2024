with open("./inputs/day4input.txt", "r") as f:
    data = f.read()

def isValid(x, y, maxX, maxY):
    return 0 <= x < maxX and 0 <= y < maxY

def findWordInDirection(grid, word, x, y, dirX, dirY):
    n, m = len(grid), len(grid[0])
    for index in range(len(word)):
        newX, newY = x + dirX * index, y + dirY * index
        if not isValid(newX, newY, n, m) or grid[newX][newY] != word[index]:
            return False
    return True

def countWordOccurrences(grid, word):
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    count = 0
    n, m = len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            for dirX, dirY in directions:
                if findWordInDirection(grid, word, i, j, dirX, dirY):
                    count += 1
    return count

grid = [list(line) for line in data.splitlines()]

count = countWordOccurrences(grid, "XMAS")

print(count)
