#shortseq shortening method (Documented in README.md - Strategy 2)
from emojikeygen import config
from emojikeygen.shorteners import alphabet
from emojikeygen.shorteners import util

def generate(index):
    """Generates emoji sequence and private key"""
    index_sequence = util.list_to_emoji_string(util.int_to_list(index, shorten_base = False))
    return index_sequence, util.generate_key(index_sequence)
