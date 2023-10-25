from class_blackjack import Blackjack
import random 

class BlackjackWithPRNG(Blackjack):
    def __init__(self, prng):
        deck = self.shuffled_deck(prng)
        super().__init__(deck)

    def shuffled_deck(self, prng):
        deck = [i for i in range(1, 12)] * 4
        shuffled = []
        while deck:
            index = int(next(prng) * len(deck))
            shuffled.append(deck.pop(index))
        return shuffled
    
def linear_congruential_generator():
    # Simplified parameters for LCG
    a, c, m = 1664525, 1013904223, 2**32
    seed = 1
    while True:
        seed = (a * seed + c) % m
        yield seed / m

def mersenne_twister():
    # Using Python's built-in Mersenne Twister
    while True:
        yield random.random()

def main():
    prng = linear_congruential_generator()  # or mersenne_twister()
    game = BlackjackWithPRNG(prng)
    print(game.play())

if __name__ == "__main__":
    main()
