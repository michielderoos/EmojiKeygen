from flask_restful import Resource, reqparse, abort
from sqlalchemy.sql.expression import func
import urllib

from emojikeygen.shorteners import emojihash
from emojikeygen.shorteners import util
from emojikeygen.models import keys, db

class Shorten(Resource):
    def get(self, emojikey):
        # Find the name associated with given emojikey, and return it
        key_row = db.session.query(keys).filter_by(emojikey = emojikey).first()
        if not key_row:
            abort(404, message="Emojikey {} does not exist".format(key_row))
        return {'name': key_row.name}
    def post(self):
        # Gather all the required data to generate and store a new emojikey
        parser = reqparse.RequestParser()
        parser.add_argument('name', required = True, type=str, help='Name of user asking for a token')
        parser.add_argument('strategy', default = 'emojihash',type=str, help='Shortening strategy to use')
        args = parser.parse_args()
        emojikey_index = db.session.query(func.max(keys.id)).scalar() or 0
        # Generate and store emojikey
        emojikey, key = emojihash.generate(emojikey_index)
        key_row = keys(emojikey = emojikey, name = args.name, key = key, strategy = args.strategy)
        db.session.add(key_row)
        db.session.commit()
        return {'emojikey': emojikey}