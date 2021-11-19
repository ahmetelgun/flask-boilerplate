from flask import request, make_response, jsonify
import bcrypt
import html

from models import DBContext, User
from service import is_email


def register():
    try:
        data = request.json
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        password = data['password']
        validated_data = validate_register_fields(
            firstname, lastname, email, password)
        if not validated_data:
            raise Exception
    except:
        return make_response(jsonify(
            {"message": "Bad request"}
        ), 400)

    if write_user(validated_data):
        return make_response(jsonify(
            {"message": "Registration success"}
        ), 200)

    return make_response(jsonify(
        {"message": "Email already exists"}
    ), 409)


def write_user(data):
    firstname, lastname, email, password = data

    with DBContext() as db:
        if db.query(User).filter_by(email=email).first():
            return False

        user = User(firstname=firstname, lastname=lastname, email=email)
        user.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        db.add(user)
        db.commit()

    return True


def validate_register_fields(firstname, lastname, email, password):
    if type(firstname) == type(lastname) == type(email) == type(password) == str:
        if len(firstname) >= 2 and len(lastname) >= 2 and is_email(email) and len(password) >= 8:
            return html.escape(firstname), html.escape(lastname), email, password
    return False
