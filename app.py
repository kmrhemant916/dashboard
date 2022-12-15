from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root1234@172.28.0.2:3306/events"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
db.init_app(app)

class GitlabEvents(db.Model):
    __tablename__ = 'gitlab_hooks'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    repository_name = db.Column(db.String(100), nullable=False)

@app.post("/gitlab/events")
def create_gitlab_events():
    request_data = request.get_json()
    event = GitlabEvents(user_id=request_data["user_id"], user_name=request_data["user_name"], repository_name=request_data["repository"]["name"])
    db.session.add(event)
    db.session.commit()
    return {"event": request_data}, 201

@app.get("/gitlab/events")
def get_gitlab_events():
    print("h")
    response = []
    for i in GitlabEvents.query.all():
        elem = {"user_name": i.user_name, "repository_name": i.repository_name}
        response.append(elem)
    return {"events": response}, 200

with app.app_context():
    db.create_all()