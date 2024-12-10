from collections import deque

with open("./inputs/9in.txt", "r") as f:
    data = f.read()

arr = deque()
ID = 0
end_idx = 0
start_idx = 0
for idx, char in enumerate(data):
    if idx % 2 == 0:
        end_idx += int(char)
        for index1 in range(start_idx, end_idx):
            arr.append(ID)
        ID += 1
        start_idx = end_idx
    else:
        end_idx += int(char)
        for index2 in range(start_idx, end_idx):
            arr.append(".")
        start_idx = end_idx

startptr = 0
endptr = len(arr) - 1

while True:
    if (arr[startptr] == ".") and (arr[endptr] != "."):
        arr[startptr], arr[endptr] = arr[endptr], arr[startptr]
    elif (arr[startptr] == ".") and (arr[endptr] == "."):
        endptr -= 1
    elif (arr[startptr] != ".") and (arr[endptr] != "."):
        startptr += 1
    else:
        endptr -= 1
    if startptr > endptr:
        break
        

checksum = 0
for idx, val in enumerate(arr):
    if val != ".":
        checksum += idx * int(val)

print(checksum)
