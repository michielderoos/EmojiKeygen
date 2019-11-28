#emojihash shortening method (Documented in README.md - Strategy 1)
import hashlib
import sys

from emojikeygen import config

from emojikeygen.shorteners import alphabet
from emojikeygen.shorteners import util

def generate(index, random_sequence_length = config.DEFAULT_RANDOM_SEQUENCE_LENGTH):
    """Generates emoji sequence and private key"""
    index_sequence = util.int_to_list(index, shorten_base = True)
    random_sequence = util.generate_random_list(random_sequence_length)
    emojikey = util.list_to_emoji_string(index_sequence) + alphabet.sentinel + util.list_to_emoji_string(random_sequence)
    return emojikey, generate_key(emojikey)

def generate_key(emojikey):
    """Generates key when given emojikey. Used by generate function, but can also be used to decode any given emojikey"""
    peppered_emojikey = emojikey + config.PEPPER
    hash = hashlib.sha256()
    hash.update(peppered_emojikey.encode('utf-8'))
    return hash.hexdigest()

