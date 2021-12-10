from flask import redirect
from flask_swagger_ui import get_swaggerui_blueprint
import jwt
from functools import wraps
from flask import Flask, jsonify, make_response,request
import datetime
from hotel_data import location


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Missing token'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print('===============')
            print(data)
            print('============')
        except:
            return jsonify({'message': 'Invalid token'}), 403
        return func(*args, **kwargs)

    return wrapped


@app.route('/')
def login():
    auth = request.authorization
    if auth and auth.password == '1234':
        token = jwt.encode({'user':auth.username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=5)}
                          , app.config['SECRET_KEY'])

        return jsonify({'token': token})
    return make_response('could not varify!', 401, {'WWW-Authenticate': 'Basic realm=Login Required'})


@app.route('/pro')
@check_for_token
def protected():
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    return redirect("http://127.0.0.1:5000/swagger", code=302)


@app.route('/un', methods=['GET'])
def un():
    # print(Price)
    Title = request.args.get('Title')
    Sleeps = request.args.get('Sleeps')
    Bedroom = request.args.get('Bedroom')
    Bathroom = request.args.get('Bathroom')
    Price = request.args.get('Price')
    Location = request.args.get('Location')

    length = 0
    if Title is not None:
        length = length + 1
    if Sleeps is not None:
        length = length + 1
    if Bedroom is not None:
        length = length + 1
    if Bathroom is not None:
        length = length + 1
    if Price is not None:
        length = length + 1
    if Location is not None:
        length = length + 1
    data = location(Location, Price, length, Bedroom, Bathroom, Sleeps, Title)
    return data


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
