#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Class that represents the amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
