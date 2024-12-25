from aoc.aoc_input import input_data

from numpy import array, argwhere, sum

file_path = "./inputs/25input.txt"

data = input_data(file_path).fetch_input()

keys = []
locks = []

def get_heights(grid):
    heights = []
    for i in range(grid.shape[1]):
        heights.append(int(sum(grid[:, i] == "#")))

    return array(heights)

for chunk in data.split("\n\n"):
    G = array([list(line) for line in chunk.splitlines()])
    # print(get_heights(G))
    if all(G[0] == "."):
        keys.append(get_heights(G))
    else:
        locks.append(get_heights(G))

pair_found = 0
# lock_key = set()
for key in keys:
    for lock in locks:
        # if tuple((tuple(lock), tuple(key))) not in lock_key:
        curr_combo = key + lock
        if all(curr_combo <= 7):
            # print(lock, key)
            # lock_key.add(tuple((tuple(lock), tuple(key))))
            pair_found += 1

print(pair_found)
