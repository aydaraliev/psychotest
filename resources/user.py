from flask_restful import Resource, reqparse
from models.users import UserModel, VoterModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("characteristics", type =dict, help="characteristcs go here")
    parser.add_argument("name_last_name", type = dict, help = "last_name_first_name")

    def post(self):
        data = self.parser.parse_args()
        user = UserModel(**data['characteristics'])
        voter = VoterModel(**data['name_last_name'])
        voters = VoterModel.find_by_f_l_name(voter.first_name, voter.last_name)
        for v in voters:
            print(v.json())
        user.save_to_db()
