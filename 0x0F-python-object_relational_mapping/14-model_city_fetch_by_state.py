#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects from the database and sort them by city id
    cities = session.query(City).order_by(City.id).all()

    # Print the City objects with their associated State name
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        state_name = state.name

        print('{}: ({}) {}'.format(state_name, city.id, city.name))

    # Close the session
    session.close()
