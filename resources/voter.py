from flask_restful import Resource, reqparse
from models.voters import VoterModel
from models.searchvoters import SearchVoterModel


class Voter(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("firstname", type=str, required=True, help="First name")
    parser.add_argument("lastname", type=str, required=True, help="Last name")
    parser.add_argument('birthday', type=str, required=True, help="Birthday")
    parser.add_argument('uuid4', type=str, required=True, help="uuid4 key here")

    def post(self):
        data = self.parser.parse_args()
        bday = data['birthday']
        bday = '.'.join(bday.split('-')[::-1])
        fname = data["firstname"].strip().upper()
        lname = data["lastname"].strip().upper()

        if lname.endswith("УУЛУ"):
            lname = lname.split()
            lname = ' '.join(lname[::-1])
        elif lname.endswith("КЫЗЫ"):
            lname = lname.split()
            lname = ' '.join(lname[::-1])

        save_search = SearchVoterModel(data['uuid4'], bday, fname, lname.upper())
        save_search.save_to_db()

        return {"matches": [voter.json() for voter in
                            VoterModel.find_voter(fname, lname, bday)]}