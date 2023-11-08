# test_prime_time.py

import unittest
from prime_time import is_prime, next_prime

class TestPrimeTime(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(1), "1 is not prime, and never will be.")
        self.assertTrue(is_prime(2), "2 is prime, and that's the truth.")
        self.assertTrue(is_prime(11), "11 is prime, and don't you forget it.")
        self.assertFalse(is_prime(15), "15 is as prime as a slice of pizza.")

    def test_next_prime(self):
        self.assertEqual(next_prime(2), 3, "The next prime after 2 should be 3.")
        self.assertEqual(next_prime(14), 17, "Come on, even a child knows that the next prime after 14 is 17.")

    def test_next_prime_with_floats(self):
        with self.assertRaises(ValueError):
            next_prime(3.5)

    def test_next_prime_with_strings(self):
        with self.assertRaises(ValueError):
            next_prime("What's a prime?")

if __name__ == '__main__':
    unittest.main()
