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

for line in content:
    if line.__contains__('seeds:'):
        l_list = line.split(' ')
        l_list = [x for x in l_list if x.isdigit()]
        for h in l_list:
            seeds_list.append(h)

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

# print(seeds_list)
# print('_________________________________')
# print(seed_soil_map)
# print('_________________________________')
# print(soil_fertilizer_map)
# print('_________________________________')
# print(fertilizer_water_map)
# print('_________________________________')
# print(water_light_map)
# print('_________________________________')
# print(light_temp_map)
# print('_________________________________')
# print(temp_humidity_map)
# print('_________________________________')
# print(humidity_loc_map)

mappers = [
    seed_soil_map,
    soil_fertilizer_map,
    fertilizer_water_map,
    water_light_map,
    light_temp_map,
    temp_humidity_map,
    humidity_loc_map
]

# Map every seed to location
location = []


#  0 - destination range
#  1 - source range
#  2 - range length
def map_seed_with_category(sd_num, mapper):
    choosen_mapper = []
    for m in mapper:
        dest = int(m[0])
        src = int(m[1])
        rang = int(m[2])
        sd = int(sd_num)
        if src <= sd <= src + rang:
            choosen_mapper = m
            sd_num = dest + sd - src
            break
    return sd_num


for seed in seeds_list:
    for m in mappers:
        seed = map_seed_with_category(seed, m)
    location.append(seed)

print("Result locations list: ", min(location))
