from flask_restful import Resource, reqparse
from models.questions import QuestionModel


class CRUDquestions(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("questions", type=dict, help="questions go here")

    def post(self, test_id):

        data = self.parser.parse_args()

        for key in data['questions'].keys():
            question = QuestionModel(ru_words=data['questions'][key][0], kg_words=data['questions'][key][1],
                                     test_id=test_id)
            question.save_to_db()

    def delete(self, test_id):

        questions = QuestionModel.find_by_id(test_id)

        for question in questions:
            if question:
                question.delete_from_db()
