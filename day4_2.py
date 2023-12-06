import re

filename = "day4_2.txt"


with open(filename) as f:
    content = f.read().splitlines()

process_card_ids = []

content_copy = content.copy()


def process_card(card):
    c_list = re.split(': | \\|', card)
    current_card_id = re.findall(r'\d', c_list[0])
    process_card_ids.append(current_card_id)

    win_nums_list = c_list[1].split()
    user_nums_list = c_list[2].split()

    win_nums_list = list(map(int, win_nums_list))
    user_nums_list = list(map(int, user_nums_list))
    won = set(user_nums_list) - (set(user_nums_list) - set(win_nums_list))

    won_cards_ids = []

    for idx, n in enumerate(won):
        won_cards_ids.append(int(idx + 1) + int(''.join(current_card_id)))

    for k in won_cards_ids:
        process_card(content[k-1])
    return won_cards_ids


copy_card_id = []
for card in content:
    c_l = re.split(': | \\|', card)
    cc_id = re.findall(r'\d', c_l[0])
    r = process_card(card)
    copy_card_id.append(r)
    print('Id card: ', ''.join(cc_id), ': ', r)


print(len(process_card_ids))


