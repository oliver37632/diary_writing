from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.contorller.favorites import favorites


class Favorites(Resource):
    @jwt_required()
    def post(self, id):
        token = get_jwt_identity()
        return favorites(
            id=id,
            token=token
        )