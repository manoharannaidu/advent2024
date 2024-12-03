import re

with open("./inputs/day3input.txt", "r") as f:
    data = f.read()

pattern = r".*?mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\).*?"

def sumMul(text:str):
    result = 0
    for m in re.finditer(pattern, text):
        result += int(m.group("num1")) * int(m.group("num2"))

    return result

result1 = 0
calc = True
for m in re.finditer(r".*?(?P<instr>do\(\)|don\'t\(\)).*?", data.replace("\n", "")):
    if m.group("instr") == "don't()":
        if calc:
            result1 += sumMul(data[m.span()[0]: m.span()[1]])
        calc = False
    elif m.group("instr") == "do()":
        if calc:
            result1 += sumMul(data[m.span()[0]: m.span()[1]])
        calc = True
    else:
        raise ValueError()

if m.group("instr") == "do()":
    result1 += sumMul(data[m.span()[0]: m.span()[1]])

print(result1)
