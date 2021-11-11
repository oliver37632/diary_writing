from model import session_scope
from model.post import Post
from model.user import User


from datetime import datetime

from flask import abort


def post(title, content, inherence, nick):
    with session_scope() as session:

        new_post = Post(
            title=title,
            content=content,
            inherence=inherence,
            created_at=datetime.now(),
            Favorites=False,
            user_nick=nick
        )

        session.add(new_post)
        session.commit()

        return {
            "message": "success"
        }, 201


def post_get(inherence):
    with session_scope() as session:
        posts = session.query(
            Post.id_pk,
            Post.title,
            Post.content,
            Post.created_at,
            Post.inherence,
            User.nick
        ).join(User, User.nick == Post.user_nick).filter(Post.inherence == inherence)

        if posts:
            return {
                       "posts": [{
                           "id_pk": id_pk,
                           "inherence": inherence,
                           "title": title,
                           "content": content,
                           "created_at": str(created_at),
                           "nick": nick
                       } for id_pk, title, content, created_at, inherence, nick in posts]
                   }, 200

        return abort("Not Found", 404)


def post_delete(id, token):
    with session_scope() as session:
        post_del = session.query(Post).filter(Post.user_nick == token, Post.id_pk == id).first()

        if post_del:
            session.delete(post_del)
            session.commit()
            return {
                       "message": "success"
                   }, 200
        return {
                   "massage": "NotFound"
               }, 404


def post_update(id, title, content, token):
    with session_scope() as session:
        post = session.query(Post).filter(Post.id_pk == id, Post.user_nick == token).first()

        if post:
            post.title = title
            post.content = content

            return {
                       "msg": "success"
                   },200

        return {
            'message': 'Error'
        }, 404