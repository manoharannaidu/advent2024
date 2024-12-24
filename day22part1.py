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

secrets = dict()
for idx, num in enumerate(input_list):
    for i in range(2000):
        curr = secretGen(num)
        num = curr
    secrets[input_list[idx]] = curr

print(sum(secrets.values()))
