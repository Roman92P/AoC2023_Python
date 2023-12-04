import re

filename = "day3_2.txt"

with open(filename) as f:
    content = f.read().splitlines()

w = len(content[0])
h = len(content)

parts = []
symbols = []
search_cords = []

for i in range(w):
    for j in range(h):
        dot = content[i][j]

        if dot.isdigit():
            parts.append(str(i) + ':' + str(j))
        if not dot.isdigit():
            if not dot.__eq__('.'):
                symbols.append(str(i) + ':' + str(j))

        # print(dot, end=' ')
    # print()

def find_search_cords(arg):
    sym_cords = re.split(r':', arg)
    x = int(sym_cords[0])
    y = int(sym_cords[1])
    if x > 0:
        search_cords.append(str(x - 1) + ':' + str(y))
    if x < w:
        search_cords.append(str(x + 1) + ':' + str(y))
    if y < h:
        search_cords.append(str(x) + ':' + str(y + 1))
    if y > 0:
        search_cords.append(str(x) + ':' + str(y - 1))
    if x > 0 and y < h:
        search_cords.append(str(x - 1) + ':' + str(y + 1))
    if x > 0 and y > 0:
        search_cords.append(str(x - 1) + ':' + str(y - 1))
    if x < w and y < h:
        search_cords.append(str(x + 1) + ':' + str(y + 1))
    if x < w and y > 0:
        search_cords.append(str(x + 1) + ':' + str(y - 1))


for p in symbols:
    find_search_cords(p)

connected_with_sym = []
for c in parts:
    if search_cords.__contains__(c):
        connected_with_sym.append(c)

correct = []
for p in parts:
    if connected_with_sym.__contains__(p):
        correct.append(p)
        cords = re.split(r':', p)
        y = int(cords[1])
        while True:
            if y < w:
                y = y + 1
                cords_to_check = cords[0] + ':' + str(y)
                if parts.__contains__(cords_to_check):
                    correct.append(cords_to_check)
                else:
                    y = int(cords[1])
                    break
            else:
                break
        while True:
            if y > 0:
                y = y - 1
                cords_to_check = cords[0] + ':' + str(y)
                if parts.__contains__(cords_to_check):
                    correct.append(cords_to_check)
                else:
                    y = int(cords[1])
                    break
            else:
                break


c = set(parts) - set(correct)
z = set(parts) - set(c)

result = 0
result_list = []
num = ''
for i in range(w):
    for j in range(h):
        dot = str(i) + ':' + str(j)
        if z.__contains__(dot) and content[i][j].isdigit():
            num = num + content[i][j]
        else:
            if num != '':
                result_list.append(num)
            num = ''

for n in result_list:
    result = result + int(n)

print(result)
