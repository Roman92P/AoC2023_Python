import time
from typing import Optional

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

found_number = []
rs_map = {}


def number_is_min(location_to_check):
    print('Checking: ', location_to_check)
    process_num = location_to_check
    for mapper in reversed(mappers):
        tmp_num = process_num
        for m in reversed(mapper):
            # print('Location: ', number_to_check, ' in mapper: ', m)
            destination = m[0]
            source = m[1]
            rang = m[2]
            if destination == process_num or destination < process_num < destination + rang:
                # print('Changing ', process_num, ' in mapper: ', m)
                tmp_num = source + (process_num - destination)
        # print('Changed number is: ', process_num)
        process_num = tmp_num
    rs_map[location_to_check] = process_num

    if belong_to_ranges(process_num):
        # number_to_check = process_num
        print('Found min: ', process_num)
        # print('All found numbers: ', found_number)
        return True
    found_number.append(process_num)
    # print('Finished verification')
    return False


def belong_to_ranges(number_to_check):
    for r in seed_rng_pair:
        if r[0] <= number_to_check <= (r[0] + r[1]):
            # print('Found in range: ', r)
            return True
    return False


# 3191849478
# min is
# 3960442213
def get_min_from_seeds():
    seed_starts_l = [item[0] for item in seed_rng_pair]
    return min(seed_starts_l)


# print(get_min_from_seeds())
# print(seed_rng_pair)
# print(belong_to_ranges(503983169))

# map seed to location
def map_seed_with_category(sd_num):
    for mapper in mappers:
        temp_n = sd_num
        for m in mapper:
            des = int(m[0])
            src = int(m[1])
            rang = int(m[2])
            if sd_num == src or src < sd_num < src + rang:
                temp_n = des + sd_num - src
                print(m)
        sd_num = temp_n

    return sd_num


# print(map_seed_with_category(3191849478))
# print(map_seed_with_category(82))
# 3969171812 - 79874952
location = 0
while True:
    if number_is_min(location):
        print('Minimum location number is: ', location)
        break
    location += 1

e_time = time.time()
# print(rs_map)
print("Took, ", e_time - s_time, 's')
