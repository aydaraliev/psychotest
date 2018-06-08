from flask_restful import Resource, reqparse
from models.tests import TestModel


class Test(Resource):

    def get(self, id):
        test = TestModel.find_by_id(id)
        if test:
            return test.json()
        return {'message': 'Test not found'}, 404


class CRUDTest(Resource):

    def post(self, name):
        if TestModel.find_by_name(name):
            return {'message': "A test with name '{}' already exists.".format(name)}, 400

        test = TestModel(name)
        try:
            test.save_to_db()
        except:
            return {"message": "An error occurred creating the test."}, 500

        return test.json(), 201

    def delete(self, name):
        test = TestModel.find_by_name(name)
        if test:
            test.delete_from_db()

        return {'message': 'Test deleted'}