from flask import Blueprint, send_from_directory, Response, request, g, jsonify
from config import Config
from passlib.hash import pbkdf2_sha256
import database
import user
import client
import datetime
import jwt
import session
import datetime

routes = Blueprint('routes', __name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = database.connect(Config.DB_NAME)
    return db


def jwt_auth(_request):
    auth = _request.headers.get('Authorization')
    if not auth:
        print('No Authorization header.')
        return False

    try:
        encoded_jwt = auth.split(' ')[1]
    except Exception as e:
        print(e)
        return False
    try:
        decoded_jwt = jwt.decode(encoded_jwt, Config.JWT_SECRET, algorithms=['HS256'])
    except Exception as e:
        print(e)
        return False

    return decoded_jwt


@routes.route('/<path:path>')
def static_files(path):
    return send_from_directory(Config.STATIC_DIR, path)


@routes.route('/user/create', methods=['POST'])
def user_create():
    # TODO: Test and improve.
    data = request.get_json()
    password_hash = pbkdf2_sha256.hash(data.get('password'))
    date = datetime.date.today()

    result = user.create(get_db(), data.get('email'), data.get('username'), password_hash, date)
    if result:
        return Response(status=201)

    return Response(status=400)


@routes.route('/user/login', methods=['POST'])
def user_login():
    data = request.get_json()

    result = user.login(get_db(), data.get('username'), data.get('password'))
    if result:
        # Return JWT with user ID as payload.
        encoded_jwt = jwt.encode(
            {
                'user_id': result,
                'username': data.get('username'),
                # 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100)
            }, Config.JWT_SECRET, algorithm='HS256')
        return Response(encoded_jwt, status=200)

    return Response(status=401)


@routes.route('/user/client', methods=['POST'])
def create_client():
    """Create a new client and create the sessions for the current month, with duration as an empty string."""
    data = request.get_json()

    decoded_jwt = jwt_auth(request)
    if not decoded_jwt:
        return Response(status=401)

    # Create the client.
    result = client.create(get_db(), decoded_jwt.get('user_id'), data.get('name'))
    if result:
        # Create the sessions for the client for the current month.
        row = data.get('row')
        today = datetime.date.today()
        for i, duration in enumerate(row):
            date = datetime.date(today.year, today.month, i + 1)
            session.create(get_db(), result, date, duration)

        return jsonify({'client_id': result, 'name': data.get('name'), 'row': data.get('row')})

    return Response(status=401)


@routes.route('/user/client', methods=['GET'])
def get_clients():
    """Get all the clients for the particular user_id.
    Get all the sessions for the given client_id in the current month."""
    decoded_jwt = jwt_auth(request)
    if not decoded_jwt:
        return Response(status=401)

    result = client.get_all(get_db(), decoded_jwt.get('user_id'))
    return jsonify(result)


@routes.route('/user/client/<int:client>', methods=['PUT'])
def update_client():
    return 'hello'


@routes.route('/')
def index():
    return 'index.html'