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
    st = session.query(State).order_by(
            State.id).filter(State.name == argv[4]).all()
    if st:
        for state in st:
            print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
