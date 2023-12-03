import re

filename = "day1.txt"

with open(filename) as f:
    content = f.read().split()

result = 0

for line in content:
    lineDigits = re.findall('\d', line)
    result = result + int(str(lineDigits[0] + '' + lineDigits[len(lineDigits) - 1]))
print(result)
