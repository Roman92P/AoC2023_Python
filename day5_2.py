import numpy as np
import time

s_time = time.time()

# filename = "day5_2_b.txt"
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


def condition(cert_mapper, n):
    if int(cert_mapper[1]) <= n <= int(cert_mapper[1]) + int(cert_mapper[2]):
        return True
    return False


def filter_mappers(mappers, sd_num):
    fml = list(mappers)
    result = []
    for mapper in fml:
        filtered_lists = list(filter(lambda x: condition(x, sd_num), mapper))
        result.append(filtered_lists)

    return result


def map_seed_with_category(sd_num):
    right_mappers = filter_mappers(mappers, sd_num)
    # print('Mapping: ', sd_num, ' with using next mappers, ', mappers)
    sum_a = 0
    for mapper in mappers:
        for m in mapper:
            dest = int(m[0])
            src = int(m[1])
            rang = int(m[2])
            sd = int(sd_num)
            if src <= sd <= src + rang:
                sd_num = sd - src + dest
                break
            sum_a = sum_a + int(sd_num)
    #     print('Mapper: ', m, 'produces: ', sd_num)
    # print('Sum: ' + str(sum_a))

    # print('Result of mapping: ', sd_num)
    return [sd_num, sum_a]


def process_seeds():
    seed_rng_pair = []

    for i, s in enumerate(seeds_list):

        if i % 2 == 0:
            end_indx = i + 1
            temp = [s, seeds_list[end_indx]]
            seed_rng_pair.append(temp)

    print('Seed:Range pairs are: ', seed_rng_pair)

    results = []
    sums = []
    for s_r in seed_rng_pair:
        print("Processing pair: ", s_r)
        start = int(s_r[0])
        end = int(s_r[0]) + int(s_r[1])
        # s_r_list = np.arange(start, end, 100000)
        # result_s_r_l = np.vectorize(map_seed_with_category)(s_r_list)
        s_r_list = list(range(start, end, ))

        result_s_r_l = []
        for loop_index, srl in enumerate(s_r_list):
            temp_r = map_seed_with_category(srl)
            result_s_r_l.append(temp_r[0])
            # print('Current sums: ', temp_r[1])
            # print('New sum: ', sums)
            # if len(sums) > 0 and temp_r[1] < sums[len(sums) - 1]:
            #     break
            # else:
            #     sums.append(temp_r[1])
            print(loop_index)
        sums.clear()
        results.append(np.min(result_s_r_l))

    results.sort()
    print(results)


process_seeds()

e_time = time.time()
print("Took, ", e_time - s_time, ' min')
