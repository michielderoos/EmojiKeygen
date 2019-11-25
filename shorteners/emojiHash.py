#emojiHash shortening method (Documented in README.md - Strategy 1)
import hashlib
import sys

sys.path.append('..')
import alphabet
import config
import util

def generate(index, random_sequence_length = config.default_random_sequence_length):
    """Generates emoji sequence and private key"""
    index_sequence = util.int_to_list(index, shorten_base = True)
    random_sequence = util.generate_random_list(random_sequence_length)
    emoji_sequence = util.list_to_emoji_string(index_sequence) + alphabet.sentinel + util.list_to_emoji_string(random_sequence)
    return {'emoji_sequence': emoji_sequence, 'private_key': generate_key(emoji_sequence)}

def generate_key(emoji_sequence):
    """Generates key when given emoji sequence. Used by generate function, but can also be used to decode any given emoji sequence"""
    peppered_emoji_sequence = emoji_sequence + config.pepper
    hash = hashlib.sha256()
    hash.update(peppered_emoji_sequence.encode('utf-8'))
    return hash.hexdigest()

