with open("./inputs/day2input.txt") as f:
    data = f.read()

safe_reports = 0

for line in data.splitlines():
    l = [int(ele) for ele in line.split(" ")]
    if all(l[i] <= l[i+1] for i in range(len(l) - 1)):
        if all(1 <= l[i+1] - l[i] <=3 for i in range(len(l) - 1)):
            safe_reports += 1
    elif all(l[i] >= l[i+1] for i in range(len(l) - 1)):
        if all(1 <= l[i] - l[i+1] <=3 for i in range(len(l) - 1)):
            safe_reports += 1
    else:
        continue

print(safe_reports)
