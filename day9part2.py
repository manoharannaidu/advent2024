from collections import deque

with open("./inputs/9in.txt", "r") as f:
    data = f.read()

ID = 0
arr = deque()
for idx, char in enumerate(data):
    if idx % 2 == 0:
        arr.append([ID] * int(char))
        ID += 1
    else:
        arr.append(["."] * int(char))

arr = [vals for vals in arr if vals != []]

for idx, vals in enumerate(arr[::-1]):
    if "." not in vals:
        for spaceidx, spaces in enumerate(arr[:(len(arr) - idx - 1)]):
            space = [i for i,v in enumerate(spaces) if v == "."]
            if len(space) >= len(vals):
                for (index, ele), s in zip(enumerate(vals), space):
                    arr[spaceidx][s], arr[(len(arr) - idx - 1)][index] = ele, arr[spaceidx][s]

result = [num for things in arr for num in things]

checksum = 0
for idx, num in enumerate(result):
    if num != ".":
        checksum += idx * int(num)

print(checksum)
