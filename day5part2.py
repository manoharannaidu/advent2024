from collections import defaultdict
from math import floor

with open("./inputs/day5input.txt", "r") as f:
    data = f.read()

rules, updates = data.split("\n\n")

rulesDict = defaultdict(list)

for rule in rules.splitlines():
    rulesDict[rule[:2]].append(rule[3:])

backRuleDict = defaultdict(list)

for rule in rules.splitlines():
    backRuleDict[rule[3:]].append(rule[:2])

def checkUpdate(update, backDict, frontDict):
    for idx, page in enumerate(update):
        thingsInBack, thingsInFront = backDict[page], frontDict[page]
        for p in update[:idx]:
            if p in thingsInFront:
                return True
        for nextp in update[idx:]:
            if nextp in thingsInBack:
                return True
    return False

incorrectUpdates = []
for update in updates.splitlines():
    currUpdate = update.split(",")
    if checkUpdate(currUpdate, backRuleDict, rulesDict):
        # print(currUpdate)
        incorrectUpdates.append(currUpdate)

for i, update in enumerate(incorrectUpdates):
    while checkUpdate(update, backRuleDict, rulesDict):
        for idx, page in enumerate(update):
            thingsInBack, thingsInFront = backRuleDict[page], rulesDict[page]
            incorrectFront = list(set(thingsInBack).intersection(set(incorrectUpdates[i][idx:])))
            incorrectBack = list(set(thingsInFront).intersection(set(incorrectUpdates[i][:idx])))
        
            for incrr in incorrectFront:
                fidx = incorrectUpdates[i].index(incrr)
                temp = incorrectUpdates[i][fidx]
                incorrectUpdates[i][fidx] = incorrectUpdates[i][idx]
                incorrectUpdates[i][idx] = temp
                del temp
        
            for bincrr in incorrectBack:
                bidx = incorrectUpdates[i].index(bincrr)
                tempb = incorrectUpdates[i][bidx]
                incorrectUpdates[i][bidx] = incorrectUpdates[i][idx]
                incorrectUpdates[i][idx] = tempb
                del tempb

part2 = 0
for update in incorrectUpdates:
    part2 += int(update[floor(len(update) / 2)])

print(part2)
