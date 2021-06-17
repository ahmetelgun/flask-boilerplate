from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from settings import DATABASE_URL
from contextlib import contextmanager

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(128), nullable=False)


if __name__ == '__main__':
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


@contextmanager
def DBContext(db_url=None):
    if not db_url:
        db_url = DATABASE_URL

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = scoped_session(Session)
    try:
        yield session
    finally:
        session.remove()

def create_test_db(test_db_url, fields):
    engine = create_engine(test_db_url)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(engine)
    with DBContext(test_db_url) as db:
        db.add_all(fields)
        db.commit()
