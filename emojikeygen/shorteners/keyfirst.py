import secrets
import baseconvert
from emojikeygen.shorteners import util

def generate(*argv):
    key = secrets.token_hex(16).upper()
    bc = baseconvert.BaseConverter(input_base=16, output_base=29)
    return util.list_to_emoji_string(bc(key)), key
