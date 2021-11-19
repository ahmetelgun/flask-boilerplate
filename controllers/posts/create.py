from datetime import datetime
from flask import request, make_response, jsonify
import html

from models import DBContext, Post
from service import create_endpoint


def create(user):
    try:
        print(request)
        data = request.json
        title = data['title']
        text = data['text']
        is_deleted = data['is_deleted']
        is_draft = data['is_draft']

        if len(title) == 0 or len(text) == 0:
            raise Exception
    except:
        return make_response(jsonify(
            {"message": "Bad request"}
        ), 400)

    endpoint = create_endpoint(datetime.utcnow(), title)
    if not endpoint:
        return make_response(jsonify(
            {"message": "Bad request"}
        ), 400)

    excerpt = " ".join(text.split()[:30])

    post_data = title, text, endpoint, excerpt, is_draft, is_deleted
    save_post(user, post_data)

    return make_response(jsonify(
        {"message": "Post created"}
    ), 200)


def save_post(user, post_data):
    title, text, endpoint, excerpt, is_draft, is_deleted = post_data
    post = Post(title=title, text=text, endpoint=endpoint, excerpt=excerpt, is_draft=is_draft, is_deleted=is_deleted, created_at=datetime.utcnow())
    with DBContext() as db:
        endpoint = post.endpoint
        count = 1
        while db.query(Post).filter_by(endpoint=endpoint).first():
            endpoint = f"{post.endpoint}-{count}"
            count += 1

        post.endpoint = endpoint
        post.author = user
        db.add(post)
        db.commit()

    return True
