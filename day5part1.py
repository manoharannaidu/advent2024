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
                return False
        for nextp in update[idx:]:
            if nextp in thingsInBack:
                return False
    return True 

correctUpdates = []
for update in updates.splitlines():
    currUpdate = update.split(",")
    if checkUpdate(currUpdate, backRuleDict, rulesDict):
        correctUpdates.append(currUpdate[floor(len(currUpdate) / 2)])

print(sum(int(page) for page in correctUpdates))
