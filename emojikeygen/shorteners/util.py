## Utility functions for shortening functions
import random
import hashlib
import baseconvert

from emojikeygen import config
from emojikeygen.shorteners import alphabet

def generate_random_list(length):
    """ Generates list of n random values between 0 and len(alphabet) (e.g. 3 => [4, 22, 21])"""
    return [random.randint(0, alphabet.length-1) for i in range(length)]

def int_to_list(i, shorten_base = False):
    """
    Converts integer to emoji-indexed list (e.g. 1500 => [1, 22, 21])
    Also supports shortened base, if we want to create a reserve sentinel character (See README.md for more on this)
    """
    base = alphabet.length if not shorten_base else alphabet.length - 1
    return list(baseconvert.base(i, 10, base))

def list_to_emoji_string(a):
    """ Converts list of base29 to emoji string (e.g. [1, 22, 21] => '🦊🦘🐙') """
    return ''.join(alphabet.alphabet[i] for i in a)

def convert_emoji_string_to_list(es):
    """ Converts list of base29 to emoji string (e.g. '🦊🦘🐙' => [1, 22, 21]) """
    return list(map(lambda char: alphabet.alphabet.index(char), es))

def generate_key(emojikey, pepper = config.PEPPER):
    """Generates key when given emojikey. Used by generate function, but can also be used to decode any given emojikey"""
    peppered_emojikey = emojikey + pepper
    hash = hashlib.sha256()
    hash.update(peppered_emojikey.encode('utf-8'))
    return hash.hexdigest()

