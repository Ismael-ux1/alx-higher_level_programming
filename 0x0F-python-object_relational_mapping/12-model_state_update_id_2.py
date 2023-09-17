#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the State object was found
    if state_to_update:
        # Update the name of the State object to "New Mexico"
        state_to_update.name = "New Mexico"

        # Commit the changes to the database
        session.commit()

    # Close the session
    session.close()
