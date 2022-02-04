from .fake_data import create_fake_data
from settings import TEST_DATABASE_URL
import models

def init_tests():
    models.DATABASE_URL = TEST_DATABASE_URL
    create_fake_data(TEST_DATABASE_URL)

init_tests()