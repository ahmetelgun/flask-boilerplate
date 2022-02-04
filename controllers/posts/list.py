from flask import request, make_response, jsonify

from models import DBContext, Post
from settings import PAGINATION_SIZE


def list(args):
    page = args.get("page", default=1, type=int)
    if int(page) < 1:
        page = 1

    start_index = (page-1)*PAGINATION_SIZE
    end_index = (page*PAGINATION_SIZE)

    with DBContext() as db:
        posts = db.query(Post).filter_by(
            is_draft=False, is_deleted=False)[start_index: end_index]

        post_list = []

        for post in posts:
            post_list.append({
                "id": post.id,
                "title": post.title,
                "excerpt": post.excerpt,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
                "endpoint": post.endpoint,
                "author_id": post.author_id,
                "author_firstname": post.author.firstname,
                "author_lastname": post.author.lastname,
            })

    return make_response(jsonify(post_list), 200)
