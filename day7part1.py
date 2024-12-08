from collections import deque

with open("./inputs/day7input.txt", "r") as f:
    data = f.read()


def funcold(target, numsList):
    from copy import deepcopy
    
    if not numsList:
        return False
    if len(numsList) < 2:
        return False

    num1 = numsList.popleft()
    num2 = numsList.popleft()

    if target == num1 * num2:
        return True
    if target == num1 + num2:
        return True
    
    mulList = deepcopy(numsList)
    addList = deepcopy(numsList)
    mulList.appendleft(num1 * num2)
    addList.appendleft(num1 + num2)

    return funcold(target, mulList) or funcold(target, addList)

counter = 0
for line in data.splitlines():
    target1, nums = line.split(":")
    nums = [int(n) for n in nums.strip().split(" ")]

    numslist = deque(nums)

    if funcold(int(target1), numslist):
        counter += int(target1)

print(counter)
