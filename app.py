from flask import Flask, g, request, make_response
import json

from service import set_token_to_response, refresh_jwt
from controllers.auth import register, login, logout
from settings import FRONTEND_URL

app = Flask(__name__)


@app.before_request
def before_request():
    g.token = request.cookies.get("token")


@app.after_request
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = FRONTEND_URL
    resp.headers['Access-Control-Allow-Headers'] = "content-type"
    resp.headers['Access-Control-Allow-Credentials'] = "true"

    if g.token:
        new_token = refresh_jwt(g.token)
        return set_token_to_response(resp, new_token)
    return set_token_to_response(resp)


@app.route('/register', methods=['POST'])
def register_func():
    return register()


@app.route('/login', methods=['POST'])
def login_func():
    return login()


@app.route('/logout')
def logout_func():
    return logout()


@app.route('/')
def index():
    return {"name": "asd"}


if __name__ == '__main__':
    app.run()
