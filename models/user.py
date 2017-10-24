#!/usr/bin/python
""" holds class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """Representation of a user """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
       # cities = relationship("City", backref="state", cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
