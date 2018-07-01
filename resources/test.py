from flask_restful import Resource, reqparse
from models.tests import TestModel


class Test(Resource):

    def get(self, id):
        test = TestModel.find_by_id(id)
        if test:
            return test.json()
        return {'message': 'Test not found'}, 404