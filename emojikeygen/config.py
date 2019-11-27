# *** Demo Config --  NOT for production use **  

SQLALCHEMY_TRACK_MODIFICATIONS = False
# Just using a basic sqlite database in PWD for local demonstration with no extra fuss
SQLALCHEMY_DATABASE_URI = "sqlite:///myproject.sqlite3"
PEPPER = 'This is a super secret string'
DEFAULT_RANDOM_SEQUENCE_LENGTH = 5