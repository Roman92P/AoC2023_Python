import re

filename = "day3_2.txt"

with open(filename) as f:
    content = f.read().splitlines()

high = len(content)
width = len(content[0])

to_sum = 0


def gear_has_two_parts(h, w):
    gear_parts = []

    num = ''

    if h > 0:
        line_above = content[h - 1]
        line_above = line_above.replace('*', '.')
        if line_above[w].isdigit() and line_above[w - 1].isdigit() and line_above[w + 1].isdigit():
            num = num + str(line_above[w - 1] + '' + line_above[w] + '' + line_above[w + 1])
            gear_parts.append(num)
            num = ''
        else:
            if line_above[w].isdigit():
                num = num + str(line_above[w])
            new_line = line_above[:w] + '*' + line_above[w + 1:]
            tem_arr = new_line.split('*')
            if tem_arr[0][-1].isdigit():
                nums_p_one = re.findall(r'\d+$', tem_arr[0])
                num = ''.join(nums_p_one) + num
                gear_parts.append(num)
                num = ''
            if tem_arr[1][0].isdigit():
                nums_p_one = re.findall(r'^\d+', tem_arr[1])
                num = num + ''.join(nums_p_one)
                gear_parts.append(num)
                num = ''

    num = ''

    gear_line = content[h]
    gear_line_p_one = gear_line[:w]
    gear_line_p_two = gear_line[w + 1:]
    if gear_line_p_one[-1].isdigit():
        num = ''.join(re.findall(r'\d+$', gear_line_p_one))
        gear_parts.append(num)
        num = ''
    if gear_line_p_two[0].isdigit():
        num = ''.join(re.findall(r'^\d+', gear_line_p_two))
        gear_parts.append(num)
        num = ''

    num = ''

    if h < len(content):
        line_below = content[h + 1]
        line_below = line_below.replace('*', '.')
        if line_below[w].isdigit() and line_below[w - 1].isdigit() and line_below[w + 1].isdigit():
            num = num + str(line_below[w -1] + '' + line_below[w] + '' + line_below[w + 1])
            gear_parts.append(num)
            num = ''
        else:
            if line_below[w].isdigit():
                num = num + str(line_below[w])
            new_line_b = line_below[:w] + '*' + line_below[w + 1:]
            tem_arr_b = new_line_b.split('*')
            if tem_arr_b[0][-1].isdigit():
                nums_p_one_b = re.findall(r'\d+$', tem_arr_b[0])
                num = ''.join(nums_p_one_b) + num
                gear_parts.append(num)
                num = ''
            if tem_arr_b[1][0].isdigit():
                nums_p_one_b = re.findall(r'^\d+', tem_arr_b[1])
                num = num + ''.join(nums_p_one_b)
                gear_parts.append(num)
                num = ''

    num = ''

    return gear_parts


for i in range(high):
    for j in range(width):
        temp_cords = str(i) + ':' + str(j)
        if (content[i][j].__eq__('*')) and len(gear_has_two_parts(i, j)) == 2:
            part_result = 1
            parts = gear_has_two_parts(i, j)
            print(parts)
            for n in parts:
                part_result *= int(n)
            to_sum += part_result
print(to_sum)
