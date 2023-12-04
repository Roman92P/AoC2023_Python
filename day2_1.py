import re

filename = "day2_2.txt"

with open(filename) as f:
    content = f.read().splitlines()

rule_one = 12
rule_two = 13
rule_three = 14


def check_game(game_input):
    temp_arr = re.split('[;,:]', game_input)
    print(temp_arr)
    for l in temp_arr:
        if l.__contains__('red'):
            if int(re.findall("\d+", l)[0]) > rule_one:
                return 0
        if l.__contains__('green'):
            if int(re.findall("\d+", l)[0]) > rule_two:
                return 0

        if l.__contains__('blue'):
            if int(re.findall("\d+", l)[0]) > rule_three:
                return 0
    return int(re.findall('\d+', temp_arr[0])[0])


result = 0
for el in content:
    result = check_game(el) + result

print(result)
