#!/usr/bin/python3
"""prints the State object with the name"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchName = sys.argv[4].split(";")[0].strip("'")

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(username, password, database, matchName),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Sesh = sessionmaker(bind=eng)
    session = Sesh()

    states = session.query(State).filter(State.name == matchName).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()
