# settings.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")
TEST_DATABASE_URL = os.environ.get("TEST_DATABASE_URL")
HTTPS = os.environ.get("HTTPS")
BACKEND_DOMAIN = os.environ.get("BACKEND_DOMAIN")    
BACKEND_PORT = os.environ.get("BACKEND_PORT")    
TOKEN_MAX_AGE = int(os.environ.get("TOKEN_MAX_AGE"))
TOKEN_REFRESH_TIME = int(os.environ.get("TOKEN_REFRESH_TIME"))

BACKEND_URL = f"{HTTPS}{BACKEND_DOMAIN}:{BACKEND_PORT}"