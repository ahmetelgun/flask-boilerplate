from settings import TOKEN_MAX_AGE, BACKEND_DOMAIN


def set_token_to_response(response, token=None):
    if token:
        response.headers['Autherization'] = f"Bearer {token}"
    return response
