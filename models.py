from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, create_engine
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


class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    text = Column(Text, nullable=False)
    excerpt = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    endpoint = Column(String(128), nullable=False, unique=True)
    is_deleted = Column(Boolean, nullable=False, default=False)
    is_draft = Column(Boolean, nullable=False, default=False)
    author_id = Column(Integer, ForeignKey('Users.id'))
    author = relationship('User', back_populates='posts')


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
