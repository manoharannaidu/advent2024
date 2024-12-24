from collections import defaultdict
from numpy import array, diff, nan, append
import pandas as pd

with open("./inputs/22input.txt", "r") as f:
    data = f.read()

input_list = []
for elem in data.splitlines():
    input_list.append(int(elem)) 

def mix(num, secret):
    return num ^ secret

def prune(secret):
    return secret % 16777216

def secretGen(secret):
    
    temp = secret << 6
    secret = mix(temp, secret)
    secret = prune(secret)
    temp = round(secret >> 5)
    secret = mix(temp, secret)
    secret = prune(secret)
    temp = secret << 11
    secret = mix(temp, secret)
    secret = prune(secret)

    return secret

secrets = defaultdict(list)
for idx, num in enumerate(input_list):
    secrets[input_list[idx]].append(int(str(num)[-1]))
    for i in range(2000):
        curr = secretGen(num)
        num = curr
        secrets[input_list[idx]].append(int(str(curr)[-1]))

secrets_diff = { key: diff(array(val)) for key, val in secrets.items() }


buyers_list = []

for key,prices in secrets.items():
        
    df = pd.DataFrame({"price": prices, "diff": append(nan, secrets_diff[key])})
    buyer_diffs_dict = dict()
    
    for window in df.rolling(4):
        if len(window) < 4:
            continue
        if any(window["diff"].isna()):
            continue
        # to skip reoccurence in one dataframe    
        if tuple(window["diff"]) in buyer_diffs_dict.keys():
            continue
        
        buyer_diffs_dict[tuple(window["diff"])] = int(window["price"].iloc[-1])

    buyers_list.append(buyer_diffs_dict)

final_data = defaultdict(list)
for buyer_info in buyers_list:
    for key, val in buyer_info.items():
        final_data[key].extend([val])

result = {key: sum(val) for key, val in final_data.items()}

print(max(result.values()))
