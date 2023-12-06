
filename = "day4_2.txt"

with open(filename) as f:
    content = f.read().splitlines()

edited_cards = []
for card in content:
    edited_cards.append(card[9:])

result = 0

for card in edited_cards:
    c_list = card.split(' | ')

    win_nums_list = c_list[0].split()
    user_nums_list = c_list[1].split()
    print(win_nums_list)
    print(user_nums_list)
    win_nums_list = list(map(int, win_nums_list))
    user_nums_list = list(map(int, user_nums_list))
    won = set(user_nums_list) - (set(user_nums_list) - set(win_nums_list))
    print(user_nums_list)
    print(win_nums_list)
    print('Won: ', won)

    i = 0
    count = 0
    for n in won:
        if count == 0:
           i = 1
        else:
            i *= 2
        count += 1

    result += i

print(result)