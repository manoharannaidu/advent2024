import re

with open("./inputs/day3input.txt", "r") as f:
    data = f.read()

pattern = r".*?mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\).*?"

result = 0
for m in re.finditer(pattern, data):
    result += int(m.group("num1")) * int(m.group("num2"))

print(result)
