from flask import Blueprint
from flask_restful import Api

bp = Blueprint("gram_book", __name__, url_prefix="")
api_basic = Api(bp)

from server.view.auth import Login
api_basic.add_resource(Login, "/login")

from server.view.auth import SigUp
api_basic.add_resource(SigUp, "/signup")

from server.view.post import Post
api_basic.add_resource(Post, "/post")

from server.view.post import GetPost
api_basic.add_resource(GetPost, "/post")

from server.view.post import DeletePost
api_basic.add_resource(DeletePost, "/post/<int:id>")

from server.view.post import UpdatePost
api_basic.add_resource(UpdatePost, "/post/<int:id>")

from server.view.poto import Upload
api_basic.add_resource(Upload, "/poto")

from server.view.poto import Download
api_basic.add_resource(Download, "/poto")

from server.view.favorites import Favorites
api_basic.add_resource(Favorites, "/Favorites/<int:id>")


