# *** Demo Config --  NOT for production use **  

SQLALCHEMY_TRACK_MODIFICATIONS = False
# Just using a basic sqlite database in PWD for local demonstration
SQLALCHEMY_DATABASE_URI = "sqlite:///myproject.sqlite3"
PEPPER = 'This is a super secret string'
DATABASE_ENCRYPTION_PASSWORD = 'This string is the most secret of them all!'
DEFAULT_RANDOM_SEQUENCE_LENGTH = 5