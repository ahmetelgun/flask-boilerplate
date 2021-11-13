register_schema = {
    'type': 'object',
    'properties': {
        'firstname': {'type': 'string'},
        'lastname': {'type': 'string'},
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['firstname', 'lastname', 'email', 'password']
}

login_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}