from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from server.contorller.poto import upload, download


class Upload(Resource):
    @jwt_required()
    def post(self):
        name = request.args.get("name")
        inherence = request.args.get("inherence")

        return upload(
            name=name,
            inherence=inherence
        )


class Download(Resource):
    @jwt_required()
    def get(self):
        inherence = request.args.get("inherence")

        return download(
            inherence=inherence
        )