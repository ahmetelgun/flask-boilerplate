from flask import Flask, g, request

from service import set_token_to_response, refresh_jwt

app = Flask(__name__)


@app.before_request
def before_request():
    try:
        token = request.cookies.get(token)
    except:
        token = ""
    g.token = token


@app.after_request
def after_request(resp):
    if g.token:
        new_token = refresh_jwt(g.token)
        return set_token_to_response(resp, new_token)
    return set_token_to_response(resp)


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()
