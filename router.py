from flask import Blueprint
from flask_restful import Api

bp = Blueprint("gram_book", __name__, url_prefix="")
api_basic = Api(bp)

from view.auth import Login
api_basic.add_resource(Login, "/login")

from view.auth import SigUp
api_basic.add_resource(SigUp, "/signup")

from view.post import Post
api_basic.add_resource(Post, "/post")

from view.post import GetPost
api_basic.add_resource(GetPost, "/post")

from view.post import DeletePost
api_basic.add_resource(DeletePost, "/post/<int:id>")

from view.post import UpdatePost
api_basic.add_resource(UpdatePost, "/post/<int:id>")

from view.poto import Upload
api_basic.add_resource(Upload, "/poto")

from view.poto import Download
api_basic.add_resource(Download, "/poto")

from view.favorites import Favorites
api_basic.add_resource(Favorites, "/Favorites/<int:id>")


