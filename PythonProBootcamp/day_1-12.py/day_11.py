import random
deler = []
player = []
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = cards[random.randint(0,12)]
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(player_score, deler_score):
    if player_score == deler_score:
        return "Draw"
    elif deler_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "Win with a Blackjack"
    elif player_score > 21:
        return "You went over. You lose"
    elif deler_score > 21:
        return "Opponent went over. You win"
    elif player_score > deler_score:
        return "You win"
    else:
        return "You lose"
   
while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    print("\n" * 50)
    player.clear()
    deler.clear()
    player.append(deal_card())
    deler.append(deal_card())
    player.append(deal_card())
    deler.append(deal_card())

    print(f"Your cards: {player}, current score: {calculate_score(player)}")
    print(f"Deler's first card: {deler[0]}")
    while calculate_score(player) != 0 and calculate_score(deler) != 0 and calculate_score(player) < 21:
        if input("\nType 'yes' to get another card, type 'no' to pass:") == "yes":
            player.append(deal_card())
            print(f"Your cards: {player}, current score: {calculate_score(player)}")
            print(f"Deler's first card: {deler[0]}")
        else:
            break
    while calculate_score(deler) != 0 and calculate_score(deler) < 17:
        deler.append(deal_card())
    print(f"\nYour final hand: {player}, final score: {calculate_score(player)}")
    print(f"Deler's final hand: {deler}, final score: {calculate_score(deler)}\n")
    print(compare(calculate_score(player), calculate_score(deler)))
