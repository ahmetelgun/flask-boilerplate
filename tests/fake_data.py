import bcrypt

from models import User, create_test_db


def create_fake_users():
     users = [
          User(firstname="Anakin", lastname="Skywalker", email="anakin@skywalker.space",
               password=bcrypt.hashpw(b"padme_amidala", bcrypt.gensalt())),
          User(firstname="Luke", lastname="Skywalker", email="luke@skywalker.space",
               password=bcrypt.hashpw(b"leia_skywalker", bcrypt.gensalt())),
          User(firstname="Obi Wan", lastname="Kenobi", email="obi@kenobi.space",
               password=bcrypt.hashpw(b"qui_gon_jinn", bcrypt.gensalt()))
     ]

     return users

def create_fake_data(TEST_DATABASE_URL):
    users = create_fake_users()
    return create_test_db(TEST_DATABASE_URL, users)
