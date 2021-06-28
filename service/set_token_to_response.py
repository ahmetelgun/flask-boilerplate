from settings import BACKEND_DOMAIN, TOKEN_MAX_AGE


def set_token_to_response(response, token=None):
    if not token:
        response.set_cookie(
            'token', "", max_age=1, domain=BACKEND_DOMAIN, path="/", secure=True, httponly=True)
        return response

    response.set_cookie('token', token, max_age=TOKEN_MAX_AGE,
                        domain=BACKEND_DOMAIN, path="/", secure=True, httponly=True)
    return response
