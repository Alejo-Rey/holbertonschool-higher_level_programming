#!/usr/bin/python3
''' list objects from State '''

import sys
from model_state import Base, State
from model_city import City
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

    for st, cit in session.query(State, City).filter(
            State.id == City.state_id).all():
        print("{}: ({}) {}".format(st.name, cit.id, cit.name))
