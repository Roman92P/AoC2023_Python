
import re

filename = "day4_1.txt"

# Process all of the original and copied scratchcards until no more scratchcards are won.
# Including the original set of scratchcards, how many total scratchcards do you end up with?

with open(filename) as f:
    content = f.read().splitlines()

process_card_ids = []


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
    return won_cards_ids


for card in content:
    copy_card_id = process_card(card)
    print(copy_card_id)

print(process_card_ids)