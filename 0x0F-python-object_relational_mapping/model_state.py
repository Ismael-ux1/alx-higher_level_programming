#!/usr/bin/python3
""" This script contains the class definition of a State and,
an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

""" Create an instance of declarative_base """
Base = declarative_base()


class State(Base):
    """
    This class definition represents the 'states' table in the database.
    Attributes:
    __tablename__ (str): The name of the database table.
    id (int): An auto-generated, unique integer representing the primary key.
    name (str): A string column with a maximum length of 128 characters.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
