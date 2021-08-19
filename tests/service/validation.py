import unittest
from service import validate


class TestValidate(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(validate([], [str]))
        self.assertFalse(validate(["s"], []))

    def test_different_length(self):
        self.assertFalse(validate(["s"], [str, str]))
        self.assertFalse(validate(["s", "s"], [str]))

    def test_unmatched(self):
        self.assertFalse(validate([5], [str]))
        self.assertFalse(validate([5], [float]))
        self.assertFalse(validate(["sda"], [int]))
        self.assertFalse(validate(["sda"], [list]))
        self.assertFalse(validate(["sda", 5], [list, int]))
        self.assertFalse(validate([b"sda"], [str]))

    def test_match(self):
        self.assertTrue(validate([], []))
        self.assertTrue(validate(["str"], [str]))
        self.assertTrue(validate([1, "asd"], [int, str]))
        self.assertTrue(validate(["str", 1, 0.5, [1,2]], [str, int, float, list]))