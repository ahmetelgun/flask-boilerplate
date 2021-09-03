from flask import g, request, escape
from datetime import datetime
import random

from models import Post, DBContext
from service import validate


def posts_create():
    try:
        data = request.json
        title = str(escape(data['title'])).strip()
        body = data['body']
        is_draft = data['is_draft']
        if not validate([title, body, is_draft], [str, str, bool]):
            raise Exception
        if 1 > len(title) or 1 > len(body):
            raise Exception
    except:
        return {"status": "error", "message": "Request body is invalid"}, 400

    with DBContext() as db:
        endpoint = "-".join(title.lower().split())
        tmp = endpoint
        while db.query(Post).filter_by(endpoint=tmp).first():
            tmp = endpoint + "-" + str(random.randint(10, 99))

        excerpt = str(escape(" ".join(body.split()[:30])))

        post = Post(title=title, body=body, excerpt=excerpt, endpoint=tmp, is_draft=is_draft)
        post.author = g.user
        db.add(post)
        db.commit()

    return {"status": "success", "message": "Post created successfully"}, 200
