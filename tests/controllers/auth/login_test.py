import unittest

from controllers.auth import is_login, validate_login_fields


class TestLogin(unittest.TestCase):

    def test_is_login(self):
        anakin_email = "anakin@skywalker.space"
        anakin_password = "padme_amidala"

        # wrong password
        self.assertFalse(is_login(anakin_email, "12345678"))
        # wrong email
        self.assertFalse(is_login("a@a.com", anakin_password))
        # success
        self.assertEqual(anakin_email, is_login(anakin_email, anakin_password).email)

    def test_validate_login_fields(self):
        valid_email = "asd@asd.com"
        non_valid_email = "asd@asd.c"

        valid_password = "12345678"
        non_valid_password = "1234567"

        # false
        self.assertFalse(validate_login_fields(non_valid_email, valid_password)) # nv
        self.assertFalse(validate_login_fields(valid_email, non_valid_password)) # vn
        self.assertFalse(validate_login_fields(non_valid_email, non_valid_password)) # nn

        # true
        self.assertTrue(validate_login_fields(valid_email, valid_password)) # vv

