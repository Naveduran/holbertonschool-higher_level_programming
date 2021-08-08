#!/usr/bin/python3
"""prints the State object with the name passed as argument
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)
    session.add(State(name='Louisiana'))
    for state in session.query(
            State).filter(State.name.like('Louisiana')).all():
        print(state.id)
    session.commit()
    session.close()
