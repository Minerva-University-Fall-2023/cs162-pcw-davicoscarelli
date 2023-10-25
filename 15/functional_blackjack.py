import random

def shuffled_deck():
    deck = [i for i in range(1, 12)] * 4  
    random.shuffle(deck)  
    return deck

def deal_card(deck):
    return deck.pop()

def calculate_score(hand):
    score = sum(hand)
    num_aces = hand.count(11)
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def blackjack(deck):
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    while calculate_score(player_hand) < 21:
        action = input("Do you want to hit or stay? ")
        if action == "hit":
            player_hand.append(deal_card(deck))
        else:
            break
    
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("Final score: ", player_score)
    
    if player_score > 21:
        return "Player busts!"
    elif dealer_score > 21:
        return "Dealer busts!"
    elif player_score > dealer_score:
        return "Player wins!"
    elif dealer_score > player_score:
        return "Dealer wins!"
    else:
        return "It's a tie!"


# Comment these lines when running functional_blackjack_prng.py
# deck = shuffled_deck()
# print(blackjack(deck))

