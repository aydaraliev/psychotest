from flask_restful import Resource, reqparse
from models.foundORnot import FoundOrNotModel

class FoundOrNot(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("uuid4", type=str, required=True, help="uuid here")
    parser.add_argument("found_presidential", type=bool, required=True, help="found presidential boolean")
    parser.add_argument("found_parliamentary", type=bool, required=True, help="found parliamentary boolean")

    def post(self):
        data = self.parser.parse_args()

        save_found = FoundOrNotModel(data["uuid4"], data["found_presidential"], data["found_parliamentary"])
        save_found.save_to_db()

        return 200