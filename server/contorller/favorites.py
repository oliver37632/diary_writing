from server.model import session_scope
from server.model.post import Post


def favorites(id, token):
    with session_scope() as session:
        post = session.query(Post).filter(Post.id_pk == id).first()

        if post:
            post = session.query(Post).filter(Post.user_nick == token).first()
            if post:
                if post.Favorites == 1:
                    post.Favorites = 0
                    return {
                        "message": "Favorites False"
                    }, 200
                else:
                    post.Favorites = 1
                    return {
                        "message": "Favorites True"
                    }, 200
            return {
                "msg": "not nick match"
            }, 404
        return {
                   "msg": "not id match"
               }, 404