from core import Boards, Posts, Users

from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))

DEBUG = True

# FIELDS

ID_FIELD            = "id"
ID_FIELD_LOOKUP     = "id"
ITEM_LOOKUP_FIELD   = "id"
ETAG_FIELD          = "etag"
DATE_CREATED        = "created"
LAST_UPDATED        = "updated"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(basedir,'dummy.sqlite3-autocreate')
DOMAIN = {
    'boards' : Boards._eve_schema['boards'],
    'posts'  : Posts._eve_schema['posts'],
    'users'  : Users._eve_schema['users'],
}
PUBLIC_METHODS = ['GET']
