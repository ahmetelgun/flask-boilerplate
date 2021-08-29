from flask import request, make_response, jsonify, g
from datetime import datetime
from functools import wraps
import jwt

from models import DBContext, User
from settings import SECRET_KEY
from service import is_token_valid


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        not_authenticated_response = make_response(
            jsonify({"message": "Login required"}),
            401
        )

        if g.user:
            return func(g.user, *args, **kwargs)

        return not_authenticated_response

    return wrapper
