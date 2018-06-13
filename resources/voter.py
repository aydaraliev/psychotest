from flask_restful import Resource, reqparse
from models.voters import VoterModel


class Voter(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("firstname", type=str, required=True, help="First name")
    parser.add_argument("lastname", type=str, help="Last name")

    def post(self):
        data = self.parser.parse_args()
        return {"matches": [voter.json() for voter in
                            VoterModel.find_voter(data["firstname"].upper(), data["lastname"].upper())]}