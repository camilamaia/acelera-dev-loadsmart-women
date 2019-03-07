#!/bin/python3
import unittest

from sum import sum_two_values


class TestSumTwoValues(unittest.TestCase):
    def test_when_two_positive_numbers(self):
        self.assertEqual(sum_two_values(2, 5), 7)

    def test_when_one_number_is_negative(self):
        self.assertEqual(sum_two_values(-2, 2), 0)


if __name__ == '__main__':
    unittest.main()
