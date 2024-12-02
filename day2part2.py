with open("./inputs/day2input.txt") as f:
    data = f.read()

def check_asc_sorted(l):
    truths = [l[i] <= l[i+1] for i in range(len(l) - 1)]

    return True if (len(truths) - sum(truths)) <= 1 else False

def check_dsc_sorted(l):
    truths = [l[i] >= l[i+1] for i in range(len(l) - 1)]

    return True if (len(truths) - sum(truths)) <= 1 else False

def check_asc_ap(l):

    for idx in range(len(l)):
        newl = [ele for i, ele in enumerate(l) if i != idx]
        truths = all(1 <= newl[i+1] - newl[i] <= 3 for i in range(len(newl) - 1))
        if truths == True:
            return True
    
    return False

def check_dsc_ap(l):
    for idx in range(len(l)):
        newl = [ele for i, ele in enumerate(l) if i != idx]
        truths = all(1 <= newl[i] - newl[i+1] <=3 for i in range(len(newl) - 1))
        if truths == True:
            return True

    return False

safe_reports1 = 0
for line in data.splitlines():
    l = [int(ele) for ele in line.split(" ")]
    if check_asc_sorted(l):
        if check_asc_ap(l):
            safe_reports1 +=1
    elif check_dsc_sorted(l):
        if check_dsc_ap(l):
            safe_reports1 += 1
    else:
        continue
        

print(safe_reports1)
