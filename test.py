


import random
import dealer_says
cards = [2, 2, 2, 2,]
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_cards += random.sample(cards,2)


def check_score(score):
    overall_score = sum(score)
    for card in score:
        if overall_score > 21:
            if card == 11:
                overall_score = overall_score - 10
    return overall_score


def dealer_line(score):
    return random.choice(cards[score])


# while True:
#     saying = dealer_says.cards[check_score(player_cards)]
#     print(saying)
#     input("Press any key to continue...")