from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
        Column,
        String,
        Integer,
        )

Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    topic_id = Column(Integer)
    reply_to_id = Column(Integer)
    board_id = Column(String)
    date = Column(Integer)
    author_id = Column(String)
    title = Column(String)
    post_text = Column(String)
    hash_id = Column(String)
