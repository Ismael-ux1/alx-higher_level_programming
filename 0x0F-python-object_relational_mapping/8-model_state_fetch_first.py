#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
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

    # Crate a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to get the first State object based on states.id
    first_state = session.query(State).order_by(State.id).first()

    # Check if the table is empty
    if first_state is None:
        print("Nothing")
    else:
        # Print the first State object
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
