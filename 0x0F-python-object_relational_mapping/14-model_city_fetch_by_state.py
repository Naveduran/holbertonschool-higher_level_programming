#!/usr/bin/python3
"""prints all City objects from the database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)

    for state in session.query(City, State).join(State).all():
        print("{}: ({}) {}".format(state.name, city.state_id, city.name))

    session.close()
