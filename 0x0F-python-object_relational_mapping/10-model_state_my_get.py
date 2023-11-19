#!/usr/bin/python3
"""Print first State object from the database hbtn_0e_6_usa"""

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

    stmt = select(State.id).where(State.name == bindparam("my_param"))
    
    with engine.connect() as connection:
        state = connection.execute(stmt, [{"my_param": argv[4]}])
        i = 0
        for row in state:
           i += 1
           print("{}".format(row.id))
        if i > 0:
            pass
        else:
            print("Not Found")

