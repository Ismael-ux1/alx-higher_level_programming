#!/usr/bin/python3
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a State instance
    state = State(name="California")

    # Create a City instance
    city = City(name="San Francisco")

    # Add the city to the state's cities relationship
    state.cities.append(city)

    # Add both state and city to the session
    session.add(state)
    session.commit()
    session.close()
