#!/usr/bin/python3
"""adds the State object Louisiana"""

import sys
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(username, password, database),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Sesh =sessionmaker(bind=eng)
    session = Sesh()

    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit
    s_object = session.query(State).order_by(State.id.desc().first)

    print(s_object.id)

    session.close()
