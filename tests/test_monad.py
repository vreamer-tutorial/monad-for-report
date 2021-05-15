import unittest
from operator import neg


def get_neg_str(num):
    return str(neg(int(num)))


class TestMonad(unittest.TestCase):
    def test_get_neg_str_when_number_is_valid(self):
        self.assertEqual('-1', get_neg_str(1))

    @unittest.skip
    def test_get_neg_str_when_number_is_not_valid(self):
        self.assertEqual(None, get_neg_str('XYZ'))
