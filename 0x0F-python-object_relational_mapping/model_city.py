#!/usr/bin/python3
'''my module to define cities'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """class definition of a City"""

    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")


State.cities = relationship(
    "City", order_by=City.id, back_populates="state")
