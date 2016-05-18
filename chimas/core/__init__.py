from sqlalchemy.ext.declarative import declarative_base
from eve_sqlalchemy.decorators import registerSchema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

from eve.utils import config # FIXME
config.ID_FIELD = 'id'

Base = declarative_base()

def get_class_by_tablename(table_fullname):
  for c in Base._decl_class_registry.values():
    if hasattr(c, '__table__') and c.__table__.fullname == table_fullname:
      return c

class CommonTable(Base):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(String, default = func.now())
    updated = Column(String, default = func.now(), onupdate = func.now())
    etag = Column(String)
    deleted = Column(String)

    def do_method(when, resource, request, lookup):

        method = request.method.lower()

        table = get_class_by_tablename(resource)

        if table != None:
            print("table {0} found!\n".format(table.__tablename__))
            methodCall = getattr(table, method)
            return methodCall(resource, request, lookup)

    def do_pre_method(resource, request, lookup):
        do_method('pre', resource, request, lookup)

    def do_post_method(resource, request, lookup):
        do_method('post', resource, request, lookup)

    def get(resource, request, lookup):

        print("METHOD WAS EXECUTED! resource: {0}\nrequest: {1}\nlookup: {2}\n".format(resource,request,lookup))

    def post(resource, request, lookup=None):

        print("METHOD WAS EXECUTED! resource: {0}\nrequest: {1}\nlookup: {2}\n".format(resource,request,lookup))

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

class Users(CommonTable):
    __tablename__ = 'users'

    login = Column(String)
    email = Column(String)
    password = Column(String)

registerSchema('boards')(Boards)
registerSchema('posts')(Posts)
registerSchema('users')(Users)
