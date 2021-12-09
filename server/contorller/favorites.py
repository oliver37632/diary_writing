from server.model import session_scope
from server.model.post import Post
from server.model.user import User
from flask import abort


def favorites(id, token):
    with session_scope() as session:
        post = session.query(Post).filter(Post.user_nick == token).first()
        if post:
            post = session.query(Post).filter(Post.inherence == id).first()
            if post:
                if post.Favorites == 1:
                    post.Favorites = 0
                    return {
                        "msg": False
                    }, 200
                else:
                    post.Favorites = 1
                    return {
                        "message": True
                    }, 200
            return {
                    "msg": "not id match"
            }, 404
        return {
                   "msg": "not nick match"
               }, 404


def ck_favorites():
    with session_scope() as session:
        posts = session.query(
            Post.id_pk,
            Post.title,
            Post.content,
            Post.url
        ).join(User, User.nick == Post.user_nick).filter(Post.Favorites == 1)

        if posts:
            return {
                       "posts": [{
                           "id_pk": id_pk,
                           "title": title,
                           "content": content,
                           "url": url
                       } for id_pk, title, content, url in posts]
                   }, 200

        return abort("Not Found", 404)


def delete_favorites(id ,token):
    with session_scope() as session:
        post = session.query(User).filter(User.nick == token).first()

        if not post:
            return {
                       "message": "user id not match"
                   }, 400

        post = session.query(Post).filter(Post.inherence == id).first()

        if not post:
            return {
                "message": "Not Fuond"
            }, 404

        if post.Favorites == 1:
            post.Favorites = 0

        return {
            "message": "success"
        }, 200

        return {"message": "error"}, 400