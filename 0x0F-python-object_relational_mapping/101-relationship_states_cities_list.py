#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@"
                           f"localhost:3306/{sys.argv[3]}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects and their related City objects
    # using the cities relationship
    states_with_cities = session.query(State).order_by(State.id).all()

    # Iterate over the results and print them
    for state in states_with_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    # Close the session
    session.close()
