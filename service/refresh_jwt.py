import jwt
from datetime import datetime

from settings import SECRET_KEY, TOKEN_MAX_AGE, TOKEN_REFRESH_TIME
from .create_jwt import create_jwt


def refresh_jwt(token):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        expire_time = decoded_jwt['datetime']
        email = decoded_jwt['email']

        if expire_time <= (datetime.now().timestamp() + TOKEN_REFRESH_TIME):
            token = create_jwt(email)
    except:
        token = None
    return token
