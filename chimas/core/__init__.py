from sqlalchemy.ext.declarative import declarative_base
from eve_sqlalchemy.decorators import registerSchema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

from .schemas.boards import boards_schema
from .schemas.posts import posts_schema
from .schemas.users import users_schema

from eve.utils import config # FIXME
config.ID_FIELD = 'id'
#config.LAST_UPDATED = 'updated'

Base = declarative_base()

def get_class_by_tablename(table_fullname):
  for c in Base._decl_class_registry.values():
    if hasattr(c, '__table__') and c.__table__.fullname == table_fullname:
      return c

class CommonTable(Base):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default = func.now())
    updated = Column(DateTime, default = func.now(), onupdate = func.now())
    etag = Column(String)
    deleted = Column(String)

    def do_method(preorpost_prefix, resource, request, lookup):

        method = request.method.lower()
        table = get_class_by_tablename(resource)

        if table != None:
            print("table {0} found!\n".format(table.__tablename__))
            try :
                print("We're 'try'ing the method")
                methodCall = getattr(table, preorpost_prefix + method)
                return methodCall(resource, request, lookup)
            except:
                pass

            print("Passed executing method")

    def do_pre_method(resource, request, lookup=None):
        __class__.do_method('pre_', resource, request, lookup)

    def do_post_method(resource, request, payload=None):
        __class__.do_method('post_', resource, request, payload)

class Boards(CommonTable):
    __tablename__ = 'boards'

    title = Column(String)
    description = Column(String)

class Posts(CommonTable):
    __tablename__ = 'posts'

    topic_id = Column(Integer)
    reply_to_id = Column(Integer)
    board_id = Column(String)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)

#users_schema = {
#    'resource_methods' : [ 'GET', 'POST' ],
#    'item_methods' : [ 'GET', 'DELETE' ]
#}

class Users(CommonTable):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, unique=True)
    login = Column(String, primary_key=True, unique=True)
    email = Column(String)
    password = Column(String)

    def pre_get(res,req,lookup):
        print("res: {0} - req: {1} - lookup: {2}\n".format(res,req,lookup))

    def pre_post(res,req,lookup):
        print("We're inside the pre_post method.")

    def post_post(res,req,payload):
        print("We're inside the post_post method.")
        print(payload)

class Roles(CommonTable):
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, unique=True)
    title = Column(String, primary_key=True, unique=True)
    users = Column(String)

registerSchema('boards')(Boards)
registerSchema('posts')(Posts)
registerSchema('users')(Users)
Boards._eve_schema['boards'].update(boards_schema)
Posts._eve_schema['posts'].update(posts_schema)
Users._eve_schema['users'].update(users_schema)
