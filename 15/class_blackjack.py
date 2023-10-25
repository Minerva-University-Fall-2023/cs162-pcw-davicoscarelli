import random

class Blackjack:
    def __init__(self, deck = None):
        if deck is None:
            self.deck = self.shuffled_deck()
        else:
            self.deck = deck
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
    
    def shuffled_deck(self):
        deck = [i for i in range(1, 12)] * 4
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def calculate_score(self, hand):
        score = sum(hand)
        num_aces = hand.count(11)
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1
        return score

    def play(self):
        while self.calculate_score(self.player_hand) < 21:
            action = input("Do you want to hit or stay? ")
            if action == "hit":
                self.player_hand.append(self.deal_card())
            else:
                break

        while self.calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())

        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

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


def main():
    game = Blackjack()
    print(game.play())

if __name__ == "__main__":
    main()