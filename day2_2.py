import re

filename = "day2_2.txt"

with open(filename) as f:
    content = f.read().splitlines()




def check_game(game_input):
    red_max = 0
    green_max = 0
    blue_max = 0
    temp_arr = re.split('[;,:]', game_input)
    for l in temp_arr:
        if l.__contains__('red'):
            if int(re.findall("\d+", l)[0]) > red_max:
                red_max = int(re.findall("\d+", l)[0])
        if l.__contains__('green'):
            if int(re.findall("\d+", l)[0]) > green_max:
                green_max = int(re.findall("\d+", l)[0])

        if l.__contains__('blue'):
            if int(re.findall("\d+", l)[0]) > blue_max:
                blue_max = int(re.findall("\d+", l)[0])

    return red_max * green_max * blue_max


result = 0
for el in content:
    result = check_game(el) + result

print(result)
