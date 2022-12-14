from flask import Flask, request

app = Flask(__name__)

events = {}
count = 0

@app.post("/gitlab/events")
def create_gitlab_events():
    request_data = request.get_json()
    if request_data["user_id"] not in events:
        events[request_data["user_id"]] = {"user_name": request_data["user_name"], "repository_name": request_data["repository"]["name"], "count": 0}
    else:
        events[request_data["user_id"]]["count"] += 1
    # print(request.headers)
    return {"event": request_data}, 201

@app.get("/gitlab/events")
def get_gitlab_events():
    return {"events": events}, 200