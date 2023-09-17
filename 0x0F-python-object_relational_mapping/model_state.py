#!/usr/bin/python3
"""
a python file that contains the class definition of a State
and an instance
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """a python file that contains the class definition of a
    State and an instance
    """

    __tablename__ = "states"
    id = Column(Integet, primary_key=True)
    name = Column(String(128), nullable=False)
