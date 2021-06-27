import jwt
from datetime import datetime

from models import DBContext, User
from settings import SECRET_KEY


def is_token_valid(token):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        expire_time = decoded_jwt['datetime']
        email = decoded_jwt['email']
    except:
        return False

    if expire_time <= datetime.now().timestamp():
        return False

    with DBContext() as db:
        user = db.query(User).filter_by(email=email).first()

    if user:
        return user
    return False
