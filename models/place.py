#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


place_amenity = Table(
        'place_amenity', Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
                "Review",
                backref="place",
                cascade="delete")

        amenities = relationship(
                "Amenity",
                secondary=place_amenity,
                viewonly=False,
                backref="place_amenities")
    else:
        @property
        def reviews(self):
            """Relationship between Place and Review"""
            from models.review import Review
            from models import storage

            review_list = []
            dicts = storage.all(Review)
            for dic in dicts:
                if dic.place_id == self.id:
                    review_list.append(dic)

            return review_list

        @property
        def amenities(self):
            """Amenity getter"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
