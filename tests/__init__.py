from .fake_data import create_users

def init_tests():
    from tests import create_users
    from settings import TEST_DATABASE_URL
    import models
    models.DATABASE_URL = TEST_DATABASE_URL
    create_users(TEST_DATABASE_URL)

init_tests()