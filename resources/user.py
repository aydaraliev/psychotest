from flask_restful import Resource, reqparse
from models.users import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("results", type=dict, help="results go here")
    parser.add_argument("user", type=dict, help="user details go here")

    def post(self):
        data = self.parser.parse_args()
        user = UserModel(**data['results'], **data['user'])
        user.save_to_db()
        return {"response": user.calculate_results()}
