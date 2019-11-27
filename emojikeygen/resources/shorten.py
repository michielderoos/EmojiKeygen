from flask_restful import Resource, reqparse

from emojikeygen.shorteners import emojihash

class Shorten(Resource):
    def get(self, emojikey):
        return {'a': 'b'}
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True, type=str, help='Name of user asking for a token')
        parser.add_argument('strategy', default = 'emojihash',type=str, help='Shortening strategy to use')
        args = parser.parse_args()
        print(args)
        return emojihash.generate(1)
