from server.model.S3 import s3_connection, s3_put_object
from server.model import session_scope
from server.model.post import Post

from server.config import AWS_S3_BUCKET_NAME

from flask import request, abort

s3 = s3_connection()


def upload(name, inherence):
    with session_scope() as session:
        f = request.files['file']
        f.save("./temp")
        ret = s3_put_object(s3, AWS_S3_BUCKET_NAME, "./temp", name)
        if ret:

            location = s3.get_bucket_location(Bucket=AWS_S3_BUCKET_NAME)['LocationConstraint']
            image_url = f'https://{AWS_S3_BUCKET_NAME}.s3.{location}.amazonaws.com/{name}'

            post = session.query(Post).filter(Post.inherence == inherence).first()

            if post:
                post.url = image_url
                return {
                           "message": "success"
                       }, 201
            else:
                return abort(404, "Not Found")

        return {
                   "message": "Error"
               }, 400


def download(inherence):
    with session_scope() as session:
        post = session.query(Post).filter(Post.inherence == inherence).first()

        if post:
            post = post.url

            return {
                "url": post
            }, 200
        return {
            "msg": "Not Found"
        }, 404

