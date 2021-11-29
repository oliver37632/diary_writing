from flask import request
from flask_restful import Resource
from server.contorller.auth import sigup, login, id_overlap_check
from server.view import validate_JSON
from server.model.post import Post

ㅇ
class SigUp(Resource):
    @validate_JSON(Post)
    def post(self):
        nick = request.json['nick']
        name = request.json['name']
        password = request.json['password']

        return sigup(
                nick=nick,
                name=name,
                password=password
                     )


class Login(Resource):
    @validate_JSON(Post)
    def post(self):
        nick = request.json['nick']
        password = request.json['password']

        return login(
            nick=nick,
            password=password
        )


class Id_Check(Resource):
    @validate_JSON(Post)
    def post(self):
        nick = request.json['nick']

        return id_overlap_check(
            nick=nick
        )