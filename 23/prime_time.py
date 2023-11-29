# prime_time.py

def is_prime(number):
    """Deterministic test for primality: simple but slow."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(number):
    """Find the next prime number after the given number."""
    if not isinstance(number, int):
        raise ValueError("Listen, I need an integer to find the next prime. Try again.")
    number += 1
    while not is_prime(number):
        number += 1
    return number
