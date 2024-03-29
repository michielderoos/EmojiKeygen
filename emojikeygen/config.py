# *** Demo Config --  NOT for production use **  

SQLALCHEMY_TRACK_MODIFICATIONS = False
# Just using a basic sqlite database in PWD for local demonstration
SQLALCHEMY_DATABASE_URI = "sqlite:///myproject.sqlite3"
PEPPER = 'This is a super secret string'
DATABASE_ENCRYPTION_KEY = 'This string is the most secret of them all!'
DEFAULT_RANDOM_SEQUENCE_LENGTH = 5
MARKOV_CORPUS_URL = "http://www.gutenberg.org/cache/epub/345/pg345.txt" #dracula.txt