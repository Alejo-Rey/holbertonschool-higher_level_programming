#!/usr/bin/python3
''' list objects from State '''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Table, Column
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    ''' Create the engine '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    for data in session.query(State).all():
        print('{}: {}'.format(data.id, data.name))
