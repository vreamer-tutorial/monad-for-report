import unittest
from operator import neg

from src.monad import Failure


def get_neg_str(num):
    result = Failure(num) | int | neg | str
    return result.get()


class TestMonad(unittest.TestCase):
    def test_get_neg_str_when_number_is_valid(self):
        self.assertEqual('-1', get_neg_str(1))

    # @unittest.skip
    def test_get_neg_str_when_number_is_not_valid(self):
        self.assertEqual(None, get_neg_str('XYZ'))
