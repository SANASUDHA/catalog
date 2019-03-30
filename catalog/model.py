import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    picture = Column(String(250))


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime, nullable=False)
    user = relationship(User, backref="book")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
                'name': self.name,
                'id': self.id
            }


class BookItem(Base):
    __tablename__ = 'book_items'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    author = Column(String(250))
    poster = Column(String(500))
    price = Column(String(8))
    btype = Column(String(250))
    date = Column(DateTime, nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship(
        Book, backref=backref('book_items', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="book_items")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self. name,
            'author': self. author,
            'poster': self.poster,
            'price': self. price,
            'btype': self. btype,
            'date': self. date,
            'id': self. id
        }


engine = create_engine('sqlite:///mybook.db')
Base.metadata.create_all(engine)
