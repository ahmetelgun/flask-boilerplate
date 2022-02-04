from datetime import datetime
from flask import request, make_response, jsonify
import html

from models import DBContext, Post
from service import create_endpoint


def detail(endpoint):
    with DBContext() as db:
        post = db.query(Post).filter_by(endpoint=endpoint).first()
        author_firstname = post.author.firstname
        author_lastname = post.author.lastname

    if not post or post.is_deleted or post.is_draft:
        return make_response(jsonify(
            {"message": "Post not found"}
        ), 404)

    post_detail = {
        "id": post.id,
        "title": post.title,
        "text": post.text,
        "created_at": post.created_at,
        "updated_at": post.updated_at,
        "endpoint": post.endpoint,
        "author_id": post.author_id,
        "author_firstname": author_firstname,
        "author_lastname": author_lastname,
    }

    return make_response(jsonify(post_detail), 200)
