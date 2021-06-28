import jwt
from datetime import datetime

from settings import SECRET_KEY, TOKEN_MAX_AGE, TOKEN_REFRESH_TIME


def refresh_jwt(token):
    decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    expire_time = decoded_jwt['datetime']
    email = decoded_jwt['email']

    if expire_time <= (datetime.now().timestamp() + TOKEN_REFRESH_TIME):
        token = jwt.encode(
            {"email": email, "datetime": datetime.now().timestamp() + TOKEN_MAX_AGE}, SECRET_KEY, algorithm="HS256"
        )

    return token
