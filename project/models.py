from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from project.setup.db import models, db


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=False, nullable=False)
    description = Column(String(255), unique=False, nullable=False)
    trailer = Column(String(255), unique=False, nullable=False)
    year = Column(Integer, unique=False)
    rating = Column(Float, unique=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'), nullable=False)
    genre = relationship("Genre")
    director_id = Column(db.Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=False)
    director = relationship("Director")


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=False, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favourite_genre = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    genre = relationship('Genre')
