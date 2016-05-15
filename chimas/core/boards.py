#from sqlalchemy.ext.declarative import declarative_base
from eve_sqlalchemy.decorators import registerSchema
#from sqlalchemy.ext.hybrid import hybrid_property
from core import Base as Base

from sqlalchemy import (
        Column,
        String,
        Integer,
        )

#Base = declarative_base()

class Boards(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    created = Column(String)
    updated = Column(String)
    etag = Column(String)

registerSchema('boards')(Boards)
