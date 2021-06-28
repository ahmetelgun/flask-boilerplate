from datetime import datetime
import unittest
import jwt

from settings import SECRET_KEY, TOKEN_MAX_AGE, TOKEN_REFRESH_TIME
from service import refresh_jwt


class TestRefreshJWT(unittest.TestCase):
    def test_refresh(self):
        age = datetime.now().timestamp() + TOKEN_REFRESH_TIME - 10
        token = jwt.encode({"email": "asd", "datetime": age},
                           SECRET_KEY, algorithm="HS256")
        new_token = refresh_jwt(token)
        self.assertNotEqual(token, new_token)

        age = datetime.now().timestamp() + TOKEN_REFRESH_TIME
        token = jwt.encode({"email": "asd", "datetime": age},
                           SECRET_KEY, algorithm="HS256")
        new_token = refresh_jwt(token)
        self.assertNotEqual(token, new_token)

    def test_not_refresh(self):
        age = datetime.now().timestamp() + TOKEN_REFRESH_TIME + 10
        token = jwt.encode({"email": "asd", "datetime": age},
                           SECRET_KEY, algorithm="HS256")
        new_token = refresh_jwt(token)
        self.assertEqual(token, new_token)
