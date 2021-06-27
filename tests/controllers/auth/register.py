import unittest

from models import DBContext, User
from controllers.auth import validate_register_fields, write_user


class TestRegister(unittest.TestCase):

    def test_validate_register_fields(self):
        valid_firstname = "asd"
        non_valid_firstname = "a"

        valid_lastname = "qwe"
        non_valid_lastname = "q"

        valid_email = "asd@asd.com"
        non_valid_email = "asd@asd.c"

        valid_password = "12345678"
        non_valid_password = "1234567"

        # False
        self.assertFalse(validate_register_fields(
            non_valid_firstname, valid_lastname, valid_email, valid_password))  # nvvv -- n -> non-valid -- v -> valid
        self.assertFalse(validate_register_fields(
            valid_firstname, non_valid_lastname, valid_email, valid_password))  # vnvv
        self.assertFalse(validate_register_fields(
            valid_firstname, valid_lastname, non_valid_email, valid_password))  # vvnv
        self.assertFalse(validate_register_fields(
            valid_firstname, valid_lastname, valid_email, non_valid_password))  # vvvn
        self.assertFalse(validate_register_fields(
            non_valid_firstname, valid_lastname, valid_email, non_valid_password))  # nvvn
        self.assertFalse(validate_register_fields(
            non_valid_firstname, non_valid_lastname, non_valid_email, non_valid_password))  # nnnn

        # True
        self.assertTrue(validate_register_fields(
            valid_firstname, valid_lastname, valid_email, valid_password))  # vvvv

    def test_write_user(self):
        # exist user
        self.assertFalse(write_user(
            ["anakin", "skywalker", "anakin@skywalker.space", b"12345678"]))

        # new user
        self.assertTrue(write_user(
            ["master", "yoda", "master@yoda.space", b"12345678"]))
