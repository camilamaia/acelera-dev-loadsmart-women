import unittest

from double_list import double_list


class TestSumList(unittest.TestCase):
    def test_when_there_are_numbers(self):
        self.assertEqual(double_list([100, 20]), [200, 40])

    def test_when_list_is_empty(self):
        self.assertEqual(double_list([]), [])


if __name__ == '__main__':
    unittest.main()
