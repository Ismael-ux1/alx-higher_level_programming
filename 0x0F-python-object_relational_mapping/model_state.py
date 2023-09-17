#!/usr/bin/python3
""" This script contains the class definition of a State and,
an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from enum import unique

# Create an instance of declarative_base
Base = declarative_base()

Base = declarative_base())
# Define the state class


class State(Base):
    # Specify the name of the database table
    __tablename__ = 'states'

    # Define the columns of the states table
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
