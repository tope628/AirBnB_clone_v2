#!/usr/bin/python
""" holds class Place"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True),
                          Column('amenity_id', String(60), ForeignKey(
                              'amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """Representation of Place """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False,
            backref="place_amenities", cascade="delete")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        def __init__(self, *args, **kwargs):
            """initializes Place"""
            super().__init__(*args, **kwargs)

        @property
        def reviews(self):
            """returns Review instances w/ place_id = current Place.id"""
            all_instances = models.storage.all()
            query = []
            for key, value in all_instances.items():
                if key.startswith('Review') and getattr(
                        value, 'place_id') == self.id:
                    query.append(value)
            return query

        @property
        def amenities(self):
            """returns Amenity instances w/ place_id = current Place.id"""
            all_instances = models.storage.all()
            query = []
            for key, value in all_instances.items():
                if key.startswith('Amenity') and getattr(
                        value, 'place_id') == self.id:
                    query.append(value)
            return query
