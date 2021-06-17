from datetime import datetime
import unittest
import jwt

from settings import SECRET_KEY
from middleware import is_token_valid


class TestLoginRequired(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.now = datetime.now().timestamp()
        cls.one_hour_later = cls.now + 3600
        cls.one_hour_before = cls.now - 3600

    def test_non_jwt(self):
        self.assertFalse(is_token_valid(""))
        self.assertFalse(is_token_valid("lmqwemwqkesad.qwlekm.lkmqwe"))

    def test_unreadable_jwt(self):
        unreadable_jwt = jwt.encode(
            {"email": "a@a.com", "datetime": self.one_hour_later}, "secret", algorithm="HS256"
        )
        self.assertFalse(is_token_valid(unreadable_jwt))

        unreadable_jwt = jwt.encode(
            {"email": "a@a.com", "datetime": self.one_hour_later}, "", algorithm="HS256"
        )
        self.assertFalse(is_token_valid(unreadable_jwt))

    def test_expired_jwt(self):
        expired_jwt = jwt.encode(
            {"email": "a@a.com", "datetime": self.now}, SECRET_KEY, algorithm="HS256"
        )
        self.assertFalse(is_token_valid(expired_jwt))

        expired_jwt = jwt.encode(
            {"email": "a@a.com", "datetime": self.one_hour_before}, SECRET_KEY, algorithm="HS256"
        )
        self.assertFalse(is_token_valid(expired_jwt))

    def test_unexisted_user(self):
        unexisted_user = jwt.encode(
            {"email": "a@a.space", "datetime": self.one_hour_later}, SECRET_KEY, algorithm="HS256"
        )
        self.assertFalse(is_token_valid(unexisted_user))

    def test_valid_token(self):
        valid_token = jwt.encode(
            {"email": "anakin@skywalker.space", "datetime": self.one_hour_later}, SECRET_KEY, algorithm="HS256"
        )
        user = is_token_valid(valid_token)
        self.assertEqual(user.email, "anakin@skywalker.space")
