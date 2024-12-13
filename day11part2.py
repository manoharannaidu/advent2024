from collections import defaultdict, Counter

def fastBlink(counter):
    result = defaultdict(int)
    for num in counter:
        if num == 0:
            result[1] += counter[num]
        elif len(str(num)) % 2 == 0:
            key = str(num)
            cut = int(len(key) / 2)
            # print(type(cut), cut)
            result[int(key[:cut])] += counter[num]
            result[int(key[cut:])] += counter[num]
        else:
            result[num * 2024] += counter[num]
    return result

qstr = "2 72 8949 0 981038 86311 246 7636740"

data = Counter([int(num) for num in qstr.split(" ")])

for i in range(75):
    data = fastBlink(data)

print(sum(data.values()))
