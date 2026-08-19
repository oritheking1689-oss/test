import random
import dealer_says
#cards = [2, 2, 2, 2,]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_score(score):
    overall_score = sum(score)
    for card in score:
        if overall_score > 21:
            if card == 11:
                overall_score = overall_score - 10
    return overall_score



def should_take (amount):
    if amount < 21:
        random.sample(cards, 1)





player_chips = 100
dealer_chips = 100
game_not_over = True
print(dealer_says.opening_logo)
input("WELCOME TO THE SPADES CAVERN!\n PRESS any key to continue")
print("\n" * 50)
while game_not_over:

    print("\n" * 50)
    print(dealer_says.logo)
    dealer_cards = []
    dealer_cards += random.sample(cards, 2)
    check_score(dealer_cards)
    while True:
        print(f"you have {player_chips} chips")
        print(f"🂡 Dealer's first card: [{dealer_cards[0]}]")
        bet = input(f"⚪🔴🔵🟢⚫enter you're bet (maximum bet is 100)")
        bet_options = [str(x) for x in range(1,101)]
        try:
            if player_chips < int(bet):
                bet = 0
                print("\n" * 30)
                print("❌💸you dont have that kind of amount, try again would ya?\n\n")
            if bet in bet_options:
                print("\n" * 30)
                break
            elif str(bet) not in bet_options:
                print("\n" * 30)
                print("❌❌invalid option, try again\n\n")
            else:
                print("\n" * 30)
                print("❌❌invalid option, try again\n\n")
        except ValueError:
            print("\n" * 30)
            print("❌❌invalid option, try again\n\n")

    player_cards = []
    player_cards += random.sample(cards,2)
    print(f"⚪🔴🔵🟢⚫bet: {bet} chips\n")
    print(f"🂡 Dealer's card: [{dealer_cards[0]}]")
    print(f"🂢🂣 you,re cards: {player_cards}, score: {check_score(player_cards)}")
    print(f"💬 Dealer says: ''{dealer_says.dealer_line_starting_bet(check_score(player_cards))}''\n\n")



    while True:
        stand_or_draw = input("do you want to stand/draw? 's' for stand, 'd' for draw: ").strip().lower()

        if stand_or_draw == "d":
            player_cards += random.sample(cards, 1)
            print("\n" * 30)
            print(f"⚪🔴🔵🟢⚫bet: {bet} chips\n")
            print(f"🂡 Dealer's card: [{dealer_cards[0]}]")
            print(f"🂢🂣 you,re cards: {player_cards}, score: {check_score(player_cards)}")
            if check_score(player_cards) >= 22:
                break
        elif stand_or_draw == "s":
            print("\n" * 30)
            print(f"⚪🔴🔵🟢⚫bet: {bet} chips\n")
            print(f"🂡 Dealer's card: [{dealer_cards[0]}]")
            print(f"🂢🂣 you,re cards: {player_cards}, score: {check_score(player_cards)}")
            break
        else:
            print("\n" * 30)
            print("❌Invalid option! Please type 's' for stand or 'd' for draw.\n\n\n")
            print(f"⚪🔴🔵🟢⚫bet: {bet} chips\n")
            print(f"🂡 Dealer's card: [{dealer_cards[0]}]")
            print(f"🂢🂣 you,re cards: {player_cards}, score: {check_score(player_cards)}")
    while check_score(dealer_cards) < 16:
        dealer_cards += random.sample(cards,1)


    #win lose code
    winner = ""
    dealer_score = check_score(dealer_cards)
    player_score = check_score(player_cards)
    if player_score == dealer_score:
        winner = "it is a DRAW, keep you're own"
    elif player_score > dealer_score:
        if player_score <= 21:
            winner = "YOU WON"
            dealer_chips -= int(bet)
            player_chips += int(bet)
        else:
            winner = "you bust, you lose to the house"
            dealer_chips += int(bet)
            player_chips -= int(bet)
    elif dealer_score > player_score:
        if dealer_score <= 21:
            winner = "dealer wins, you lose to the house"
            dealer_chips += int(bet)
            player_chips -= int(bet)
        else:
            winner = "dealer BUSTED!, YOU WIN"
            dealer_chips -= int(bet)
            player_chips += int(bet)


    print("\n" * 30)
    print(f"🂡 dealer cards {dealer_cards}, dealer hand score: {check_score(dealer_cards)}")
    print(f"🂢🂣 you're cards: {player_cards}, you're hand score: {check_score(player_cards)}")
    print(f"⚪🔴🔵🟢⚫{winner} {bet} chips. you have {player_chips} now.\ndealer has {dealer_chips} chips.")




    if int(dealer_chips) <= 0:
        print("\n" * 30)
        print("as you grab you,re cash and go outside...\nremembering what happened tonight...\n you know that just like you end up a winner...\nyou could go outside in a different time as a loser.....")
        print("and as you past the entrench door...\nlooking dawn at the floor\nsmiling a little from the win...\nand going to start you're new beginning.....")
        game_not_over = False

    elif int(player_chips) <= 0:
        print("\n" * 30)
        print(f"\n\n\n\n\nyou got {player_chips} chips left\n\n\n")
        print("you lost you're pants at the spades cavern...\ni hoped you learned you're lesson...\nif you gamble all you got...\nyou might lose it all to just some bed luck.....")
        game_not_over = False
    else:
        keep_going = input("\n\n\npress any key to continue...")




#TODO - fix the bag that the dealer says the same thing.
