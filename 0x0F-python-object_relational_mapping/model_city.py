#!/usr/bin/python3
""" Define City class that inherits from Base """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    cityclass: Define City class that inherits from Base

    Attributes:
        id (int): An auto-generated, unique integer representing the city's ID
    name (str): A string of up to 128 characters representing the city's name.
    state_id (int): An integer representing the foreign key,
    to the associated state's ID.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
