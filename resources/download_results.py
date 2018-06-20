from flask_restful import Resource, reqparse
from flask import send_file
import pandas as pd
from io import BytesIO


from models.users import UserModel
from models.searchvoters import SearchVoterModel
from models.foundORnot import FoundOrNotModel


class FileDownload(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("login", type=str, help="login goes here")
    parser.add_argument("password", type=str, help="password goes here")

    def post(self):
        login = 'psycho_test'
        password = 'psycho_test_auca'

        data = self.parser.parse_args()

        if data['login'] == login and data['password'] == password:
            searches = SearchVoterModel.query.all()
            searches = [search.to_dict() for search in searches]
            users = UserModel.query.all()
            users = [user.to_dict() for user in users]
            found_not_found = FoundOrNotModel.query.all()
            found_not_found = [found.to_dict() for found in found_not_found]

            searches = pd.DataFrame(searches)
            users = pd.DataFrame(users)
            found_not_found = pd.DataFrame(found_not_found)

            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')

            users.to_excel(writer, sheet_name="users", index=False)
            searches.to_excel(writer, sheet_name="searches", index=False)
            found_not_found.to_excel(writer, sheet_name="found_not_found", index=False)

            writer.save()
            output.seek(0)

            writer.close()


            return send_file(output, attachment_filename="data.xlsx", as_attachment=True)
        else:
            return 403