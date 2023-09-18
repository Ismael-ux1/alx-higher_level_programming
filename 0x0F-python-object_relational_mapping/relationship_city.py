#!/usr/bin/python3
"""This module defines the City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base
from sys import argv


class City(Base):
    """Represents a city in the database.

    This class defines the structure and properties of a City object,
    including its name and a foreign key reference to the State it belongs to.

    Attributes:
        id (int): A unique identifier for the city.
        name (str): The name of the city.
        state_id (int): A foreign key reference to the,
        State that the city belongs to.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
