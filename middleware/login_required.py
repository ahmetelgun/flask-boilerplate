from flask import request, make_response, jsonify
from datetime import datetime
from functools import wraps
import jwt

from models import DBContext, User
from settings import SECRET_KEY
from service import is_token_valid


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
