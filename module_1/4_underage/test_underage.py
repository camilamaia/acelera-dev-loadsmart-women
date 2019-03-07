import unittest

from underage import is_underage


class TestSumTwoValues(unittest.TestCase):
    def test_when_age_is_less_than_18(self):
        self.assertTrue(is_underage(10))

    def test_when_age_is_greater_than_18(self):
        self.assertFalse(is_underage(25))

    def test_when_age_is_18(self):
        self.assertFalse(is_underage(18))

    def test_when_age_is_negative(self):
        self.assertEqual(is_underage(-200),
                         'Invalid age, it only accepts positive numbers')


if __name__ == '__main__':
    unittest.main()
