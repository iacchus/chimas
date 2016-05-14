from eve import Eve
from eve.utils import config

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from eve_sqlalchemy.decorators import registerSchema

#from core.users import Users
from core.boards import Base, Boards
#from core.posts import Posts

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
        Column,
        String,
        Integer,
        )

#from eve.utils import config

import os

basedir = os.path.abspath(os.path.dirname(__file__))

#ID_FIELD = 'id'
#ITEM_LOOKUP_FIELD = ID_FIELD
#config.ID_FIELD = ID_FIELD
#config.ITEM_LOOKUP_FIELD = ID_FIELD

#Base = declarative_base()

#class Boards(Base):
#    __tablename__ = 'boards'

#    id = Column(Integer, primary_key=True, autoincrement=True)
#    title = Column(String)
#    description = Column(String)

registerSchema('boards')(Boards)

SETTINGS = {
    'DEBUG':True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(basedir,'dummy.sqlite3'),
    'DOMAIN':
    {
        'boards': Boards._eve_schema['boards']
    },
    'PUBLIC_METHODS': ['GET']
}

app = Eve(auth=None,settings=SETTINGS,validator=ValidatorSQL,data=SQL)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
#db.create_all()

if __name__ == "__main__":

    app.run();
