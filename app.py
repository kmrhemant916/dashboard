from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
import uuid
from functools import wraps
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root1234@localhost:3306/dashboard"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'admin'

db = SQLAlchemy(app)
db.init_app(app)

class GitlabEvents(db.Model):
    __tablename__ = 'gitlab_hooks'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    repository_name = db.Column(db.String(100), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(100), primary_key = True)
    password = db.Column(db.String(100))

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-Access-Token' in request.headers:
            token = request.headers['x-Access-Token']
            print(token)
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            print("kjnfejkrnjfn")
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print(data)
            print("mngrjerngjknerjgtnjertngjhnegrj")
            current_user = User.query.filter_by(name = data['username']).first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated

# route for logging user in
@app.route('/login', methods =['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )

    user = User.query\
        .filter_by(name = auth.get('username'))\
        .first()

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'username': auth.get('username'),
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'])
        return make_response(jsonify({'token' : token}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )

@app.route('/signup', methods =['POST'])
def signup():
    data = request.get_json()
    name, password = data.get('username'), data.get('password')
    user = User.query.filter_by(name = name).first()
    if not user:
        user = User(
            name = name,
            password = generate_password_hash(password, method='pbkdf2:sha1', salt_length=4)
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "Successfully registered."}, 201
    return {"message": "User already exists. Please Log in."}, 202

@app.post("/gitlab/events")
@token_required
def create_gitlab_events(current_user):
    request_data = request.get_json()
    event = GitlabEvents(user_id=request_data["user_id"], user_name=request_data["user_name"], repository_name=request_data["repository"]["name"])
    db.session.add(event)
    db.session.commit()
    return {"event": request_data}, 201

@app.get("/gitlab/events")
# @token_required
def get_gitlab_events(current_user):
    response = []
    for i in GitlabEvents.query.all():
        elem = {"user_name": i.user_name, "repository_name": i.repository_name}
        response.append(elem)
    return {"events": response}, 200

with app.app_context():
    db.create_all()