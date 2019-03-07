import unittest

from sum_list import sum_list, easy_sum_list


class TestSumList(unittest.TestCase):
    def test_when_numbers_are_positives(self):
        self.assertEqual(sum_list([100, 20]), 120)

    def test_when_numbers_are_negative(self):
        self.assertEqual(sum_list([-100, -20]), -120)

    def test_when_list_is_empty(self):
        self.assertEqual(sum_list([]), 0)


class TestEasySumList(unittest.TestCase):
    def test_when_numbers_are_positives(self):
        self.assertEqual(easy_sum_list([100, 20]), 120)

    def test_when_numbers_are_negative(self):
        self.assertEqual(easy_sum_list([-100, -20]), -120)

    def test_when_list_is_empty(self):
        self.assertEqual(easy_sum_list([]), 0)


if __name__ == '__main__':
    unittest.main()
