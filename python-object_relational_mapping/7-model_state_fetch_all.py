#!/usr/bin/python3
"""ists all State objects from the database"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(username, password, database),
                        pool_pre_ping=True)
    Sesh = sessionmaker(bind=eng)
    session = Sesh()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
