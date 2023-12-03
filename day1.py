import re

# Define the file's name.
filename = "day1.txt"

# Open the file and read its content.
with open(filename) as f:
    content = f.read().split()

result = 0
# Display the content.
for line in content:
    lineDigits = re.findall('\d', line)
    result = result + int(str(lineDigits[0] + '' + lineDigits[len(lineDigits) - 1]))
print(result)
