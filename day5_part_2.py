import time

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

number_to_check = 0

found_number = []


def number_is_min(number_to_check):
    for mapper in reversed(mappers):
        for m in mapper:
            destination = m[0]
            source = m[1]
            rang = m[2]
            if destination <= number_to_check <= destination + (rang - 1):
                number_to_check = source + (number_to_check - destination)
                print(number_to_check)

    print('Found min: ', number_to_check)
    if len(found_number) > 0 and found_number[-1] < number_to_check:
        return True
    found_number.append(number_to_check)
    return False


while True:
    if number_is_min(number_to_check):
        print('Minimum location number is: ', number_to_check)
        break
    number_to_check += 1

e_time = time.time()
print("Took, ", e_time - s_time, 's')

# Incorrect resp:
# 1426555549
# 3532982064
