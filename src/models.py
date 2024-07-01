import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(400), unique=True)
    password = Column(String(500))

    # Relationship with Favorite
    favorites = relationship("Favorite", back_populates = "user")


class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    character_id = Column(Integer)
    planet_id = Column(Integer)
    specimen_id = Column(Integer)

    # Relationship with User
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates = "favorites")

    # Relationship with Character
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character", back_populates = "favorites")

    # Relationship with Planet
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet", back_populates = "favorites")

    # Relationship with Specimen
    specimen_id = Column(Integer, ForeignKey("specimen.id"))
    specimen = relationship("Specimen", back_populates = "favorites")


class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(350))
    specimen = Column(String(350))
    height_cm = Column(String(10))
    eye_color = Column(String(10))
    class_order = Column (String(50))

    # Relationship with Favorite
    favorites = relationship("Favorite", back_populates = "character")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    atmosphere = Column(Integer)
    native_creatures = Column(String(500))
    capital = Column(String(250))

    # Relationship with Favorite
    favorites = relationship("Favorite", back_populates = "planet")

class Specimen(Base):
    __tablename__ = "specimen"
    id = Column(Integer, primary_key=True)
    name = Column(String(400))
    ethnic_group = Column(String(400))
    height = Column(String(10))
    eye_color = Column(String(50))

    # Relationship with Favorite
    favorites = relationship("Favorite", back_populates = "specimen")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
