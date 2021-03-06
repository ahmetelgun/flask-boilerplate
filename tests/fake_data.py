import bcrypt

from models import User, create_test_db


def create_users(TEST_DATABASE_URL):
    users = [
        User(firstname="Anakin", lastname="Skywalker", email="anakin@skywalker.space",
             password=bcrypt.hashpw(b"padme_amidala", bcrypt.gensalt())),
        User(firstname="Luke", lastname="Skywalker", email="luke@skywalker.space",
             password=bcrypt.hashpw(b"leia_skywalker", bcrypt.gensalt())),
        User(firstname="Obi Wan", lastname="Kenobi", email="obi@kenobi.space",
             password=bcrypt.hashpw(b"qui_gon_jinn", bcrypt.gensalt()))
    ]
    return create_test_db(TEST_DATABASE_URL, users)
