from flask_restful import Resource
from flask import request

from flask_jwt_extended import get_jwt_identity, jwt_required

from contorller.post import post_get, post_delete, post_update, post


class Post(Resource):
    @jwt_required()
    def post(self):
        title = request.json['title']
        content = request.json['content']
        inherence = request.json['inherence']
        nick = get_jwt_identity()
        return post(
            title=title,
            content=content,
            inherence=inherence,
            nick=nick
        )


class GetPost(Resource):
    @jwt_required()
    def get(self):

        inherence = request.json['inherence']

        return post_get(
            inherence=inherence
        )


class DeletePost(Resource):
    @jwt_required()
    def delete(self, id):
        token = get_jwt_identity()
        return post_delete(
            token=token,
            id=id
        )


class UpdatePost(Resource):
    @jwt_required()
    def patch(self, id):
        title = request.json["title"]
        content = request.json["content"]
        token = get_jwt_identity()
        return post_update(
            id=id,
            title=title,
            content=content,
            token=token
        )
