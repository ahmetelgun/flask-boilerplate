import re


def is_email(email):
    regex = r"[A-Za-z0-9\._-]+@[A-Za-z0-9\._-]+\.[A-Za-z]{2,}"
    if(re.search(regex, email)):
        return True
    return False
