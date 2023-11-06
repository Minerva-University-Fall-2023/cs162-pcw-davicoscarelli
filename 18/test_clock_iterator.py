import unittest
from clock_iterator import ClockIterator

class TestClockIterator(unittest.TestCase):

    def test_midnight(self):
        clock = ClockIterator()
        self.assertEqual(next(clock), "00:00", "Midnight looks like '00:00', right?")

    def test_one_minute_past_midnight(self):
        clock = ClockIterator()
        next(clock)  # Skip midnight
        self.assertEqual(next(clock), "00:01", "One minute past midnight should be '00:01'.")

    def test_rollover(self):
        clock = ClockIterator()
        for _ in range(1439):  # Fast forward to 23:59
            next(clock)
        self.assertEqual(next(clock), "23:59", "Just before the day rolls over, it's '23:59'.")
        self.assertEqual(next(clock), "00:00", "And then we're back to the start, '00:00'.")

if __name__ == '__main__':
    unittest.main()
