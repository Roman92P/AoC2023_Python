import time
from typing import Optional

s_time = time.time()

filename = "day5_1.txt"

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


def number_is_min(number_to_check):
    process_num = number_to_check
    for mapper in reversed(mappers):
        for m in reversed(mapper):
            print('Checking: ', number_to_check, ' in mapper: ', m)
            destination = m[0]
            source = m[1]
            rang = m[2]
            if destination <= process_num <= destination + (rang - 1):
                process_num = source + (process_num - destination)
            print('New number is: ', process_num)
    prev = 'Empty'
    if len(found_number) > 0:
        prev = found_number[-1]
    print('Found min: ', process_num, '. Previously found number is: ', prev)
    if len(found_number) > 0 and found_number[-1] < process_num:
        if belong_to_ranges(number_to_check):
            number_to_check = process_num
            return True
    found_number.append(process_num)
    print('Finished verification')
    return False


def belong_to_ranges(number_to_check):
    for r in seed_rng_pair:
        if r[0] <= number_to_check <= r[0] + r[1]:
            return True
    return False


def get_min_from_seeds():
    seed_starts_l = [item[0] for item in seed_rng_pair]
    return min(seed_starts_l)


loc_to_check = 0

while True:
    if number_is_min(loc_to_check):
        print('Minimum location number is: ', loc_to_check)
        break
    loc_to_check += 1

e_time = time.time()
print("Took, ", e_time - s_time, 's')

# 166557950 - 2059461237
