import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint("gitlab", __name__, description="Operations on users")

@blp.route("/gitlab/events")
class Store(MethodView):
    def get(self, store_id):
        pass

    def delete(self, store_id):
        pass