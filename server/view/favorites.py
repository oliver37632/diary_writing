from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.contorller.favorites import favorites, ck_favorites, delete_favorites
from server.view import validate_JSON
from server.model.post import Post


class Favorites(Resource):
    @jwt_required()
    def post(self, id):
        token = get_jwt_identity()
        return favorites(
            id=id,
            token=token
        )


class CkFavorites(Resource):
    def get(self):
        return ck_favorites()


class DeleteFavorites(Resource):
    def delete(self, id):
        token = get_jwt_identity()
        return delete_favorites(
            id=id,
            token=token
        )