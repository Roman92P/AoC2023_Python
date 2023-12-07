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

for l in content:
    if l.__contains__('seeds:'):
        seeds_list.append(l)

for indx, i in enumerate(content):
    if i.__contains__('seed-to-soil map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                seed_soil_map.append(next_l)
            else:
                break
            indx = new_indx

    if i.__contains__('soil-to-fertilizer map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                soil_fertilizer_map.append(next_l)
            else:
                break
            indx = new_indx
    if i.__contains__('fertilizer-to-water map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                fertilizer_water_map.append(next_l)
            else:
                break
            indx = new_indx
    if i.__contains__('water-to-light map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                water_light_map.append(next_l)
            else:
                break
            indx = new_indx
    if i.__contains__('light-to-temperature map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                light_temp_map.append(next_l)
            else:
                break
            indx = new_indx
    if i.__contains__('temperature-to-humidity map:'):
        while True:
            new_indx = indx + 1
            next_l = content[new_indx]
            if len(next_l) > 0 and next_l[0].isdigit():
                temp_humidity_map.append(next_l)
            else:
                break
            indx = new_indx
    if i.__contains__('humidity-to-location map:'):
        while True:
            if indx + 1 < len(content):
                new_indx = indx + 1
                next_l = content[new_indx]
                if len(next_l) > 0 and next_l[0].isdigit():
                    humidity_loc_map.append(next_l)
                else:
                    break
                indx = new_indx
            else:
                break

print(seeds_list)
print('_________________________________')
print(seed_soil_map)
print('_________________________________')
print(soil_fertilizer_map)
print('_________________________________')
print(fertilizer_water_map)
print('_________________________________')
print(water_light_map)
print('_________________________________')
print(light_temp_map)
print('_________________________________')
print(temp_humidity_map)
print('_________________________________')
print(humidity_loc_map)