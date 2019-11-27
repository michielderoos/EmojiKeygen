import os

SQLALCHEMY_TRACK_MODIFICATIONS = False
# Just using a basic sqlite database in PWD for local demonstration with no extra fuss
SQLALCHEMY_DATABASE_URI = "sqlite:///myproject.sqlite3"

