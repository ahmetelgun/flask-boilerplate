from flask import request, make_response, jsonify
from datetime import datetime
from functools import wraps
import jwt

from models import DBContext, User
from settings import SECRET_KEY


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        not_authenticated_response = make_response(jsonify(
            {"message": "Login required"}
        ), 401)

        if not token:
            return not_authenticated_response

        user = is_token_valid(token)
        if user:
            return func(user, *args, **kwargs)

        return not_authenticated_response

    return wrapper


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
