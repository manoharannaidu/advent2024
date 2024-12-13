from numpy import array, unique
from scipy.ndimage import label
from scipy.signal import convolve2d

with open("./inputs/12input.txt", "r") as f:
    data = f.read()

grid = array([list(line) for line in data.splitlines()])

ans = 0

for L, n in [label(grid == g) for g in unique(grid)]:
    for i in range(n):
        H = (L == i + 1)

        x = abs(convolve2d(H, [[-1, 1], [1, -1]]))

        ans += H.sum() * x.sum()

print(ans)
