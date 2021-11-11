from flask import request
from flask_restful import Resource
from server.contorller.auth import sigup, login


class SigUp(Resource):
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
    def post(self):
        nick = request.json['nick']
        password = request.json['password']

        return login(
            nick=nick,
            password=password
        )