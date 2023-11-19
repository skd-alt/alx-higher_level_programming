#!/usr/bin/python3
"""
defines the States Class model
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey


class City(Base):
    """
    City class defined
    id: primary key
    name: the state name
    state_id: foreign key for State table
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
