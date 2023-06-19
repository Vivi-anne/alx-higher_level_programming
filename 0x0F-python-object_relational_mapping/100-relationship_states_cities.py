#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    calState = State(name='California')
    sfrCity = City(name='San Francisco')
    calState.cities.append(sfrCity)

    session.add(calState)
    session.add(sfrCity)
    session.commit()
