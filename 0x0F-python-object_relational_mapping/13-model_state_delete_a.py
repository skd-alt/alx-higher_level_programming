#!/usr/bin/python3
"""Delete State objects"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, bindparam, select
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()
