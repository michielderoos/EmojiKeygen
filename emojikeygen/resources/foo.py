from flask_restful import Resource

class Foo(Resource):
    def get(self):
        return {'a': 'b'}
    def post(self):
        return {'a': 'b'}
