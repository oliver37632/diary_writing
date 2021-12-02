from flask import request
from flask_restful import Resource
from server.contorller.auth import sigup, login, id_overlap_check


class SignUp(Resource):
    def post(self):
        nick = request.json['nick']
        name = request.json['name']
        password = request.json['password']

        return signup(
                nick=nick,
                name=name,
                password=password
                     )


class Login(Resource):
    def post(self):
        nick = request.json['nick']
        password = request.json['password']

        return login(
            nick=nick,
            password=password
        )


class Id_Check(Resource):
    def post(self):
        nick = request.json['nick']

        return id_overlap_check(
            nick=nick
        )