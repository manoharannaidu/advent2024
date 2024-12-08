from collections import deque
from copy import deepcopy

with open("./inputs/day7input.txt", "r") as f:
    data = f.read()

def funcnew(target, numsList):
    
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

    return funcnew(target, mulList) or funcnew(target, addList)


def funcnew2(target, numsList):
    if not numsList:
        return False
    if len(numsList) < 2:
        return False
    
    num1 = numsList.popleft()
    num2 = numsList.popleft()

    if target == num1 * num2:
        if not numsList:
            return True
    if target == num1 + num2:
        if not numsList:
            return True
    if target == int(str(num1) + str(num2)):
        if not numsList:
            return True
    
    mulList = deepcopy(numsList)
    addList = deepcopy(numsList)
    catList = deepcopy(numsList)
    mulList.appendleft(num1 * num2)
    addList.appendleft(num1 + num2)
    catList.appendleft(int(str(num1) + str(num2)))

    return funcnew2(target, mulList) or funcnew2(target, addList) or funcnew2(target, catList)

counter = 0
for line in data.splitlines():
    target1, nums = line.split(":")
    nums = [int(n) for n in nums.strip().split(" ")]

    numslist = deque(nums)
    nL = deepcopy(numslist)

    if funcnew(int(target1), numslist):
        counter += int(target1)
    elif funcnew2(int(target1), nL):
        counter += int(target1)

print(counter)
