from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from contextlib import contextmanager
import datetime

from settings import DATABASE_URL


Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    posts = relationship('Post', back_populates='author')

    def get_user(self):
        return {"id": self.id, "firstname": self.firstname, "lastname": self.lastname, "email": self.email}


class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    body = Column(String, nullable=False)
    excerpt = Column(String, nullable=False)
    endpoint = Column(String(64), nullable=False, unique=True)
    created_date = Column(Integer, nullable=False,
                          default=int(datetime.datetime.utcnow().timestamp()))
    updated_date = Column(DateTime, nullable=True,
                          onupdate=int(datetime.datetime.utcnow().timestamp()))
    is_draft = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey('Users.id'))
    author = relationship("User", back_populates="posts")


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
