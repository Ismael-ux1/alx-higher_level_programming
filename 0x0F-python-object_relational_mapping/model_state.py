#!/usr/bin/python3
""" This script contains the class definition of a State and,
an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Create an instance of declarative_base
Base = declarative_base()


# Define the state class
class State(Base):
    # Specify the name of the database table
    __tablename__ = 'states'

    # Define the id attribute
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
