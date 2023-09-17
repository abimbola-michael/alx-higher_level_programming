#!/usr/bin/python3

"""
a script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    """a script that adds the State object “Louisiana” to the
    database hbtn_0e_6_usa
    """

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]
                )
            )
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    state = session.query(State).filter_by(name="Louisiana").first()
    print(state.id)

    session.commit()
