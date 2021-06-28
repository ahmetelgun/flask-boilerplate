from flask import request, g, make_response, jsonify
import bcrypt

from service import is_email, create_jwt
from models import DBContext, User


def login():
    try:
        data = request.json
        email = data['email']
        password = data['password']
        validated_data = validate_login_fields(email, password)

        if not validated_data:
            raise Exception

    except:
        return make_response(jsonify(
            {"message": "Bad request"}
        ), 400)

    user = is_login(email, password)
    if user:
        g.token = create_jwt(user.email)
        return make_response(jsonify(
            {"message": "Login success"}
        ), 200)
    
    return make_response(jsonify(
        {"message": "Username or password is incorrect"}
    ), 401)


def is_login(email, password):
    with DBContext() as db:
        user = db.query(User).filter_by(email=email).first()

    if user and bcrypt.checkpw(password.encode(), user.password):
        return user
    return False


def validate_login_fields(email, password):
    if type(email) == type(password) == str:
        if is_email(email) and len(password) >= 8:
            return email, password
    return False
