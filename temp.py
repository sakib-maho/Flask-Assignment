from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, jsonify, render_template, send_from_directory
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

app = Flask(__name__, template_folder='swagger/templates')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


spec = APISpec(
    title='flask-api-swagger-doc',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)


@app.route('/api/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())


class TodoResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    status = fields.Boolean()


class TodoListResponseSchema(Schema):
    todo_list = fields.List(fields.Nested(TodoResponseSchema))
    todos_list = fields.List(fields.Nested(TodoResponseSchema))


@app.route('/todo')
def todo():
    """Get list of todo
        ---
        get:
            description: get list of Todos
            responses:
                200:
                    description: Return a todo list
                    content:
                        application/json:
                            schema: TodoListResponseSchema

    """

    dummy_data = [{
        'id': 1,
        'task': 'One',
        'status': False
    },
        {
            'id': 2,
            'task': 'Two',
            'status': True
        }
    ]

    return TodoListResponseSchema().dump({'todo_list': dummy_data})


with app.test_request_context():
    spec.path(view=todo)




@app.route('/todos')
def todos():
    """Get list of todos
        ---
        get:
            description: get list of Todos
            responses:
                200:
                    description: Return a todos list
                    content:
                        application/json:
                            schema: TodoListResponseSchema

    """

    dummy_data = [{
        'id': 4,
        'task': 'One',
        'status': False
    },
        {
            'id': 434,
            'task': 'Two',
            'status': True
        }
    ]

    return TodoListResponseSchema().dump({'todos_list': dummy_data})


with app.test_request_context():
    spec.path(view=todos)





@app.route('/docs')
@app.route('/docs/<path:path>')
def swagger_docs(path=None):
    if not path or path == 'index.html':
        return render_template('index.html', base_url='/docs')
    else:
        return send_from_directory('./swagger/static', path)


if __name__ == '__main__':
    app.run(debug=True)
