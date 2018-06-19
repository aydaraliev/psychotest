import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.test import TestModel, Test, CRUDTest
from resources.question import QuestionModel, CRUDquestions
from resources.user import UserModel, User
from models.interpretation import InterpretationModel
from resources.voter import Voter, VoterModel, SearchVoterModel
from resources.foundOrNotEP import FoundOrNot, FoundOrNotModel
from resources.download_results import FileDownload

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'rust4m'



# CRUD
api.add_resource(CRUDTest, '/CRUD/tests/<string:name>')
api.add_resource(CRUDquestions, '/CRUD/questions/<int:test_id>')

# front api
api.add_resource(Test, '/tests/<int:id>')
api.add_resource(User, '/tests/results')
api.add_resource(Voter, '/tests/voter')
api.add_resource(FoundOrNot, '/tests/found_not_found')
api.add_resource(FileDownload, '/tests/cbac5cc3-d1d4-4390-94e8-5541e083630b')

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)

