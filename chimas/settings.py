from core import Boards, Posts, Users

from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))

DEBUG = True

# FIELDS

ID_FIELD            = "id"
ITEM_LOOKUP_FIELD   = "id"
ETAG                = "etag"
DATE_CREATED        = "created"
LAST_UPDATED        = "updated"
DELETED             = "deleted"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(basedir,'dummy.sqlite3-autocreate')



DOMAIN = {
    'boards' : Boards._eve_schema['boards'],
    'posts'  : Posts._eve_schema['posts'],
    'users'  : Users._eve_schema['users'],
}

DOMAIN['users'].update({
    'resource_methods' : [ 'GET', 'POST', 'DELETE' ]
})


#RESOURCE METHODS = ['GET']
PUBLIC_METHODS = ['GET','POST']
ITEM_METHODS = ['GET']
#PUBLIC_ITEM_METHODS = []

import pprint
pprint.pprint(Users._eve_schema['users'], width=1)
