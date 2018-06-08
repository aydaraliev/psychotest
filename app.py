import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.test import Test, CRUDTest
from resources.question import CRUDquestions
from resources.user import User

app = Flask(__name__)
CORS(app)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'rust4m'


@app.before_first_request
def create_tables():
    db.create_all()


# CRUD
api.add_resource(CRUDTest, '/CRUD/tests/<string:name>')
api.add_resource(CRUDquestions, '/CRUD/questions/<int:test_id>')

# front api
api.add_resource(Test, '/tests/<int:id>')
api.add_resource(User, '/tests/results')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
