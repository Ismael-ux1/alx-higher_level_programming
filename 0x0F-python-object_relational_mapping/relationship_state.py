#!/usr/bin/python3
"""This module defines the State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()


class State(Base):
    """Represents a state in the database.

    This class defines the structure and properties of a State object,
    including its name and a one-to-many relationship with City objects.

    Attributes:
        id (int): A unique identifier for the state.
        name (str): The name of the state.
        cities (relationship): A one-to-many relationship that links
            the state to multiple City objects. This allows accessing
            the cities associated with a particular state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    # Define the one-to-many relationship with City
    cities = relationship("City", backref="state")
