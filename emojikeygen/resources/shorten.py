from flask_restful import Resource, reqparse, abort
from sqlalchemy.sql.expression import func

from emojikeygen.shorteners import emojihash, shortseq, markov, keyfirst
from emojikeygen.models import keys, db

# Strategies we want to make available through the API
strategies = {'emojihash': emojihash, 'shortseq': shortseq, 'dracula': markov, 'keyfirst': keyfirst}

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
        # Get current index and desired strategy
        emojikey_index = db.session.query(func.max(keys.id)).scalar() or 0
        if args.strategy not in strategies:
            abort(400, message="Invalid Strategy: Strategy {} does not exist".format(args.strategy))
        strategy = strategies[args.strategy]
        # Generate and store emojikey
        emojikey, key = strategy.generate(emojikey_index)
        key_row = keys(emojikey = emojikey, name = args.name, key = key, strategy = args.strategy)
        db.session.add(key_row)
        db.session.commit()
        return {'emojikey': emojikey}