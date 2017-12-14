#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
