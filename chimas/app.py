from eve import Eve
from eve.utils import config

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from eve_sqlalchemy.decorators import registerSchema

from core import Base as Base

from core.users import Users
from core.boards import Boards
from core.posts import Posts

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
        Column,
        String,
        Integer,
        )

#import settings
#from eve.utils import config

#import os

#basedir = os.path.abspath(os.path.dirname(__file__))

#registerSchema('posts')(Posts)
#registerSchema('users')(Users)

#SETTINGS = {
#    'DEBUG':True,
#    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(basedir,'dummy.sqlite3-autocreate'),
#    'DOMAIN':
#    {
#        'boards': Boards._eve_schema['boards'],
#        'posts': Posts._eve_schema['posts'],
#        'users': Users._eve_schema['users'],
#    },
#    'PUBLIC_METHODS': ['GET']
#}

#app = Eve(auth=None,settings=SETTINGS,validator=ValidatorSQL,data=SQL)
app = Eve(auth=None,validator=ValidatorSQL,data=SQL)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

if __name__ == "__main__":

    app.run();
