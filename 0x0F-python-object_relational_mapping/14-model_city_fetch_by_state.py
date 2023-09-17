#!/usr/bin/python3

"""
a script that prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    """a script that prints all City objects from the database
    hbtn_0e_14_usa
    """

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State
    from model_city import City

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]
                )
            )
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(
            State.name, City.id, City.name
            ).filter(State.id == City.state_id)
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    session.close()
