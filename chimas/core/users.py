from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
        Column,
        String,
        Integer,
        )

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    email = Column(String)
    password = Column(String)
