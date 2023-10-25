from functional_blackjack import blackjack
import random 

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

def shuffled_deck(prng):
    deck = [i for i in range(1, 12)] * 4
    shuffled = []
    while deck:
        index = int(next(prng) * len(deck))
        shuffled.append(deck.pop(index))
    return shuffled

def blackjack_with_prng(prng):
    deck = shuffled_deck(prng)
    return blackjack(deck)


def main():
    # prng = linear_congruential_generator() 
    prng = mersenne_twister()  
    print(blackjack_with_prng(prng))

if __name__ == "__main__":
    main()