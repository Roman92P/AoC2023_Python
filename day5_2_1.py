import time

s_time = time.time()

filename = "day5_2.txt"

with open(filename) as f:
    content = f.read().splitlines()

seeds_list = []

seed_soil_map = []

soil_fertilizer_map = []

fertilizer_water_map = []

water_light_map = []

light_temp_map = []

temp_humidity_map = []

humidity_loc_map = []

seed_rng_pair = []

for line in content:
    if line.__contains__('seeds:'):
        l_list = line.split(' ')
        l_list = [x for x in l_list if x.isdigit()]
        for h in l_list:
            seeds_list.append(h)
        for i, s in enumerate(seeds_list):

            if i % 2 == 0:
                end_indx = i + 1
                temp = [s, seeds_list[end_indx]]
                seed_rng_pair.append(temp)

for indx, i in enumerate(content):
    if i.__contains__('seed-to-soil map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                seed_soil_map.append(next_l.split(' '))
            else:
                break
            indx = new_indx

    if i.__contains__('soil-to-fertilizer map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                soil_fertilizer_map.append(next_l.split(' '))
            else:
                break
            indx = new_indx
    if i.__contains__('fertilizer-to-water map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                fertilizer_water_map.append(next_l.split(' '))
            else:
                break
            indx = new_indx
    if i.__contains__('water-to-light map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                water_light_map.append(next_l.split(' '))
            else:
                break
            indx = new_indx
    if i.__contains__('light-to-temperature map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                light_temp_map.append(next_l.split(' '))
            else:
                break
            indx = new_indx
    if i.__contains__('temperature-to-humidity map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                temp_humidity_map.append(next_l.split(' '))
            else:
                break
            indx = new_indx
    if i.__contains__('humidity-to-location map:'):
        while True:
            if indx + 1 < len(content):
                new_indx = indx + 1
                next_l = content[new_indx]
                if len(next_l) > 0 and next_l[0].isdigit():
                    humidity_loc_map.append(next_l.split(' '))
                else:
                    break
                indx = new_indx
            else:
                break

mappers = [
    seed_soil_map,
    soil_fertilizer_map,
    fertilizer_water_map,
    water_light_map,
    light_temp_map,
    temp_humidity_map,
    humidity_loc_map
]

location = []


def map_seed(seed_num):
    sd_num = int(seed_num)

    for mapper_lists in mappers:
        for mapper_list in mapper_lists:
            mapper_int_list = [int(x) for x in mapper_list]

            destination = mapper_int_list[0]
            source = mapper_int_list[1]
            range = mapper_int_list[2]

            if source <= sd_num <= source + range:
                sd_num = destination + (sd_num - source)
                break

    print(sd_num)
    return sd_num


def process(chunk):
    return [map_seed(x) for x in chunk]


s_seed_range_l = seeds_list[::2]
e_seed_range_l = seeds_list[1::2]
s_seed_range_l = [int(x) for x in s_seed_range_l]
e_seed_range_l = [int(x) for x in e_seed_range_l]
all_seed_range = [min(s_seed_range_l), int(max(s_seed_range_l)) + int(max(e_seed_range_l))]

print(all_seed_range)

cur_map_res = 0


def is_on_the_range(number):
    for n in seed_rng_pair:
        x = int(n[0])
        y = int(n[1])
        if x <= int(number) <= x + y:
            return True
    return False


def get_first_av_number(input_nr):
    max_rgn_nums = []
    for n in seed_rng_pair:
        x = int(n[0])
        y = int(n[1])
        max_rgn_nums.append(int(x) + int(y))
    print(max_rgn_nums)
    int_list = [int(x) for x in max_rgn_nums]
    int_list.sort(reverse=True)
    for u in int_list:
        if u < input_nr:
            time.sleep(15)
            return u
    return 0


before_pausa = []
# i = int(all_seed_range[1])
i = int('1235680074')
# while i > int(all_seed_range[0]):
while i > int('1197133308'):
    print('Checking number: ', i)
    if is_on_the_range(i):
        map_result = map_seed(i)
        if cur_map_res != 0 and cur_map_res < map_result:
            print('Mapping result: ', cur_map_res)
            break
        cur_map_res = map_result
        i -= 1
    else:
        before_pausa.append(i)
        i = get_first_av_number(i)
        cur_map_res = 0
print(before_pausa)


e_time = time.time()
print("Took, ", e_time - s_time, 's')

# Checking number:  4060249500
# 1426555552
# Checking number:  4060249499
# 1426555551
# Checking number:  4060249498
# 1426555550
# Checking number:  4060249497
# 1426555549
# Checking number:  4060249496
# 2873005387
# Mapping result:  1426555549
# [4464425380]
# Took,  487.9617609977722 s

# 4066309214 - start from and this is error
# 1235680074

# Incorrect resp:
# 1426555549
# 3532982064

# last range
