import jwt
from datetime import datetime

from settings import TOKEN_MAX_AGE, SECRET_KEY


def create_jwt(email):
    token = jwt.encode(
        {"email": email, "datetime": datetime.now().timestamp() + TOKEN_MAX_AGE}, SECRET_KEY, algorithm="HS256"
    )

    return token