import re


def create_endpoint(date, title):
    year = date.year
    month = date.month
    day = date.day

    title = re.sub('\W+', '-', title)
    title = title.strip('-').lower()
    if len(title) == 0:
        return False

    return f"/{year}/{month}/{day}/{title}"
