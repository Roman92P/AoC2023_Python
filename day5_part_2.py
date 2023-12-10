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
                temp = [int(s), int(seeds_list[end_indx])]
                seed_rng_pair.append(temp)

for indx, i in enumerate(content):
    if i.__contains__('seed-to-soil map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                a = next_l.split(' ')
                a = [int(x) for x in a]
                seed_soil_map.append(a)
            else:
                break
            indx = new_indx

    if i.__contains__('soil-to-fertilizer map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                a = next_l.split(' ')
                a = [int(x) for x in a]
                soil_fertilizer_map.append(a)
            else:
                break
            indx = new_indx
    if i.__contains__('fertilizer-to-water map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                a = next_l.split(' ')
                a = [int(x) for x in a]
                fertilizer_water_map.append(a)
            else:
                break
            indx = new_indx
    if i.__contains__('water-to-light map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                a = next_l.split(' ')
                a = [int(x) for x in a]
                water_light_map.append(a)
            else:
                break
            indx = new_indx
    if i.__contains__('light-to-temperature map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                a = next_l.split(' ')
                a = [int(x) for x in a]
                light_temp_map.append(a)
            else:
                break
            indx = new_indx
    if i.__contains__('temperature-to-humidity map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                a = next_l.split(' ')
                a = [int(x) for x in a]
                temp_humidity_map.append(a)
            else:
                break
            indx = new_indx
    if i.__contains__('humidity-to-location map:'):
        while True:
            if indx + 1 < len(content):
                new_indx = indx + 1
                next_l = content[new_indx]
                if len(next_l) > 0 and next_l[0].isdigit():
                    a = next_l.split(' ')
                    a = [int(x) for x in a]
                    humidity_loc_map.append(a)
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

while True:



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
