#shortseq shortening method (Documented in README.md - Strategy 2)
import hashlib

from emojikeygen import config

from emojikeygen.shorteners import alphabet
from emojikeygen.shorteners import util

def generate(index):
    """Generates emoji sequence and private key"""
    index_sequence = util.list_to_emoji_string(util.int_to_list(index, shorten_base = False))
    return index_sequence, generate_key(index_sequence)

def generate_key(emojikey):
    """Generates key when given emojikey. Used by generate function, but can also be used to decode any given emojikey"""
    peppered_emojikey = emojikey + config.PEPPER
    hash = hashlib.sha256()
    hash.update(peppered_emojikey.encode('utf-8'))
    return hash.hexdigest()
