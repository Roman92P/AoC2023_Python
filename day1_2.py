import re
from io import StringIO

filename = "day1_2b.txt"

nums = [
    'zero',
    '0',
    'one',
    '1',
    'two',
    '2',
    'three',
    '3',
    'four',
    '4',
    'five',
    '5',
    'six',
    '6',
    'seven',
    '7',
    'eight',
    '8',
    'nine',
    '9',
]


def check_if_arr_contain_num(arg):
    for l in nums:
        if str(arg).__contains__(l):
            return l
    return ''


def find_all_nums(arg):
    tmp = []
    str = ''
    for el in arg:
        str = str + el
        if check_if_arr_contain_num(str) != '':
            tmp.append(check_if_arr_contain_num(str))
            str = ''

    retrieved_nums = []
    for el in tmp:
        for n in nums:
            if el.__contains__(n):
                retrieved_nums.append(n)
    return retrieved_nums


with open(filename) as f:
    content = f.read().split()

result = 0

for line in content:
    nums_arr = find_all_nums(line)
    for el in nums_arr:
        if el.isalpha():
            nums_arr[nums_arr.index(el)] = nums[nums.index(el) + 1]
    p = int(nums_arr[0] + '' + nums_arr[len(nums_arr) - 1])
    print(p)
    result = result + p
print(result)
