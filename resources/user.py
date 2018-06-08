from flask_restful import Resource, reqparse
from models.users import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("characteristics", type=dict, help="characteristcs go here")

    def post(self):
        data = self.parser.parse_args()
        user = UserModel(**data['characteristics'])
        user.save_to_db()
