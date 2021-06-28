from flask import g, make_response, jsonify


def logout():
    g.token = ""
    return make_response(jsonify(
        {"message": "success"}
    ), 200)
