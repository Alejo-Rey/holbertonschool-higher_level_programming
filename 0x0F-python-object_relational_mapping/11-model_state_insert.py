#!/usr/bin/python3
''' list objects from State '''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    data = session.query(State).filter(
        State.name == ("Louisiana")).one_or_none()
    if data:
        print('{}'.format(data.id))
    else:
        print('Not found')
