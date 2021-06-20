import unittest
from service import is_email


class TestIsEmail(unittest.TestCase):

    def test_not_email(self):
        self.assertFalse(is_email("asd@.com"))
        self.assertFalse(is_email("asd@com"))
        self.assertFalse(is_email("asdcom"))
        self.assertFalse(is_email("asd.asd@com"))
        self.assertFalse(is_email("asd@c.c"))

    def test_email(self):
        self.assertTrue(is_email("asd@asd.co"))
        self.assertTrue(is_email("asd@asd.com"))
        self.assertTrue(is_email("asd.asd@asd.com"))
        self.assertTrue(is_email("asd.asd@asd.asd.com"))
        self.assertTrue(is_email("asd_asd.asd@asd.asd.com"))
        self.assertTrue(is_email("asd_asd-asd.asd@asd.asd.com"))
