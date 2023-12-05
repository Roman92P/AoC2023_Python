import re

symbol_with_parts = []


def find_punkt_tail(r_l):
    correct = []
    for p in parts:
        if r_l.__eq__(p):
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
    return correct


def find_start_cords(arg):
    result_list = []
    result = []
    sym_cords = re.split(r':', arg)
    x = int(sym_cords[0])
    y = int(sym_cords[1])
    up = ''
    down = ''
    left = ''
    right = ''
    up_left = ''
    up_right = ''
    down_left = ''
    down_right = ''
    signals = []
    if x > 0:
        if content[x - 1][y].isdigit():
            up = (str(x - 1) + ':' + str(y))
            signals.append(".")
        else:
            if x > 0 and y < h:
                if content[x - 1][y + 1].isdigit():
                    up_right = (str(x - 1) + ':' + str(y + 1))
                    signals.append(".")
            if x > 0 and y > 0:
                if content[x - 1][y - 1].isdigit():
                    up_left = (str(x - 1) + ':' + str(y - 1))
                    signals.append(".")
    if x < w:
        if content[x + 1][y].isdigit():
            down = (str(x + 1) + ':' + str(y))
            signals.append(".")
        else:
            if x < w and y < h:
                if content[x + 1][y + 1].isdigit():
                    down_right = (str(x + 1) + ':' + str(y + 1))
                    signals.append(".")
            if x < w and y > 0:
                if content[x + 1][y - 1].isdigit():
                    down_left = (str(x + 1) + ':' + str(y - 1))
                    signals.append(".")
    if y < h:
        if content[x][y + 1].isdigit():
            right = (str(x) + ':' + str(y + 1))
            signals.append(".")
    if y > 0:
        if content[x][y - 1].isdigit():
            left = (str(x) + ':' + str(y - 1))
            signals.append(".")

    if len(signals) >= 2:
        result_list.append('gear')
        result_list.append(up)
        result_list.append(down)
        result_list.append(left)
        result_list.append(right)
        result_list.append(up_right)
        result_list.append(up_left)
        result_list.append(down_right)
        result_list.append(down_left)
        result_list = list(filter(None, result_list))

        for l in result_list:
            if l.__eq__('gear'):
                result.append('gear')
            if not l.__eq__('gear'):
                result.append(l)
                a = find_punkt_tail(l)
                for n in a:
                    result.append(n)

    return result


filename = "day3_1.txt"

with open(filename) as f:
    content = f.read().splitlines()

w = len(content[0])
h = len(content)

parts = []

for i in range(w):
    for j in range(h):
        dot = content[i][j]
        if dot.isdigit():
            parts.append(str(i) + ':' + str(j))

for i in range(w):
    for j in range(h):
        dot = content[i][j]
        if not dot.isdigit():
            if dot.__eq__('*'):
                gear = str(i) + ':' + str(j)
                for f in find_start_cords(gear):
                    symbol_with_parts.append(f)

str_cords = ' '.join(str(x) for x in symbol_with_parts)
splited_gear_cords = list(filter(None, re.split('gear', str_cords)))
print(splited_gear_cords)

nums = []
for c in splited_gear_cords:
    c_list = re.split('\s+', c)
    c_list.sort()
    c_list = list(filter(None, c_list))
    cur_x = 0
    num = ''

    for el in c_list:
        l_list = re.split(':', el)
        x = int(l_list[0])
        y = int(l_list[1])

        if x != cur_x :
            nums.append(num)
            cur_x = x
            num = str(content[x][y])
        else:
            num = num + content[x][y]
    nums.append(num)
    nums.append('')

print(nums)

part_result = 1
p_result = []
for g in nums:
    print(g)
    if g.__eq__(''):
       print(g)
    if g.isdigit():
        part_result = part_result * int(g)
    else:
        p_result.append(part_result)
        part_result = 1


sum = 0

print(p_result)

for t in p_result:
    if int(t) > 1:
        sum = sum + int(t)

print(sum)

