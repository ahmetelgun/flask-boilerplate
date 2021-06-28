from flask import Flask, g, request, make_response

from service import set_token_to_response, refresh_jwt
from controllers.auth import register, login

app = Flask(__name__)


@app.before_request
def before_request():
    g.token = request.cookies.get("token")


@app.after_request
def after_request(resp):
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


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()
