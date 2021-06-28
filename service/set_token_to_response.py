from settings import BACKEND_DOMAIN, TOKEN_MAX_AGE


def set_token_to_response(response, token=None):
    if not token:
        response.set_cookie("token", "", max_age=TOKEN_MAX_AGE, path="/",
                            domain=BACKEND_DOMAIN, secure=True, httponly=True, samesite="Lax")
        return response

    response.set_cookie("token", token, max_age=TOKEN_MAX_AGE, path="/",
                        domain=BACKEND_DOMAIN, secure=True, httponly=True, samesite="Lax")
    return response
