from flask_restful import Resource, reqparse
from models.users import UserModel
from misc import send_email


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("results", type=dict, help="results go here")
    parser.add_argument("user", type=dict, help="user details go here")

    def post(self):
        data = self.parser.parse_args()

        data['user']['responses'] = str(data['user']['responses'])
        user = UserModel(**data['results'], **data['user'])
        user.save_to_db()
        user_results = user.calculate_results()

        if data['user']['sendEmail'] == True:
            send_email.send_email('aidaraliev@gmail.com', 'password_here',
                                  'archer1strong@gmail.com',
                                  'Результаты теста на определение личностных качеств', user_results)

        return {"response": user_results}
