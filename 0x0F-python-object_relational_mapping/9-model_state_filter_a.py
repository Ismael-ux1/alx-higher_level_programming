#!/usr/bin/python3
"""
List all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to get all state objects containing the letter 'a'
    states_with_a = (session.query(State).filter(State.name.like('%a%'))
                     .order_by(State.id).all())

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
