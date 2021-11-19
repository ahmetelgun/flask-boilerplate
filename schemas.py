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

posts_create = {
    'type': 'object',
    'properties': {
        'title': {'type': 'string'},
        'text': {'type': 'string'},
        'is_deleted': {'type': 'boolean'},
        'is_draft': {'type': 'boolean'}
    },
    'required': ['title', 'text', 'is_deleted', 'is_draft']
}