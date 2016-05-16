from sqlalchemy.ext.declarative import declarative_base
from eve_sqlalchemy.decorators import registerSchema

from sqlalchemy import (
        Column,
        String,
        Integer,
        ForeignKey,
        DateTime )

from sqlalchemy import func

Base = declarative_base()

class CommonTable(Base):
    __abstract__ =  True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(String, default = func.now())
    updated = Column(String, default = func.now(), onupdate = func.now())
    etag = Column(String)

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
