import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import gitlab_events
from schemas import  GitlabPushEventSchema


blp = Blueprint("GitLab", __name__, description="Operations on gitlab events")
@blp.route("/gitlab/events")
class Gitlab(MethodView):
    def get(self):
        pass

    @blp.arguments( GitlabPushEventSchema)
    @blp.response(201,  GitlabPushEventSchema)
    def post(self, events_data):
        print("hiu")
        print(events_data)
        pass
        # gitlab_events.append(events_data)
        # return {"gitlab_events": gitlab_events}