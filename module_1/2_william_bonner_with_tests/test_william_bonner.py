import unittest

from william_bonner import say_good_night


class TestSayGoodNight(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(say_good_night(), 'Boa noite.')


if __name__ == '__main__':
    unittest.main()
