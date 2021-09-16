from flask import jsonify

from models import Post, DBContext, User


def posts_index():
    posts = get_posts()

    return jsonify({
        "status": "success",
        "posts": posts
    }), 200


def get_posts():
    with DBContext() as db:
        posts = db.query(Post.title, Post.excerpt, Post.created_date, Post.updated_date,
                         Post.author_id).filter_by(is_draft=False, is_deleted=False).all()

        for index, post in enumerate(posts):
            posts[index] = dict(post)
            posts[index]['author'] = db.query(User).filter_by(
                id=post.author_id).first().get_user()

    return posts
