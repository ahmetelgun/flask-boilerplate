from flask import Flask, g, request, make_response
from flask_expects_json import expects_json
import json

from service import set_token_to_response, refresh_jwt, is_token_valid
from controllers.auth import register, login, logout
from controllers import posts
from settings import FRONTEND_URL
from middleware import login_required
import schemas

app = Flask(__name__)


@app.before_request
def before_request():
    try:
        headers = request.headers
        bearer = headers.get('Authorization')
        token = bearer.split()[1]
        user = is_token_valid(token)
        if user:
            g.user = user
            g.token = token
        else:
            raise Exception

    except:
        g.token = None
        g.user = None

@app.after_request
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = FRONTEND_URL
    resp.headers['Access-Control-Allow-Headers'] = "content-type"

    new_token = refresh_jwt(g.token)
    return set_token_to_response(resp, new_token)


@app.route('/register', methods=['POST'])
@expects_json(schemas.register_schema)
def register_func():
    return register()


@app.route('/login', methods=['POST'])
@expects_json(schemas.login_schema)
def login_func():
    return login()


@app.route('/logout', methods=['GET'])
def logout_func():
    return logout()

@app.route('/posts/create', methods=['POST'])
@expects_json(schemas.posts_create)
@login_required
def posts_create_func(user):
    return posts.create(user)

@app.route('/', methods=['GET'])
@login_required
def index(user):
    return {"message": f"welcome, {user.firstname}"}


if __name__ == '__main__':
    app.run()
